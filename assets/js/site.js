"use strict";
// All core content and navigation are available without JavaScript.
document.documentElement.classList.add("js");

const traceButtons = [...document.querySelectorAll("[data-trace]")];
const tracePanels = [...document.querySelectorAll("[data-trace-panel]")];
function showTrace(name) {
  traceButtons.forEach(button => {
    button.setAttribute("aria-pressed", String(button.dataset.trace === name));
    button.setAttribute("aria-controls", `trace-${button.dataset.trace}`);
  });
  tracePanels.forEach(panel => { panel.hidden = panel.dataset.tracePanel !== name; });
}
traceButtons.forEach(button => button.addEventListener("click", () => showTrace(button.dataset.trace)));
if (tracePanels.length) showTrace("input");

const archiveTools = document.querySelector("[data-archive-tools]");
if (archiveTools) {
  const search = document.querySelector("#writing-search");
  const filters = [...document.querySelectorAll("[data-filter]")];
  const items = [...document.querySelectorAll("[data-writing-item]")];
  const count = document.querySelector("[data-result-count]");
  const empty = document.querySelector("[data-empty-state]");
  let category = "All";
  function filterWriting() {
    const query = search.value.trim().toLocaleLowerCase();
    let visible = 0;
    items.forEach(item => {
      const matchesCategory = category === "All" || item.dataset.category === category;
      const matchesQuery = !query || item.textContent.toLocaleLowerCase().includes(query);
      item.hidden = !(matchesCategory && matchesQuery);
      if (!item.hidden) visible++;
    });
    filters.forEach(button => button.setAttribute("aria-pressed", String(button.dataset.filter === category)));
    count.textContent = `${visible} ${visible === 1 ? "note" : "notes"} ${query || category !== "All" ? "found" : "in the archive"}`;
    empty.hidden = visible > 0;
  }
  filters.forEach(button => button.addEventListener("click", () => {
    category = button.dataset.filter;
    filterWriting();
  }));
  search.addEventListener("input", filterWriting);
  archiveTools.hidden = false;
  filterWriting();
}
// Close the native mobile navigation after navigation or Escape.
const menu = document.querySelector(".mobile-menu");
if (menu) {
  menu.querySelectorAll("a").forEach(link => link.addEventListener("click", () => { menu.open = false; }));
  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && menu.open) {
      menu.open = false;
      menu.querySelector("summary").focus();
    }
  });
  document.addEventListener("click", event => {
    if (menu.open && !menu.contains(event.target)) menu.open = false;
  });
}
