from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image, ImageOps
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "src" / "content"
PUBLIC_DIR = ROOT / "public"
ASSET_DIR = PUBLIC_DIR / "assets"
IMAGE_DIR = ASSET_DIR / "images"
BRAND_DIR = ASSET_DIR / "brand"
PDF_PATH = ROOT / "Civil Lab Complex.pdf"
LOGO_PATH = ROOT / "CCE.png"


SITE_VISITS = [
    {
        "title": "Ahli Stadium Visit",
        "source": "Site Visits/Ahli Stadium Visit/FB_IMG_1781446325958.jpg",
        "image": "site-visits/ahli-stadium-site-visit.webp",
        "alt": "Students wearing safety vests during a stadium site visit",
        "learningFocus": ["Construction site exposure", "On-site safety awareness", "Project execution and management"],
        "caption": "Students observe construction coordination, safety practices, and project delivery in a real site environment.",
    },
    {
        "title": "Arkan 205 Site Visit",
        "source": "Site Visits/Arkan205- Site Visit/FB_IMG_1781447202766.jpg",
        "image": "site-visits/arkan-construction-site.webp",
        "alt": "Civil engineering students at an active construction project",
        "learningFocus": ["Construction sequencing", "Structural systems observation", "Site communication"],
        "caption": "A field visit focused on construction sequencing, site organization, and structural work in progress.",
    },
    {
        "title": "Cairo Metro Visit",
        "source": "Site Visits/Cairo Metro Visit/FB_IMG_1781452768558.jpg",
        "image": "site-visits/cairo-metro-field-visit.webp",
        "alt": "Civil engineering students observing Cairo Metro construction works",
        "learningFocus": ["Infrastructure delivery", "Construction site exposure", "Safety awareness"],
        "caption": "Students connect transportation infrastructure concepts with large-scale site execution.",
    },
    {
        "title": "Construction Site Visit",
        "source": "Site Visits/Construction Site/FB_IMG_1781450604888.jpg",
        "image": "site-visits/construction-site-exposure.webp",
        "alt": "Student group standing at a construction site",
        "learningFocus": ["Site logistics", "Project execution and management", "Civil engineering practice"],
        "caption": "General construction site exposure for understanding field workflow, logistics, and professional roles.",
    },
    {
        "title": "Dar Al-Handasah Visit",
        "source": "Site Visits/Dar Al-Hansasah Visit/FB_IMG_1781446567189.jpg",
        "image": "site-visits/engineering-consultancy-visit.webp",
        "alt": "Civil engineering students visiting a professional engineering consultancy",
        "learningFocus": ["Consultancy workflows", "Design coordination", "Professional practice"],
        "caption": "A consultancy-oriented visit introducing design coordination, engineering documentation, and professional practice.",
    },
]

ACTIVITIES = [
    {
        "title": "Earthquake Competition Event",
        "category": "Competition",
        "source": "CCE Activities & Events/The Earthquake Competition Event/FB_IMG_1781452418859.jpg",
        "image": "activities/earthquake-competition.webp",
        "alt": "Students and faculty during an earthquake engineering competition activity",
        "caption": "A student competition focused on structural response, teamwork, and engineering explanation.",
        "editablePlaceholder": False,
    },
    {
        "title": "Spaghetti Competition Celebration",
        "category": "Competition",
        "source": "CCE Activities & Events/Spaghetti Competition Celebration/FB_IMG_1781452625318.jpg",
        "image": "activities/spaghetti-structure-competition.webp",
        "alt": "Student team presenting a lightweight structural model",
        "caption": "A hands-on model-building activity that encourages structural thinking and iterative design.",
        "editablePlaceholder": False,
    },
    {
        "title": "Civil Engineering Day",
        "category": "Department Event",
        "source": "CCE Activities & Events/Civil Engineering Day/FB_IMG_1781451993743.jpg",
        "image": "activities/civil-engineering-day.webp",
        "alt": "Civil Engineering Day session with students and faculty",
        "caption": "A department event for sharing civil engineering knowledge, experiences, and student engagement.",
        "editablePlaceholder": False,
    },
    {
        "title": "Graduation Project Defense",
        "category": "Academic Showcase",
        "source": "CCE Activities & Events/Graduation Project Defense/FB_IMG_1781452901402.jpg",
        "image": "activities/graduation-project-defense.webp",
        "alt": "Student presenting a civil engineering graduation project",
        "caption": "A capstone presentation setting where students communicate design decisions and applied project outcomes.",
        "editablePlaceholder": False,
    },
    {
        "title": "STEM & High School Hands-on Activities",
        "category": "Workshop",
        "source": "CCE Activities & Events/STEM & high school - hands-on activities/FB_IMG_1781451782262.jpg",
        "image": "activities/hands-on-workshop.webp",
        "alt": "Students participating in a hands-on civil engineering workshop",
        "caption": "Workshop-style activities that introduce engineering measurement, observation, and experimentation.",
        "editablePlaceholder": False,
    },
    {
        "title": "CCE Bazaar",
        "category": "Student Activity",
        "source": "CCE Activities & Events/CCE Bazaar/FB_IMG_1781452200550.jpg",
        "image": "activities/cce-bazaar-models.webp",
        "alt": "Civil engineering model displays at a CCE activity",
        "caption": "A visual showcase of student work, models, and department activities.",
        "editablePlaceholder": False,
    },
]

PDF_LABS = [
    {
        "title": "Structural Testing Area",
        "page": 1,
        "imageIndex": 2,
        "image": "labs/structural-testing-area.webp",
        "alt": "Structural testing frame from the Civil Lab Complex PDF",
        "description": "A structural testing area for observing load response and frame behavior.",
        "studentsLearn": ["Load application", "Structural response observation", "Test setup awareness"],
        "practicalRelevance": "Supports understanding of how structural elements behave under controlled loading.",
    },
    {
        "title": "Lab Instruction Room",
        "page": 2,
        "imageIndex": 1,
        "image": "labs/lab-instruction-room.webp",
        "alt": "Instruction room shown in the Civil Lab Complex PDF",
        "description": "A teaching room connected to lab briefings, demonstrations, and technical instruction.",
        "studentsLearn": ["Lab preparation", "Technical briefing", "Engineering discussion"],
        "practicalRelevance": "Prepares students to connect lab procedures with engineering interpretation.",
    },
    {
        "title": "Surveying Laboratory",
        "page": 3,
        "imageIndex": 1,
        "image": "labs/surveying-laboratory.webp",
        "alt": "Surveying equipment in the Civil Lab Complex PDF",
        "description": "A surveying lab supporting measurement, field instruments, and spatial data collection.",
        "studentsLearn": ["Survey instrument handling", "Site measurement", "Spatial documentation"],
        "practicalRelevance": "Surveying is essential for setting out, mapping, and site-control work in civil projects.",
    },
    {
        "title": "Concrete & Materials Laboratory",
        "page": 4,
        "imageIndex": 1,
        "image": "labs/concrete-materials-laboratory.webp",
        "alt": "Concrete and materials laboratory shown in the Civil Lab Complex PDF",
        "description": "A materials lab for civil engineering material testing and quality-related demonstrations.",
        "studentsLearn": ["Material testing workflow", "Concrete and aggregate awareness", "Quality-control reasoning"],
        "practicalRelevance": "Materials testing supports safe construction, specification compliance, and durability decisions.",
    },
    {
        "title": "Soil Mechanics Laboratory",
        "page": 5,
        "imageIndex": 1,
        "image": "labs/soil-mechanics-laboratory.webp",
        "alt": "Soil mechanics laboratory equipment from the Civil Lab Complex PDF",
        "description": "A geotechnical lab for soil behavior, testing setups, and foundation-related learning.",
        "studentsLearn": ["Soil classification awareness", "Geotechnical testing concepts", "Foundation behavior links"],
        "practicalRelevance": "Soil mechanics supports foundation design, excavation work, and ground-condition evaluation.",
    },
    {
        "title": "Meteorology Laboratory",
        "page": 6,
        "imageIndex": 1,
        "image": "labs/meteorology-laboratory.webp",
        "alt": "Meteorology laboratory from the Civil Lab Complex PDF",
        "description": "A lab space for environmental and meteorological observation connected to infrastructure performance.",
        "studentsLearn": ["Environmental measurement awareness", "Climate data context", "Infrastructure exposure factors"],
        "practicalRelevance": "Weather and environmental conditions influence drainage, construction operations, and asset durability.",
    },
    {
        "title": "Hydraulics Laboratory",
        "page": 7,
        "imageIndex": 1,
        "image": "labs/hydraulics-laboratory.webp",
        "alt": "Hydraulics laboratory equipment from the Civil Lab Complex PDF",
        "description": "A hydraulics lab for water-flow demonstrations and fluid mechanics learning.",
        "studentsLearn": ["Flow behavior", "Hydraulic measurement", "Fluid mechanics interpretation"],
        "practicalRelevance": "Hydraulics supports drainage, water systems, channels, and infrastructure service design.",
    },
    {
        "title": "Transportation & Asphalt Laboratory",
        "page": 8,
        "imageIndex": 1,
        "image": "labs/transportation-asphalt-laboratory.webp",
        "alt": "Transportation and asphalt laboratory from the Civil Lab Complex PDF",
        "description": "A transportation and asphalt lab for pavement material and infrastructure testing concepts.",
        "studentsLearn": ["Pavement material awareness", "Testing equipment recognition", "Transport infrastructure quality concepts"],
        "practicalRelevance": "Supports highway, pavement, and transport-infrastructure engineering practice.",
    },
    {
        "title": "Environmental Laboratory",
        "page": 9,
        "imageIndex": 1,
        "image": "labs/environmental-laboratory.webp",
        "alt": "Environmental laboratory from the Civil Lab Complex PDF",
        "description": "An environmental lab for observing water/environmental testing setups relevant to civil infrastructure.",
        "studentsLearn": ["Environmental testing awareness", "Sample handling concepts", "Infrastructure and environmental links"],
        "practicalRelevance": "Environmental testing supports water quality, sustainability, and responsible infrastructure delivery.",
    },
]

PDF_GALLERY = [
    {
        "title": "Surveying Equipment Detail",
        "page": 3,
        "imageIndex": 2,
        "image": "labs/surveying-equipment-detail.webp",
        "alt": "Surveying instruments close-up from the Civil Lab Complex PDF",
    },
    {
        "title": "Materials Testing Detail",
        "page": 4,
        "imageIndex": 2,
        "image": "labs/materials-testing-detail.webp",
        "alt": "Materials testing detail from the Civil Lab Complex PDF",
    },
]


def save_web_image(source: Path, output: Path, max_width: int = 1500) -> tuple[int, int]:
    with Image.open(source) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        return save_image_object(image, output, max_width=max_width)


def save_image_object(image: Image.Image, output: Path, max_width: int = 1500) -> tuple[int, int]:
    if image.width > max_width:
        ratio = max_width / image.width
        image = image.resize((max_width, round(image.height * ratio)), Image.Resampling.LANCZOS)
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, "WEBP", quality=84, method=6)
    return image.size


def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def prepare_logo() -> dict:
    BRAND_DIR.mkdir(parents=True, exist_ok=True)
    output = BRAND_DIR / "cce-logo.svg"
    output.write_bytes(LOGO_PATH.read_bytes())
    return {"source": LOGO_PATH.name, "output": "assets/brand/cce-logo.svg", "note": "Source file has .png extension but contains SVG markup."}


def prepare_standard_images(items: list[dict], section: str) -> list[dict]:
    prepared = []
    for item in items:
        output = IMAGE_DIR / item["image"]
        width, height = save_web_image(ROOT / item["source"], output)
        record = {k: v for k, v in item.items() if k != "source"}
        record["image"] = f"assets/images/{item['image']}"
        record["sourceFile"] = item["source"]
        record["width"] = width
        record["height"] = height
        record["section"] = section
        prepared.append(record)
    return prepared


def extract_pdf_images() -> tuple[list[dict], list[dict], list[dict]]:
    reader = PdfReader(PDF_PATH)
    all_items = PDF_LABS + PDF_GALLERY
    extracted_map = {}
    for item in all_items:
        page = reader.pages[item["page"] - 1]
        pdf_image = list(page.images)[item["imageIndex"] - 1]
        with Image.open(__import__("io").BytesIO(pdf_image.data)) as image:
            width, height = save_image_object(ImageOps.exif_transpose(image).convert("RGB"), IMAGE_DIR / item["image"])
        extracted_map[(item["page"], item["imageIndex"])] = {
            "source": f"{PDF_PATH.name}, page {item['page']}, embedded image {item['imageIndex']}",
            "output": f"assets/images/{item['image']}",
            "width": width,
            "height": height,
        }

    labs = []
    for item in PDF_LABS:
        key = (item["page"], item["imageIndex"])
        meta = extracted_map[key]
        record = {k: v for k, v in item.items() if k not in {"page", "imageIndex"}}
        record["image"] = meta["output"]
        record["source"] = meta["source"]
        record["width"] = meta["width"]
        record["height"] = meta["height"]
        labs.append(record)

    gallery = []
    for item in PDF_GALLERY:
        key = (item["page"], item["imageIndex"])
        meta = extracted_map[key]
        gallery.append({
            "title": item["title"],
            "image": meta["output"],
            "alt": item["alt"],
            "source": meta["source"],
            "width": meta["width"],
            "height": meta["height"],
        })
    return labs, gallery, [*labs, *gallery]


def main() -> None:
    shutil.rmtree(PUBLIC_DIR, ignore_errors=True)
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    logo_record = prepare_logo()
    site_visits = prepare_standard_images(SITE_VISITS, "Site Visits")
    activities = prepare_standard_images(ACTIVITIES, "Activities & Events")
    labs, lab_gallery, lab_usage = extract_pdf_images()

    write_json(CONTENT_DIR / "site-visits.json", {"title": "Site Visits", "items": site_visits})
    write_json(CONTENT_DIR / "activities-events.json", {"title": "Activities & Events", "items": activities})
    write_json(CONTENT_DIR / "cce-labs.json", {
        "title": "CCE Labs",
        "sourcePdf": PDF_PATH.name,
        "overview": "The CCE labs support practical learning through testing, measurement, observation, and engineering interpretation across civil engineering disciplines.",
        "labs": labs,
        "gallery": lab_gallery,
    })

    usage = {
        "logo": logo_record,
        "siteVisits": site_visits,
        "activitiesEvents": activities,
        "cceLabs": lab_usage,
        "ignored": [
            "Repeated Image9.png logo/header objects inside Civil Lab Complex.pdf were ignored as non-lab photography.",
            "Videos in CCE Activities & Events/Videos were not used because the requested deliverable is a static image-led microsite.",
            "Unselected duplicate event and site-visit photos were ignored to avoid repetition and keep each section focused.",
        ],
    }
    write_json(CONTENT_DIR / "media-usage.json", usage)
    print(json.dumps({
        "logo": logo_record["output"],
        "siteVisitImages": len(site_visits),
        "activityImages": len(activities),
        "labImages": len(lab_usage),
    }, indent=2))


if __name__ == "__main__":
    main()
