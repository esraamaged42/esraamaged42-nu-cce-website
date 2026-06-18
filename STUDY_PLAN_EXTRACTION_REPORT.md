# Study Plan Extraction Report

## Excel File Used

Source workbook:

- `2023 Bylaws_3_3_2025_CVL.xlsx`

Generated content file:

- `src/content/study-plan.json`

## Sheets Read

The workbook contains these sheets:

- `Major-1 (NARS)`
- `Major-1 (Competencies)`
- `CCE Major-1 (8 S)`
- `CCE Major-1 (7 S)`
- `CE Minor`
- `List of Courses`
- `Major-2 (NARS)`
- `Major-2 (Competencies)`
- `CCE Major-2 (8 S)`
- `CCE Major-2 (7 S) (new)`
- `Statistics`

Published study-plan sheets:

- `CCE Major-1 (8 S)`
- `CCE Major-2 (8 S)`

The 7-semester sheets were inspected but not published because the user requested a clear study plan and both 8-semester plans validate directly to 144 credit hours.

## Semester Detection

The published sheets use four year blocks with two semesters each:

- `Fall Y1`
- `Spring Y1`
- `Fall Y2`
- `Spring Y2`
- `Fall Y3`
- `Spring Y3`
- `Fall Y4`
- `Spring Y4`

The extractor reads:

- left semester block: course code `B`, course title `C`, credits `D`, prerequisite `K`
- right semester block: course code `S`, course title `T`, credits `U`, prerequisite `AB`

The website normalizes these into:

- Semester 1
- Semester 2
- Semester 3
- Semester 4
- Semester 5
- Semester 6
- Semester 7
- Semester 8

The original fall/spring labels remain in the JSON as `term`.

## Track Handling

Workbook evidence:

- `CCE Major-1 (8 S)` header: `Major-1 "Construction Engineering & Management" CEM [8-Semesters Study Plan]`
- `CCE Major-2 (8 S)` header: `Major-2 "Smart Structural Engineering" SSE [8-Semesters Study Plan]`

Website mapping:

- `Major-1 / CEM` -> Project Management Track
- `Major-2 / SSE` -> Smart Structures Track

Both tracks are displayed inside the single Study Plan page using tabs.

## Credit-Hour Assignment

Rules applied:

- `EGL111 English I`: 0 credit hours
- `EGL112 English II`: 0 credit hours
- `EGL213 Writing Skills`: 3 credit hours
- `EGL214 Communication and Presentation Skills`: 3 credit hours
- `CVL391 Practical Training-1`: 0 credit hours
- `CVL392 Practical Training-2`: 0 credit hours
- remaining courses use the workbook value; the remaining plan courses are 3 credit hours

The user prompt says "Writing Skills and Presentation is 3 credit hours." The workbook contains two separate courses:

- `EGL213 Writing Skills`: 3 credit hours
- `EGL214 Communication and Presentation Skills`: 3 credit hours

The website preserves the workbook structure and documents this wording difference.

## Validation

Smart Structures Track:

- Source sheet: `CCE Major-2 (8 S)`
- Number of semesters: 8
- Total credit hours: 144
- Zero-credit requirements: 4
- Result: equals 144

Project Management Track:

- Source sheet: `CCE Major-1 (8 S)`
- Number of semesters: 8
- Total credit hours: 144
- Zero-credit requirements: 4
- Result: equals 144

## Assumptions and Conflicts

- Official course descriptions were not available in the workbook. The course detail panels use concise generic descriptions based on course titles and civil engineering context.
- Course type is inferred from workbook flags and course names.
- The 7-semester sheets require human confirmation before publication.
- No numeric credit-hour conflict prevented validation to 144 credit hours.
