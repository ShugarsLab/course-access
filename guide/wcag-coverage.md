# WCAG coverage

Under the 2024 ADA Title II rule, public colleges and universities must make web content, including course documents posted to a learning management system, meet WCAG 2.1 Level A and AA. The compliance date for large public entities is April 26, 2027.

We treat WCAG as the floor, not the goal. For students who use screen readers, the pipeline goes well beyond it: WCAG requires a text alternative for every figure, but not one that teaches, and the guide's conventions are built around what a listening student needs in order to learn. This page is the other side of that: the WCAG success criteria that matter for course materials, and how far the pipeline covers each, so the gaps are visible and can be filled.

This is a working list, not legal advice. Instructors should check their institution's own guidance. Built-in checkers (PowerPoint's and Word's Check Accessibility, Acrobat's accessibility check) are a useful first pass for several rows below, though they check presence more than quality.

**Status:** *Covered* = a stage of the pipeline handles it. *Being added* = now part of the pipeline, still being tried out. *Partly* = handled for some materials or by convention without a check. *Not yet* = not addressed.

| Area | WCAG 2.1 success criteria | What it means for course materials | Status |
|---|---|---|---|
| Text alternatives | 1.1.1 Non-text content (A) | Every image, chart, and figure has a description or is marked decorative; equations are read | Covered: the core of the pipeline |
| Audio and video | 1.2.1, 1.2.2, 1.2.3 (A); 1.2.4, 1.2.5 (AA) | Captions for recorded and live video; transcripts for audio; audio description, or a text alternative, for what is only shown | Not yet: lecture recordings and videos embedded in slides or course pages |
| Structure | 1.3.1 Info and relationships (A) | Real headings, lists, and tables with header rows; tagged PDFs | Covered for slides, PDFs, and the Word companion; Partly for R Markdown |
| Reading order | 1.3.2 Meaningful sequence (A) | Slide objects and PDF tags in the order the content should be read | Covered (stage 4) |
| Instructions that rely on sight | 1.3.3 Sensory characteristics (A) | No instructions that work only by shape, color, or position: the red line, the box on the right | Being added: a stage 2 check while proofreading |
| Color as the only signal | 1.4.1 Use of color (A) | Chart series, highlights, and status not told apart by color alone | Being added: descriptions carry in words what color encodes; stage 2 now flags slides where color alone tells things apart |
| Text contrast | 1.4.3 Contrast, minimum (AA) | Text at least 4.5:1 against its background (3:1 for large text), including text on images | Being added: theme check before starting; stage 2 measures text against the rendered slide |
| Graphics contrast | 1.4.11 Non-text contrast (AA) | Chart lines, markers, and other graphics needed to understand content at least 3:1 against adjacent colors | Not yet: a check on rendered figures, with color-vision simulation, is planned; a colorblind-safe default palette in R prevents most problems |
| Resize and reflow | 1.4.4 Resize text, 1.4.10 Reflow (AA) | Content readable when enlarged; for documents, mostly a matter of format | Partly: the Word companion and HTML reflow; a slide PDF does not |
| Images of text | 1.4.5 Images of text (AA) | Screenshots of text and code become real text | Covered (stage 2) |
| Text spacing, hover content | 1.4.12, 1.4.13 (AA) | Mostly web pages, such as knitted HTML worksheets | Not yet checked |
| Keyboard | 2.1.1, 2.1.2 (A) | Interactive content (HTML worksheets, embedded widgets, explorable plots) works without a mouse | Partly: maidr's explorable plots tried by ear from the R console; not yet in posted HTML, since in knitted documents maidr removed alt text and captions |
| Timing and motion | 2.2.1, 2.2.2 (A); 2.3.1 (A) | No auto-advancing content without control; animated GIFs and moving content can be paused; nothing flashes more than three times a second | Being added for slides: stage 2 flags animated GIFs. Video not yet |
| Titles | 2.4.2 Page titled (A) | Every file has a document title, not a file name, as its title | Covered at ship for slides and PDFs; being added for the Word companion and knitted HTML |
| Link text | 2.4.4 Link purpose (A) | Link text says where it goes; no bare URLs or click here | Being added: a stage 2 check |
| Headings | 2.4.6 Headings and labels (AA) | Headings describe their sections | Partly: slide titles become headings in the Word companion |
| Language | 3.1.1 Language of page (A); 3.1.2 Language of parts (AA) | Each file's language is set; passages in another language are marked | 3.1.1 Covered at ship for the PDF, being added for the Word companion and knitted HTML; 3.1.2 Not yet (for example, non-English names or quotations in readings) |
| Forms | 3.3.1, 3.3.2 (A); 4.1.2 (A) | Fillable PDFs and Word forms, such as assignment templates, have labeled fields | Not yet |

## Outside the scope of documents

Some obligations sit with the institution or with other tools rather than with an instructor's files: course pages in the learning management system, publisher platforms and other third-party content, quizzes and their timing, and individual accommodations for a student, which remain a separate obligation.

## Where the new checks sit in the pipeline

- **Before you start, once per course:** the theme's colors, for text contrast. Fixed in the theme (and the source file, for decks authored elsewhere), so the fix is made once.
- **Stage 2 (Plan), alongside proofreading:** text contrast measured on the rendered slides, color-only meaning, wording that only works by sight, link text, animated GIFs. Each is a plan item the instructor can skip.
- **Ship:** PowerPoint's Check Accessibility as a baseline before export; document title and language on every output, the Word companion and knitted HTML included.
- **R Markdown:** a colorblind-safe default palette in the worksheet setup.

## Next steps

Planned additions are listed in the [roadmap](../ROADMAP.md).
