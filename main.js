import { APPLICATION_LINK } from "./config.js";

const content = {
  studyPlan: null,
  siteVisits: null,
  activitiesEvents: null,
  cceLabs: null,
};

const navItems = [
  ["Home", "index.html"],
  ["Study Plan", "study-plan.html"],
  ["Site Visits", "site-visits.html"],
  ["Activities & Events", "activities-events.html"],
  ["CCE Labs", "cce-labs.html"],
];

const pillars = [
  {
    title: "Study Plan",
    href: "study-plan.html",
    kicker: "144 credit hours",
    text: "Interactive semester-by-semester plans for Smart Structures and Project Management.",
    icon: "M12 4v16M4 8h16M4 16h16",
  },
  {
    title: "Site Visits",
    href: "site-visits.html",
    kicker: "Field learning",
    text: "Construction, infrastructure, consultancy, and safety exposure through curated site visits.",
    icon: "M5 18h14M7 18V9l5-4 5 4v9M10 18v-5h4v5",
  },
  {
    title: "Activities & Events",
    href: "activities-events.html",
    kicker: "Student engagement",
    text: "Competitions, academic showcases, workshops, civil engineering days, and department activities.",
    icon: "M7 7h10v10H7zM4 4h16v16H4z",
  },
  {
    title: "CCE Labs",
    href: "cce-labs.html",
    kicker: "Lab complex",
    text: "PDF-sourced CCE lab cards covering testing, surveying, hydraulics, soil, and environmental learning.",
    icon: "M10 3v6l-5 8a3 3 0 0 0 2.6 4.5h8.8A3 3 0 0 0 19 17l-5-8V3",
  },
];

const page = document.body.dataset.page;

function currentPage() {
  const file = window.location.pathname.split("/").pop();
  return file || "index.html";
}

function icon(path) {
  return `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="${path}" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
}

function renderShell() {
  const active = currentPage();
  const header = document.querySelector("#site-header");

  if (header) {
    header.innerHTML = `
      <div class="nav-shell">
        <a class="brand" href="index.html" aria-label="CCE Department home">
          <img src="assets/brand/cce-logo.svg" alt="CCE Department logo">
          <span>Civil Engineering Program</span>
        </a>

        <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav">
          <span></span><span></span><span></span>
          <span class="sr-only">Menu</span>
        </button>

        <nav id="main-nav" class="main-nav" aria-label="Main navigation">
          ${navItems
            .map(
              ([label, href]) =>
                `<a href="${href}"${
                  href === active ? ' aria-current="page"' : ""
                }>${label}</a>`
            )
            .join("")}
        </nav>

        <a class="apply-cta header-apply" href="${APPLICATION_LINK}" data-apply-link target="_blank" rel="noopener noreferrer">
          Apply Now
        </a>
      </div>
    `;

    const toggle = header.querySelector(".nav-toggle");
    const nav = header.querySelector("#main-nav");

    toggle?.addEventListener("click", () => {
      const open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("is-open", !open);
    });
  }

  const footer = document.querySelector("#site-footer");

  if (footer) {
    footer.innerHTML = `
      <div class="footer-grid">
        <div>
          <img src="assets/brand/cce-logo.svg" alt="CCE Department logo">
          <p>Focused microsite for the Civil Engineering Program / CCE Department.</p>
        </div>

        <nav aria-label="Footer navigation">
          ${navItems.map(([label, href]) => `<a href="${href}">${label}</a>`).join("")}
        </nav>

        <a class="apply-cta footer-apply" href="${APPLICATION_LINK}" target="_blank" rel="noopener noreferrer">
          Apply Now
        </a>
      </div>
    `;
  }
}

function bindApplyLinks() {
  document.querySelectorAll("[data-apply-link]").forEach((link) => {
    link.setAttribute("href", APPLICATION_LINK);
    link.setAttribute("target", "_blank");
    link.setAttribute("rel", "noopener noreferrer");

    link.addEventListener("click", (event) => {
      event.preventDefault();
      window.open(APPLICATION_LINK, "_blank", "noopener,noreferrer");
    });
  });
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function list(items) {
  return `<ul>${items.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>`;
}

function renderHome() {
  const cards = document.querySelector("#pillar-cards");
  if (!cards) return;

  cards.innerHTML = pillars
    .map(
      (pillar, index) => `
    <a class="pillar-card" href="${pillar.href}" style="--i:${index}">
      <span class="card-icon">${icon(pillar.icon)}</span>
      <span class="eyebrow">${pillar.kicker}</span>
      <strong>${pillar.title}</strong>
      <span>${pillar.text}</span>
    </a>
  `
    )
    .join("");
}

function ensureModal() {
  let modal = document.querySelector("#course-modal");

  if (!modal) {
    modal = document.createElement("dialog");
    modal.id = "course-modal";
    modal.innerHTML = `
      <div class="modal-panel">
        <button class="modal-close" type="button">Close</button>
        <div id="course-modal-body"></div>
      </div>
    `;

    document.body.append(modal);

    modal.querySelector(".modal-close").addEventListener("click", () => modal.close());

    modal.addEventListener("click", (event) => {
      if (event.target === modal) modal.close();
    });
  }

  return modal;
}

function openCourse(course) {
  const modal = ensureModal();
  const body = modal.querySelector("#course-modal-body");

  body.innerHTML = `
    <p class="eyebrow">${escapeHtml(course.courseCode)} / ${escapeHtml(course.type)} / ${course.creditHours} CH</p>
    <h2>${escapeHtml(course.courseName)}</h2>
    <p>${escapeHtml(course.description)}</p>
  `;

  modal.showModal();
}

function courseButton(course) {
  return `
    <div class="course-line">
      <span class="code">${escapeHtml(course.courseCode)}</span>
      <button type="button" class="course-link">${escapeHtml(course.courseName)}</button>
      <span class="credits">${course.creditHours} CH</span>
    </div>
  `;
}

function renderPage() {
  if (page === "home") renderHome();
}

renderShell();
bindApplyLinks();

async function loadJson(path) {
  const response = await fetch(path);
  if (!response.ok) throw new Error(`Failed to load ${path}`);
  return response.json();
}

Promise.all([
  loadJson("study-plan.json"),
  loadJson("site-visits.json"),
  loadJson("activities-events.json"),
  loadJson("cce-labs.json"),
])
  .then(([studyPlan, siteVisits, activitiesEvents, cceLabs]) => {
    content.studyPlan = studyPlan;
    content.siteVisits = siteVisits;
    content.activitiesEvents = activitiesEvents;
    content.cceLabs = cceLabs;

    renderPage();
  })
  .catch((error) => {
    console.error(error);
    const main = document.querySelector("main");

    if (main) {
      main.insertAdjacentHTML(
        "beforeend",
        '<section class="section"><div class="section-inner">Content could not be loaded.</div></section>'
      );
    }
  });
