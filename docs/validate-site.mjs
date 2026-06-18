import fs from "node:fs/promises";
import path from "node:path";

const root = process.cwd();
const srcDir = path.join(root, "src");
const publicDir = path.join(root, "public");

const requiredPages = [
  "index.html",
  "study-plan.html",
  "site-visits.html",
  "activities-events.html",
  "cce-labs.html",
];

const forbiddenPages = [
  "about.html",
  "careers.html",
  "contact.html",
  "field-trips.html",
  "laboratories.html",
  "project-management.html",
  "smart-structures.html",
  "student-experience.html",
  "technologies.html",
];

const requiredContent = [
  "study-plan.json",
  "site-visits.json",
  "activities-events.json",
  "cce-labs.json",
  "media-usage.json",
];

async function assertFile(filePath, label = filePath) {
  try {
    const stat = await fs.stat(filePath);
    if (!stat.isFile()) throw new Error();
  } catch {
    throw new Error(`Missing required file: ${label}`);
  }
}

for (const page of requiredPages) {
  await assertFile(path.join(srcDir, page), page);
}

for (const page of forbiddenPages) {
  try {
    await fs.stat(path.join(srcDir, page));
    throw new Error(`Forbidden old page still exists in src: ${page}`);
  } catch (error) {
    if (error.code !== "ENOENT") throw error;
  }
}

for (const file of requiredContent) {
  await assertFile(path.join(srcDir, "content", file), `src/content/${file}`);
}

await assertFile(path.join(publicDir, "assets", "brand", "cce-logo.svg"), "public logo");

const studyPlan = JSON.parse(await fs.readFile(path.join(srcDir, "content", "study-plan.json"), "utf8"));
if (!Array.isArray(studyPlan.tracks) || studyPlan.tracks.length !== 2) {
  throw new Error("Study plan must contain exactly two tracks.");
}
for (const track of studyPlan.tracks) {
  if (track.totalCreditHours !== 144 || !track.validation?.equalsExpectedTotal) {
    throw new Error(`${track.name} does not validate to 144 credit hours.`);
  }
  const courseCount = track.semesters.flatMap((semester) => semester.courses).length;
  if (courseCount < 40) {
    throw new Error(`${track.name} has too few course entries.`);
  }
}

const siteVisits = JSON.parse(await fs.readFile(path.join(srcDir, "content", "site-visits.json"), "utf8"));
const activities = JSON.parse(await fs.readFile(path.join(srcDir, "content", "activities-events.json"), "utf8"));
const labs = JSON.parse(await fs.readFile(path.join(srcDir, "content", "cce-labs.json"), "utf8"));

if (siteVisits.items.length < 5) throw new Error("Expected at least five site visit cards.");
if (activities.items.length < 5) throw new Error("Expected at least five activity/event cards.");
if (labs.labs.length < 7) throw new Error("Expected at least seven lab cards from the PDF.");
if (labs.sourcePdf !== "Civil Lab Complex.pdf") throw new Error("CCE Labs must reference Civil Lab Complex.pdf.");

const usedImages = new Set();
for (const group of [siteVisits.items, activities.items, labs.labs, labs.gallery]) {
  for (const item of group) {
    if (usedImages.has(item.image)) {
      throw new Error(`Image repeated incorrectly: ${item.image}`);
    }
    usedImages.add(item.image);
    await assertFile(path.join(publicDir, item.image), item.image);
  }
}

for (const page of requiredPages) {
  const html = await fs.readFile(path.join(srcDir, page), "utf8");
  const navLinks = [...html.matchAll(/href="([^"]+\.html)"/g)].map((match) => match[1]);
  const allowedLinks = new Set(requiredPages);
  const bad = navLinks.filter((href) => !allowedLinks.has(href));
  if (bad.length) {
    throw new Error(`${page} links to non-pillar page(s): ${bad.join(", ")}`);
  }
}

console.log("Four-pillar static site validation passed.");
