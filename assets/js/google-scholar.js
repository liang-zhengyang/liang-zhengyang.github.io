(function () {
  "use strict";

  const settings = document.getElementById("google-scholar-loader");
  if (!settings) return;

  const normalizeTitle = (title) =>
    String(title).normalize("NFKD").toLowerCase().replace(/[^a-z0-9]+/g, "");
  const yearOf = (value) => /^\d{4}$/.test(String(value)) ? Number(value) : 0;
  const citationsOf = (value) => {
    const count = Number(value);
    return value != null && Number.isFinite(count) && count >= 0 ? count : null;
  };
  const safeUrl = (value) => {
    try {
      const url = new URL(value);
      return ["https:", "http:"].includes(url.protocol) ? url.href : null;
    } catch (_) {
      return null;
    }
  };
  const profileUrl = safeUrl(settings.dataset.profileUrl);
  const profileId = profileUrl ? new URL(profileUrl).searchParams.get("user") : null;

  function collectPublicationCards() {
    const container = document.getElementById("scholar-publications");
    if (!container) return [];
    // Keep the source Markdown outside the container for Jekyll's HTML parsing.
    let sibling = container.nextElementSibling;
    while (sibling && !/^H[1-6]$/.test(sibling.tagName)) {
      const next = sibling.nextElementSibling;
      if (sibling.classList.contains("paper-box")) container.appendChild(sibling);
      sibling = next;
    }
    const cards = Array.from(container.querySelectorAll(".paper-box"));
    cards.forEach((card) => {
      if (card.dataset.scholarYear) return;
      const paperLink = card.querySelector(".paper-box-text a[href*='arxiv.org/abs/']");
      const arxivId = paperLink && paperLink.href.match(/\/abs\/(\d{2})\d{2}\./);
      const badge = card.querySelector(".badge");
      const badgeYear = badge && badge.textContent.match(/\b\d{4}\b/);
      card.dataset.scholarYear = arxivId ? `20${arxivId[1]}` : badgeYear ? badgeYear[0] : "0";
    });
    return cards;
  }

  function filterPublications() {
    const select = document.getElementById("publication-year");
    const container = document.getElementById("scholar-publications");
    if (!select || !container) return;
    const cards = Array.from(container.querySelectorAll(".paper-box"));
    let visible = 0;
    cards.forEach((card) => {
      card.hidden = select.value !== "all" && String(yearOf(card.dataset.scholarYear)) !== select.value;
      if (!card.hidden) visible += 1;
    });
    const count = document.getElementById("publication-count");
    if (count) count.textContent = `${visible} of ${cards.length} publications`;
  }

  function refreshYearFilter() {
    const filters = document.getElementById("publication-filters");
    const select = document.getElementById("publication-year");
    if (!filters || !select) return;
    const cards = collectPublicationCards();
    if (!cards.length) return;
    const selected = select.value;
    const counts = new Map();
    cards.forEach((card) => {
      const year = yearOf(card.dataset.scholarYear);
      counts.set(year, (counts.get(year) || 0) + 1);
    });
    const options = document.createDocumentFragment();
    const addOption = (value, label) => {
      const option = document.createElement("option");
      option.value = value;
      option.textContent = label;
      options.appendChild(option);
    };
    addOption("all", "All years");
    [...counts.keys()].sort((a, b) => b - a).forEach((year) =>
      addOption(String(year), `${year || "Undated"} (${counts.get(year)})`));
    select.replaceChildren(options);
    select.value = selected !== "all" && counts.has(Number(selected)) ? selected : "all";
    filters.hidden = false;
    filterPublications();
  }

  function validateData(data) {
    if (!data || typeof data !== "object" || citationsOf(data.citedby) === null) {
      throw new Error("Invalid Scholar data");
    }
    if (profileId && data.scholar_id !== profileId) {
      throw new Error("Scholar data belongs to a different profile");
    }
    return data;
  }

  function addLink(parent, label, url) {
    const href = safeUrl(url);
    if (!href) return;
    const link = document.createElement("a");
    link.href = href;
    link.textContent = label;
    parent.appendChild(link);
  }

  function updateCitations(data) {
    const total = document.getElementById("total_cit");
    if (total) total.textContent = data.citedby;
    const publications = data.publications || {};
    const byTitle = data.publications_by_title || {};
    document.querySelectorAll(".show_paper_citations").forEach((element) => {
      const paper = publications[element.dataset.scholarId] ||
        byTitle[normalizeTitle(element.dataset.title || "")];
      const count = paper ? citationsOf(paper.num_citations) : null;
      element.textContent = count === null ? "" : `| Citations: ${count}`;
    });
  }

  function createCard(paper) {
    const card = document.createElement("div");
    card.className = "paper-box scholar-paper";
    const text = document.createElement("div");
    text.className = "paper-box-text";
    const title = document.createElement("p");
    addLink(title, paper.title, safeUrl(paper.url) || paper.scholar_url || profileUrl);
    if (!title.firstChild) title.textContent = paper.title;
    text.appendChild(title);
    if (paper.authors) {
      const authors = document.createElement("p");
      // Scholar author lists may be abbreviated; never invent full names or roles.
      authors.textContent = paper.authors;
      text.appendChild(authors);
    }
    const links = document.createElement("p");
    addLink(links, "Google Scholar", paper.scholar_url || profileUrl);
    const citations = document.createElement("span");
    citations.className = "show_paper_citations";
    citations.dataset.scholarId = paper.author_pub_id || "";
    citations.dataset.title = paper.title;
    const strong = document.createElement("strong");
    strong.appendChild(citations);
    links.appendChild(document.createTextNode(" "));
    links.appendChild(strong);
    text.appendChild(links);
    card.appendChild(text);
    return card;
  }

  function updateCard(card, paper) {
    const year = yearOf(paper.year);
    if (year) card.dataset.scholarYear = year;
    const marker = card.querySelector(".show_paper_citations");
    if (marker) {
      marker.dataset.scholarId = paper.author_pub_id || "";
      marker.dataset.title = paper.title;
    }
    const text = card.querySelector(".paper-box-text");
    const title = text.querySelector("p a");
    if (title) title.textContent = paper.title;
    // Keep curated images, full author lists, contribution marks and resource links.
    let details = text.querySelector(".publication-details");
    if (!details) {
      details = document.createElement("p");
      details.className = "publication-details";
      text.insertBefore(details, text.lastElementChild);
    }
    const venue = String(paper.venue || "").trim();
    details.textContent = venue;
    if (year && !venue.includes(String(year))) {
      details.textContent += `${venue ? " · " : ""}${year}`;
    }
    details.hidden = !details.textContent;
  }

  function updatePublications(data) {
    const container = document.getElementById("scholar-publications");
    if (!container || settings.dataset.autoPublications !== "true") return;
    // Old citation-only snapshots work until the next successful crawler run.
    if (!Array.isArray(data.publication_list) || !data.publication_list.length) return;
    const papers = data.publication_list.filter((paper) =>
      paper && typeof paper.title === "string" && paper.title.trim());
    if (!papers.length) return;

    const cards = collectPublicationCards();
    const byId = new Map();
    const byTitle = new Map();
    cards.forEach((card) => {
      const marker = card.querySelector(".show_paper_citations");
      if (!marker) return;
      if (marker.dataset.scholarId) byId.set(marker.dataset.scholarId, card);
      byTitle.set(normalizeTitle(marker.dataset.title || ""), card);
    });

    papers.forEach((paper) => {
      const key = normalizeTitle(paper.title);
      let card = byId.get(paper.author_pub_id) || byTitle.get(key);
      if (!card) {
        card = createCard(paper);
        cards.push(card);
      }
      updateCard(card, paper);
      if (paper.author_pub_id) byId.set(paper.author_pub_id, card);
      byTitle.set(key, card);
    });
    // Stable sorting preserves the curated order within each publication year.
    cards.sort((a, b) => yearOf(b.dataset.scholarYear) - yearOf(a.dataset.scholarYear));
    const fragment = document.createDocumentFragment();
    cards.forEach((card) => fragment.appendChild(card));
    container.appendChild(fragment);
    refreshYearFilter();
  }

  async function load() {
    const dailyCacheKey = new Date().toISOString().slice(0, 10);
    const urls = [...new Set([settings.dataset.url, settings.dataset.fallbackUrl].filter(Boolean))];
    const needsPublications = settings.dataset.autoPublications === "true" &&
      document.getElementById("scholar-publications");
    let citationOnlyData = null;
    for (const url of urls) {
      try {
        const response = await fetch(`${url}?v=${dailyCacheKey}`, {
          cache: "no-store",
          signal: AbortSignal.timeout(15000),
        });
        if (!response.ok) throw new Error(`Scholar request failed: ${response.status}`);
        const data = validateData(await response.json());
        // A CDN may still serve the old schema after the crawler has published
        // the new list. Try the direct source before accepting that snapshot.
        if (needsPublications && url !== urls[urls.length - 1] &&
            (!Array.isArray(data.publication_list) || !data.publication_list.length)) {
          citationOnlyData = data;
          continue;
        }
        updatePublications(data);
        updateCitations(data);
        return;
      } catch (error) {
        console.warn("Unable to load Google Scholar data.", error);
      }
    }
    if (citationOnlyData) updateCitations(citationOnlyData);
  }

  function initialize() {
    refreshYearFilter();
    const select = document.getElementById("publication-year");
    if (select) select.addEventListener("change", filterPublications);
    load();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialize, { once: true });
  } else {
    initialize();
  }
})();
