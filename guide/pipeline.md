# The remediation pipeline

The pipeline is an ordered, instructor-led process for making course materials accessible. We currently have pipelines for three kinds of material: lecture slides, readings, and R Markdown worksheets. All three share one set of conventions for describing [figures](describing-figures.md) and [equations](equations.md), and draw from a [house style](house-style-template.md).

Each kind of material at a glance: [slides](#slides-at-a-glance), [readings](#readings-at-a-glance), and [R Markdown worksheets](#r-markdown-worksheets-at-a-glance).

## Why the order matters

Each stage changes something the next one depends on. Grouping the pieces of a figure, or splitting a build into separate slides, changes which objects exist and in what order. So anything that depends on order (descriptions written one build at a time, reading order, decorative flags) comes after the structure has settled. We learned this the expensive way: checking reading order before grouping meant checking it twice, and descriptions written before deciding what an object was (a figure, a decoration, a picture of text) were often thrown away.

So the work has an order: structure, then the plan, then descriptions, then reading order last, since any change to structure undoes it. These stages can also break a slide's animations, so keep the original deck for teaching and remediate a copy for posting.

## What every posted file needs

Whatever the material, each posted file should have:

- a **document title** (screen readers announce it instead of the file name) and a **language**;
- **headings** a listener can move between;
- **real tables** with header rows marked;
- **alt text** on every figure that carries information, and the decorative flag on everything that doesn't;
- a **reading order** that follows the argument.

Every file we post is made accessible, and each is designed for different readers. The PDF of the slides is tagged and described for everyone; the [Word companion](word-companion.md), with live equations and minimal repeated content, is built for listening. Students choose the format that works for them.

## Slides at a glance

*Full chapter: [Slides](slides.md).* A deck is remediated in a copy of its .pptx, where PowerPoint's accessibility features are, and the original stays as it is for teaching. Structure comes first, because every later stage depends on which objects exist. We post two files per deck: a tagged PDF of the slides and a text-only [Word companion](word-companion.md) built for listening. Decks made in Keynote, Google Slides, or Beamer are covered in [Keynote and Google Slides](keynote-google-slides.md) and [Beamer](beamer.md) (both in progress).

| Step | What happens | Why here |
|---|---|---|
| [Before you start](slides.md#before-you-start) | Put the Accessibility tab on the ribbon; keep an untouched copy; decide what happens to speaker notes; carry over slides already remediated in an earlier deck; work from the slides as students see them; check the theme's colors; have a house style | Every later step works from what students actually see, and nothing settled before is redone |
| [1. Structure](slides.md#1-structure) | Group the pieces of each drawn figure; ungroup callout boxes so their text is read as text; split builds whose later steps cover earlier content | Changes which objects exist, so everything else depends on it |
| [2. Plan](slides.md#2-plan) | Proofread; turn pictures of text and code into real text; rebuild pictures of tables as real tables with header rows; empty table cells hidden under shapes; check text contrast, meaning carried by color alone, link text, and wording that only works by sight; decide which figures need a description and which repeats are decorative | Settles what each object is before anyone writes a word about it |
| [3. Draft and review](slides.md#3-draft-and-review) | Write figure descriptions from the slides as students see them, one build at a time, in the course's house style; review every description in place | Descriptions of a build depend on each other, so they are written as a sequence |
| [4. Reading order and decorative](slides.md#4-reading-order-and-decorative) | Put the title first, then the rest in the order the lecture follows; mark repeated content decorative | Any structural change undoes reading order, so it goes last |
| [Ship](slides.md#ship) | Set the document title; export a tagged PDF and check it; build the [Word companion](word-companion.md); check each as students will receive it | Problems that only show in the posted files are caught before students see them |

## Readings at a glance

*Full chapter: [Readings](readings.md).* A publisher's PDF is someone else's document. The goal is access, not improvement, so every change is the smallest one that gets there: add what is missing, and keep what the publisher built.

| Step | What happens | Why here |
|---|---|---|
| [Before you start](readings.md#before-you-start) | Check with your library about posting a copy; save the file as downloaded, since every later step writes a new copy | Every change can be checked against the original, or undone |
| [Audit](readings.md#1-audit-the-existing-tags) | List the publisher's tags (headings, tables with header cells, figures, language), with `pdf_audit.py` or in Acrobat; run Acrobat's Autotag **only** if the file has no usable tags | Decides how little needs changing: on a well-tagged paper, Autotag made the structure worse |
| [Draft](readings.md#3-draft-descriptions-for-approval) | Read each figure at full resolution, with the paper's own discussion of it; describe what the prose leaves out (layout, values, panels the text skips); the instructor approves every description | The paper already discusses its figures, so a description adds only what the text doesn't |
| [Write](readings.md#4-write-the-descriptions-and-the-language) | Add the alt text and the language code, and nothing else; check that pages and text are otherwise unchanged (script planned) | The smallest change that gives access |
| [Finish](readings.md#5-mark-logos-and-icons-decorative) | Spot-check the alt text in Acrobat; mark logos and icons as artifacts (decorative) | Marking something decorative edits the page content, which is safest done in Acrobat |

**Evidence:** our practice, on only a few articles so far; treat the steps as provisional.

## R Markdown worksheets at a glance

*Full chapter: [R Markdown worksheets](rmarkdown.md).* A worksheet can be knitted again every semester, so fixes belong in the source wherever possible. We post every worksheet in three formats: the .Rmd file, the knitted HTML, and a PDF.

| Step | What happens | Why here |
|---|---|---|
| [Describe](rmarkdown.md#1-describe-figures-in-the-source) | Read each plot from the knitted HTML and write a fixed-text description into the chunk's `fig.alt` option, so students see no extra code | A fix in the source survives every re-knit |
| [Repair](rmarkdown.md#2-repair-the-source) | Fix heading levels, math that won't render in HTML, broken links, wording that assumes one format, and typos | HTML output, and screen readers, depend on structure that a PDF hides |
| [Verify](rmarkdown.md#3-check-the-knitted-html) | Re-knit, then check the HTML: every plot has its description, headings nest, math renders | Nothing is finished until it is checked on the re-knitted file |
| [PDF](rmarkdown.md#4-remediate-the-knitted-pdf) | Run Acrobat's Autotag on the knitted PDF, then correct it in passes: figure descriptions and equation readings, misfiled equations and false headings, reading-order breaks, and inline symbols a screen reader would misread (scripts planned) | A knitted PDF has no tags at all, and every knit starts over |

A knitted LaTeX PDF carries no tags at all, so it needs a tagging step before it can be remediated. **That step uses Acrobat's Autotag, which requires Adobe Acrobat Pro**, a commercial product. Equations in a knitted PDF still need written readings: Autotag tags them as figures with nothing to say. Quarto and LaTeX's own tagging may remove the Autotag step in future; we have not tried them. **Evidence:** our practice; the PDF passes have not yet been heard with a screen reader.

## What the pipeline does not yet cover

The pipeline's depth is screen-reader access. The other WCAG 2.1 AA requirements that apply to course materials, and how far the pipeline covers each, are tracked in [WCAG coverage](wcag-coverage.md).
