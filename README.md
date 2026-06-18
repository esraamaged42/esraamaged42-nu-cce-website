# CCE Department / Civil Engineering Program Microsite

Focused static English microsite for the Civil Engineering Program / CCE Department at Nile University.

The website is intentionally organized around exactly four pillars:

1. Study Plan
2. Site Visits
3. Activities & Events
4. Videos& Reels
5. CCE Labs

The top navigation contains only:

- Home
- Study Plan
- Site Visits
- Activities & Events
- Videos & Reels
- CCE Labs

## Project Structure

Main pages:

- `src/index.html`
- `src/study-plan.html`
- `src/site-visits.html`
- `src/activities-events.html`
- `src/cce-labs.html`

Editable content:

- `src/content/study-plan.json`
- `src/content/site-visits.json`
- `src/content/activities-events.json`
- `src/content/cce-labs.json`
- `src/content/media-usage.json`

Shared configuration:

- `src/assets/js/config.js` stores the official Apply Now URL.

Public optimized assets:

- `public/assets/brand/cce-logo.svg`
- `public/assets/graphics/cce-hero-visual.svg`
- `public/assets/images/site-visits/`
- `public/assets/images/activities/`
- `public/assets/images/labs/`

The frontend is a dependency-free static stack using HTML, CSS, modern JavaScript modules, JSON content files, and Node-based dev/build scripts.

## NU Palette

The NU-inspired visual palette is centralized in:

```text
src/assets/css/styles.css
```

Look for the `:root` block. It defines the shared color tokens used across the navbar, hero, buttons, cards, study-plan controls, course details, and footer:

- `--nu-primary`
- `--nu-deep`
- `--nu-navy`
- `--nu-sky`
- `--nu-ice`
- `--nu-fog`
- `--nu-accent`

The palette was aligned to the available CCE/Nile University logo in the root folder and kept to blue, navy, sky, white, and soft background tones for a focused department microsite.

## Run Locally

```bash
npm install
npm run dev
```

Open the URL printed in the terminal, usually:

```text
http://127.0.0.1:4173
```

## Build

```bash
npm run build
```

The deployable static site is generated in:

```text
dist/
```

## Validate

```bash
npm run validate
```

Validation checks:

- only the five required pages exist
- the navigation links point only to the four required sections plus Home
- the logo exists
- the CCE Labs content references `Civil Lab Complex.pdf`
- all referenced images exist
- images are not repeated across sections
- both study-plan tracks validate to 144 credit hours

## Study Plan Updates

Source workbook:

```text
2023 Bylaws_3_3_2025_CVL.xlsx
```

Regenerate the study-plan content:

```bash
python3 scripts/extract-study-plan.py
```

The script writes:

```text
src/content/study-plan.json
```

Each course includes:

- course code
- course name
- credit hours
- semester
- track
- type
- description
- skills
- job-market relevance
- practical applications
- related careers

Official course descriptions were not included in the workbook. Current descriptions are concise generic descriptions based on course titles and civil engineering context.

## Media Updatesadel898
nu-cce-website
Repository navigation
Code
Issues
1
 (1)
Pull requests
Actions
Projects
Security and quality
Insights
Settings
Files
Go to file
t
T
CCE Activities & Events
Site Visits


Regenerate optimized media and section content:

```bash
python3 scripts/prepare-media.py
```

This script:

- copies the root `CCE.png` logo into `public/assets/brand/cce-logo.svg`
- selects non-overlapping site visit images
- selects non-overlapping activity/event images
- extracts CCE lab images from `Civil Lab Complex.pdf`
- writes section JSON files for Site Visits, Activities & Events, and CCE Labs

To replace an image later:

1. Update the relevant list inside `scripts/prepare-media.py`.
2. Run `python3 scripts/prepare-media.py`.
3. Run `npm run validate`.

Image display behavior is centralized in `src/assets/css/styles.css` through `.media-frame` and `.media-image`. Gallery, event, site visit, and lab photos use `object-fit: contain` inside fixed-ratio frames so the full image remains visible without stretching, squeezing, or forced cropping. When replacing media, use good-quality source images and keep the generated image path referenced in the relevant JSON content file.

If a new section needs a photo card, reuse the existing `renderCardGallery` structure in `src/assets/js/main.js` so the same non-distorting image treatment is applied.

## Apply Link

The official admissions link is stored once in:

```text
src/assets/js/config.js
```

Update `APPLICATION_LINK` there if Nile University changes the application URL. Header, homepage, and footer Apply Now buttons read from this constant and open the admissions portal in a new browser tab.

## Custom Hero Visual

The homepage hero does not use existing lab, site, or activity photos. It uses a custom SVG created for this project:

```text
public/assets/graphics/cce-hero-visual.svg
```

## Deploy to Cloudflare Pages

Use these settings:

- Framework preset: None
- Build command: `npm run build`
- Build output directory: `dist`
- Install command: `npm install`

## Deploy to GitHub Pages

Use a GitHub Actions workflow that runs:

```bash
npm install
npm run build
```

Then publish the `dist/` folder to GitHub Pages.

The site uses relative links, so it can work under a GitHub Pages repository subpath.

## Reports

Additional documentation:

- `STUDY_PLAN_EXTRACTION_REPORT.md`
- `MEDIA_USAGE_REPORT.md`
  ## Updates
  Add an extra icon titled "Videos & Reels" beside the four main sections: CCE Labs, Study Plan, Site Visits, and Activities & Events. I will upload a folder containing the videos and reels for this section.
  . Remove the word "PDF" from the sentence:
   "Additional lab details from the Civil Lab Complex. PDF"
  . Add a new item under the Site Visits section titled:
   "Site Visits to Leading Construction Companies"-add the uploaded photos and use the following description:
"Program senior students have visited some well-known construction companies such as Arab Contractors, Orascom, CCC, Redcon, Bauer Egypt, Palm Hills, New Giza, and ZED."
Improve the overall website design and color scheme. The current design feels too simple and childish. Please make it more professional, modern, and visually appealing, with a stronger use of Nile University’s blue identity. Add suitable engineering-related graphics and improve the cover page to make it more smart, professional, attractive, and catchy.
  
