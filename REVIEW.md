# Portfolio redesign — November 3, 2026

The previous site led with a chronological writing feed and a cloud-defense profile. Its main gaps for an application-security audience were the absence of the AppSec internship, missing current tooling projects, and limited paths from the introduction to concrete engineering work. The resume link escaped the GitHub Pages project path and used a filename absent from the repository. The historical PDF and gittuf writeup also contained retired percentage claims.

## Changes

- Repositioned the homepage around application security, source review, and security tooling, with selected work and experience before the writing archive.
- Added AppSec Assistant and automation-scripts, with scope boundaries and direct public source links.
- Rewrote the gittuf contribution article using the verified merged PRs; separated internship dates from later upstream merges and preserved collaborative attribution.
- Retained all 12 article URLs, moved discovery into a searchable/filterable archive, and added context distinguishing labs, coursework, and research.
- Replaced blanket “100% preventable” article stat cards with concrete security practices.
- Applied one local stylesheet and navigation system across 19 pages. Removed the browser Tailwind compiler, remote fonts, and embedded credential scripts.
- Added responsive layouts, native mobile navigation, keyboard focus, skip links, reduced-motion support, social preview metadata, and a sitemap.
- Linked the existing public project reports and replaced the stale resume download with an email request.
- Added a dependency-free site checker and a read-only CI workflow with pinned action commits.

## Verification

- Local checker: 19 pages and 429 local references pass, including file/fragment resolution, metadata, IDs, semantic landmarks, sitemap, and static CSP constraints.
- Verified that 61 code samples match the original text across the 11 migrated articles. The twelfth article, gittuf, was intentionally rewritten.
- Browser checks: all 19 pages fit a 390px viewport with no document-level horizontal overflow; each has one h1 and no broken images.
- Checked all 19 desktop layouts at 1440px, plus the three review steps, writing topic filters, combined search, no-match state, filter reset, and mobile menu Escape dismissal.
- External checks confirmed public project repositories, merged PRs, and credential links. Some destinations reject automated HEAD requests; PortSwigger destinations were independently retrieved successfully. LinkedIn rejects automated verification, so its existing profile link is retained without claiming a successful automated check.

## Remaining content maintenance

The historical resume PDF remains in the repository but is not promoted by the site. Replace it only after preparing and reviewing a current resume. Legacy research and lab articles retain their technical body content; this redesign is not an independent reproduction of their experiments or an exhaustive technical audit. OSWE is explicitly shown as training in progress.
