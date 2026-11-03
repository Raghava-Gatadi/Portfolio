#!/usr/bin/env python3
"""Dependency-free integration checks for this GitHub Pages site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SITE = 'https://raghava-gatadi.github.io/Portfolio/'

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.duplicates = []
        self.references = []
        self.h1 = 0
        self.main = 0
        self.title = ''
        self.in_title = False
        self.description = ''
        self.canonical = ''
        self.errors = []
        self.lang = ''
        self.csp = ''
        source = path.read_text(encoding='utf-8')
        if '__PRESERVE_CODE_' in source: self.errors.append('unresolved formatting placeholder')
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html': self.lang = attrs.get('lang', '')
        if tag == 'h1': self.h1 += 1
        if tag == 'main': self.main += 1
        if tag == 'title': self.in_title = True
        if attrs.get('id'):
            if attrs['id'] in self.ids: self.duplicates.append(attrs['id'])
            self.ids.add(attrs['id'])
        if tag == 'meta':
            if attrs.get('name') == 'description': self.description = attrs.get('content', '')
            if attrs.get('http-equiv', '').lower() == 'content-security-policy': self.csp = attrs.get('content', '')
            if attrs.get('property') == 'og:image':
                val = attrs.get('content', '')
                if val.startswith(SITE) and not (ROOT / val[len(SITE):]).is_file():
                    self.errors.append('missing social preview image')
        if tag == 'link' and attrs.get('rel') == 'canonical': self.canonical = attrs.get('href', '')
        if tag in ('a', 'link', 'script', 'img'):
            val = attrs.get('src') if tag in ('script', 'img') else attrs.get('href')
            if val is not None:
                self.references.append(val)
                if val.startswith('/'):
                    self.errors.append('root-relative path breaks project hosting: ' + val)
            if tag == 'img' and not attrs.get('alt'): self.errors.append('image is missing alt text')
            if tag == 'a' and attrs.get('target') == '_blank' and 'noopener' not in attrs.get('rel', ''):
                self.errors.append('new-window link is missing noopener')
            if tag in ('script', 'img') and val and urlsplit(val).scheme:
                self.errors.append('unexpected external runtime resource: ' + val)
            if tag == 'link' and attrs.get('rel') == 'stylesheet' and val and urlsplit(val).scheme:
                self.errors.append('unexpected external stylesheet: ' + val)
        if tag == 'script' and not attrs.get('src'): self.errors.append('inline script blocked by site CSP')
        if tag == 'style' or 'style' in attrs: self.errors.append('inline style blocked by site CSP')
        if any(k.startswith('on') for k in attrs): self.errors.append('inline event handler blocked by site CSP')
        if tag in ('iframe', 'object', 'embed', 'form'): self.errors.append('unexpected third-party embed or form')

    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False

    def handle_data(self, data):
        if self.in_title: self.title += data


def check():
    pages = {p: Page(p) for p in sorted(ROOT.rglob('*.html')) if '.git' not in p.parts}
    errors = []
    references = 0
    titles = set()
    for path, page in pages.items():
        name = str(path.relative_to(ROOT))
        if page.h1 != 1: page.errors.append('expected exactly one h1')
        if page.main != 1: page.errors.append('expected exactly one main landmark')
        if page.lang != 'en': page.errors.append('expected English document language')
        if not page.description: page.errors.append('missing description')
        if not page.title.strip() or page.title in titles: page.errors.append('missing or duplicate title')
        titles.add(page.title)
        if page.canonical != SITE + name: page.errors.append('incorrect canonical URL')
        if not page.csp or "object-src 'none'" not in page.csp: page.errors.append('missing content security policy')
        if page.duplicates: page.errors.append('duplicate IDs: ' + ', '.join(page.duplicates))
        if 'main' not in page.ids or 'top' not in page.ids: page.errors.append('missing shared skip/back anchor')
        for ref in page.references:
            url = urlsplit(ref)
            if url.scheme or url.netloc: continue
            references += 1
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(ROOT):
                page.errors.append('link escapes site: ' + ref)
                continue
            if target.is_dir(): target = target / 'index.html'
            if not target.is_file(): page.errors.append('missing file: ' + ref)
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                page.errors.append('missing anchor: ' + ref)
        errors.extend(name + ': ' + error for error in page.errors)
    sitemap = ET.parse(ROOT / 'sitemap.xml').getroot()
    urls = {node.text for node in sitemap.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
    expected = {SITE + str(path.relative_to(ROOT)) for path in pages}
    if urls != expected: errors.append('sitemap and HTML pages do not match')
    if not (ROOT / '.nojekyll').exists(): errors.append('missing .nojekyll')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: {len(pages)} pages, {references} local references, metadata, CSP, semantic landmarks, and sitemap.')
    return 0

if __name__ == '__main__':
    sys.exit(check())
