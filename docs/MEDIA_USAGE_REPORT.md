# Media Usage Report

## Logo

Root logo used:

- Source: `CCE.png`
- Output: `public/assets/brand/cce-logo.svg`

Note: the source file has a `.png` extension but contains SVG markup. The website preserves it as SVG to avoid distortion and keep quality.

The logo appears in:

- header/navbar
- homepage first viewport through the header only
- footer

The duplicate logo previously shown inside the homepage hero content was removed so the first viewport presents one clean logo instance in the navbar/header area.

## Image Display Handling

Photo cards across Site Visits, Activities & Events, and CCE Labs now use the shared `.media-frame` / `.media-image` treatment in `src/assets/css/styles.css`.

- Photos are displayed with `object-fit: contain`.
- Fixed-ratio frames prevent layout shifts across desktop, tablet, and mobile.
- Neutral NU-blue background fills and a subtle blurred backdrop avoid empty-looking letterboxing without stretching or cropping the source photo.
- The custom homepage hero SVG is not a reused site, activity, or lab photo and is allowed to scale naturally without forced dimensions.

## Custom Hero Visual

The homepage hero does not use any provided lab, site, or activity photo. It uses a custom SVG created for this project:

- `public/assets/graphics/cce-hero-visual.svg`

The visual uses blueprint grid lines, structural forms, bridge/truss geometry, gradients, and civil engineering graphic elements.

## Site Visits Images

Images used only in the Site Visits section:

- `Site Visits/Ahli Stadium Visit/FB_IMG_1781446325958.jpg` -> `public/assets/images/site-visits/ahli-stadium-site-visit.webp`
- `Site Visits/Arkan205- Site Visit/FB_IMG_1781447202766.jpg` -> `public/assets/images/site-visits/arkan-construction-site.webp`
- `Site Visits/Cairo Metro Visit/FB_IMG_1781452768558.jpg` -> `public/assets/images/site-visits/cairo-metro-field-visit.webp`
- `Site Visits/Construction Site/FB_IMG_1781450604888.jpg` -> `public/assets/images/site-visits/construction-site-exposure.webp`
- `Site Visits/Dar Al-Hansasah Visit/FB_IMG_1781446567189.jpg` -> `public/assets/images/site-visits/engineering-consultancy-visit.webp`

These images were selected because they clearly show site or field-visit contexts. They are not reused in Activities & Events or CCE Labs.

## Activities & Events Images

Images used only in the Activities & Events section:

- `CCE Activities & Events/The Earthquake Competition Event/FB_IMG_1781452418859.jpg` -> `public/assets/images/activities/earthquake-competition.webp`
- `CCE Activities & Events/Spaghetti Competition Celebration/FB_IMG_1781452625318.jpg` -> `public/assets/images/activities/spaghetti-structure-competition.webp`
- `CCE Activities & Events/Civil Engineering Day/FB_IMG_1781451993743.jpg` -> `public/assets/images/activities/civil-engineering-day.webp`
- `CCE Activities & Events/Graduation Project Defense/FB_IMG_1781452901402.jpg` -> `public/assets/images/activities/graduation-project-defense.webp`
- `CCE Activities & Events/STEM & high school - hands-on activities/FB_IMG_1781451782262.jpg` -> `public/assets/images/activities/hands-on-workshop.webp`
- `CCE Activities & Events/CCE Bazaar/FB_IMG_1781452200550.jpg` -> `public/assets/images/activities/cce-bazaar-models.webp`

These images are not reused in Site Visits or CCE Labs.

## CCE Labs PDF Images

PDF source:

- `Civil Lab Complex.pdf`

The PDF contains 9 pages. Text extracted from the PDF identifies these lab-related pages:

- Survey lab
- Concrete & Materials lab
- Soil mechanics lab
- the Meteorology Lab
- Hydraulics lab
- Transportation & Asphalt lab
- Environmental lab

Images extracted and used for the CCE Labs section:

- page 1 embedded image 2 -> `public/assets/images/labs/structural-testing-area.webp`
- page 2 embedded image 1 -> `public/assets/images/labs/lab-instruction-room.webp`
- page 3 embedded image 1 -> `public/assets/images/labs/surveying-laboratory.webp`
- page 3 embedded image 2 -> `public/assets/images/labs/surveying-equipment-detail.webp`
- page 4 embedded image 1 -> `public/assets/images/labs/concrete-materials-laboratory.webp`
- page 4 embedded image 2 -> `public/assets/images/labs/materials-testing-detail.webp`
- page 5 embedded image 1 -> `public/assets/images/labs/soil-mechanics-laboratory.webp`
- page 6 embedded image 1 -> `public/assets/images/labs/meteorology-laboratory.webp`
- page 7 embedded image 1 -> `public/assets/images/labs/hydraulics-laboratory.webp`
- page 8 embedded image 1 -> `public/assets/images/labs/transportation-asphalt-laboratory.webp`
- page 9 embedded image 1 -> `public/assets/images/labs/environmental-laboratory.webp`

The CCE Labs section uses only images extracted from the PDF, not event or site-visit photos.

## Ignored Media

Ignored items:

- repeated `Image9.png` logo/header objects inside `Civil Lab Complex.pdf`, because they are not lab photography
- duplicate or near-duplicate event photos, to avoid visual repetition
- duplicate or near-duplicate site visit photos, to keep the gallery focused
- videos in `CCE Activities & Events/Videos`, because the requested site is a static image-led microsite
- old generated WebP files from the previous unsuitable site version, removed from `src/assets/images`

## Repetition Confirmation

No optimized image is reused across Site Visits, Activities & Events, and CCE Labs. Site visit images come only from the `Site Visits` folder. Activity images come only from `CCE Activities & Events`. Lab images come only from `Civil Lab Complex.pdf`.
