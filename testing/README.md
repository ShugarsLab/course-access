# Test results

What we found when we tested our materials, in one place: the evidence the guide's rules cite. The guide's chapters state the rules that follow from these results and link here, rather than repeating them.

Two kinds of result are recorded:

- **Heard with a screen reader:** a person listened to a file with a screen reader and noted what came through.
- **Found by inspecting the file:** the file's structure (PDF tags, HTML, the .pptx) was checked directly, without listening. Correct structure is necessary for a good listening experience, but it is not proof of one.

Each result gives the screen reader, the program, and the month, with versions where we recorded them, because results change with versions. Results added from now on should record versions. Each set of results lists the rules it supports.

Results from other setups are welcome, especially from screen-reader users and from screen readers and programs we haven't tested: see [Contributing](../CONTRIBUTING.md#share-test-kit-results). New results are added under their setup, or as a new setup, with the same details.

This folder holds this page and the [test kits](kits/README.md), ready-made files for some of these checks that anyone can run with a screen reader. More will be added here as our testing grows. Tests of the AI prompts are logged with the prompts, in the [prompt test log](../ai-assistant/prompt-test-log.md).

## At a glance

| Setup | Main result | Rules it supports |
|---|---|---|
| [NVDA with PowerPoint](#nvda-with-powerpoint) | Alt text on groups, shapes, and equations is not read; equations are not read as math | [P2](../guide/principles.md#p2), [E1](../guide/equations.md#e1), [F24](../guide/describing-figures.md#f24) |
| [NVDA with Word](#nvda-with-word) | Live equations are read and can be explored | [E1](../guide/equations.md#e1), [The Word companion](../guide/word-companion.md) |
| [VoiceOver with Preview, on a PowerPoint PDF](#voiceover-with-preview-on-a-pdf-exported-from-powerpoint) | Alt text is read; an equation with alt text is heard up to four times | [E2](../guide/equations.md#e2), [E3](../guide/equations.md#e3) |
| [VoiceOver with Safari, knitted HTML](#voiceover-with-safari-on-knitted-html) | Display equations read well; inline math breaks up the sentence | [R Markdown worksheets](../guide/rmarkdown.md#3-check-the-knitted-html) |
| [VoiceOver with RStudio](#voiceover-with-rstudio) | Line-by-line reading works through long files; continuous reading doesn't | [Working in R with a screen reader](../students/working-in-r-with-a-screen-reader.md#reading-long-files) |
| [maidr from the R console](#maidr-from-the-r-console) | An explorable plot can be moved through by keyboard and heard | [Working in R with a screen reader](../students/working-in-r-with-a-screen-reader.md#explore-a-plot-by-sound-maidr) |
| [Inspections of files](#found-by-inspecting-files) | Keynote's PDF export, Autotag, maidr in knitted documents, and others | Linked below |

---

## Heard with a screen reader

### NVDA with PowerPoint

*October 2026. NVDA on Windows, reading .pptx decks in PowerPoint; NVDA and PowerPoint versions not recorded.*

- **Alt text on a group is not read.** NVDA reads the objects inside the group one by one instead, so a figure built from shapes is heard as a list of fragments.
- **Alt text on arrows and other shapes is not read.** Narration written on an arrow reaches a listener only through the Word companion.
- **Equations:** NVDA read neither PowerPoint's own equations nor alt text written on them. NVDA's documented math support covers native equations in Word and equations made with MathType, not PowerPoint's own equations.
- **Alt text on pictures is read.**
- **Inline Greek letters** typed as ordinary text (μ, σ, α inside a sentence) are read correctly.
- **A superscript 2** is not read as "squared."
- **Punctuation is voiced:** parentheses, quote marks, and colons.
- **Object names** from the Selection Pane ("Line", "Group 10") are read aloud.
- **Repeated slide titles marked decorative:** NVDA still announced the slide number. This rests on a single test.

Supports: [P2](../guide/principles.md#p2); [Where descriptions are read](../guide/describing-figures.md#where-descriptions-are-read); [F10](../guide/describing-figures.md#f10); [E1](../guide/equations.md#e1), [E7](../guide/equations.md#e7), [E17](../guide/equations.md#e17); the house style's quote marks and Greek letters ([worked example](../guide/house-style-example.md#punctuation-and-symbols)); naming objects in a shared .pptx ([Slides: Ship](../guide/slides.md#ship)).

### NVDA with Word

*October 2026. NVDA on Windows with the MathCAT add-on, reading Word documents; versions not recorded.*

- **Native Word equations are read, and can be explored** piece by piece (term, numerator, subscript) instead of being heard once at speed.
- **Word announces the start of every equation,** even one holding a single symbol, which helps for a full equation and gets in the way for one letter.
- **An empty paragraph is announced as "blank."**

Supports: [E1](../guide/equations.md#e1), [E19](../guide/equations.md#e19); [The Word companion](../guide/word-companion.md).

### VoiceOver with Preview, on a PDF exported from PowerPoint

*October 2026. VoiceOver on macOS Tahoe 26.6.2, reading a tagged PDF exported from PowerPoint, in Preview.*

- **Alt text on figures is read.**
- **Every equation is read with PowerPoint's own spoken reading,** whether or not alt text was written. An equation that also had alt text was heard up to four times: the alt text, then PowerPoint's reading, then both again from a second tag. An equation without alt text was read once.
- **Equations inside a described figure** are read after the figure's description.
- **PowerPoint's readings have defects:** a function name spelled out letter by letter ("l o g sub e"), stray punctuation ("a. times b"), and "start equation mu" for a lone symbol in a sentence.

How NVDA and JAWS read the same PDF is untested.

Supports: [E2](../guide/equations.md#e2), [E3](../guide/equations.md#e3), [E14](../guide/equations.md#e14); [In the PDF](../guide/equations.md#in-the-pdf-read-once-unless-alt-text-is-added).

### VoiceOver with Safari, on knitted HTML

*October 2026. VoiceOver on macOS Tahoe 26.6.2, reading an R Markdown worksheet knitted to HTML (equations shown with MathJax), in Safari.*

- **Display equations** were read well as a whole and could be explored piece by piece.
- **Inline math** in a sentence was read as a separate item, breaking up the sentence; some italics did the same.
- **Every equation is a Tab stop,** MathJax's default.

NVDA has not been tested with the knitted HTML.

Supports: [R Markdown worksheets, stage 3](../guide/rmarkdown.md#3-check-the-knitted-html).

### VoiceOver with RStudio

*October 2026. VoiceOver on macOS Tahoe 26.6.2, RStudio 2026.09.0+174, with the files in the [long-file test kit](kits/rstudio-long-files/README.md).*

- **Moving line by line** with the Down arrow read every line of two 400-line files to the end, with short lines and with long ones.
- **Reading continuously** in the Source editor read the current line and then left the editor; in the Visual editor it stopped after about 30 lines, and started from the top whatever the cursor's position.

A screen reader on Windows has been observed to stop after about 200 lines when reading continuously; that has not yet been tested systematically.

Supports: [Working in R with a screen reader](../students/working-in-r-with-a-screen-reader.md#reading-long-files).

### maidr from the R console

*October 2026. maidr 0.4.0, R 4.6.0.*

- A plot opened with maidr's `show()` from the console could be explored by keyboard and heard.

What maidr does to knitted documents is under [inspections](#found-by-inspecting-files), below.

Supports: [Working in R with a screen reader](../students/working-in-r-with-a-screen-reader.md#explore-a-plot-by-sound-maidr).

---

## Found by inspecting files

Checked in the files themselves, not by ear.

| What | Result | Where it matters |
|---|---|---|
| Alt text in decks exported from Keynote (October 2026) | The alt-text field arrives filled with the picture's file name or the word *Image*. One deck reported alt text on 112 of 112 images and had no real descriptions. | [`alt_audit.py`](../tools/README.md#alt-text-audit); [Describing figures](../guide/describing-figures.md#why-figures-in-teaching-are-a-different-problem) |
| Keynote's own PDF export (October 2026) | No document language, every bullet tagged as a top-level heading, fewer than half the figures with alt text, and table headers lost. | [Slides](../guide/slides.md) (export the PDF from PowerPoint) |
| Header rows in a PDF exported from PowerPoint (October 2026) | Header flags set in PowerPoint became header cells in the PDF's tags. | [F15](../guide/describing-figures.md#f15) |
| Acrobat's Autotag on a publisher's well-tagged article (October 2026) | Made the structure worse: sections and subsections dropped two heading levels, the author's name became a heading, and the title was tagged twice. | [Readings](../guide/readings.md#1-audit-the-existing-tags); [E5](../guide/equations.md#e5) |
| Acrobat's automatic equation readings (October 2026) | A long fraction was read as "numerator, 1 plus 1 plus … 14 end numerator", losing the denominator and the result; "start equation element of" for x ∈ S; "equals 1 sixth" for = 1/6 (correct). | [E5](../guide/equations.md#e5) |
| Autotag on knitted R Markdown PDFs (October 2026) | Plots, display equations, and lines of code all tagged as figures (27 on one worksheet: 6 plots, 10 equations, 11 lines of code or output); run-in headings and code read out of order; `\neq` and `\mu` come through as characters likely read as "equals" and "micro". | [R Markdown worksheets, stage 4](../guide/rmarkdown.md#4-remediate-the-knitted-pdf) |
| Printing knitted HTML to PDF from Chromium (October 2026) | Chrome's own Save as PDF produced a tagged file: alt text on figures, headings, title, and code as text. The macOS print dialog does not tag. Math not checked. | [R Markdown worksheets, alternatives](../guide/rmarkdown.md#alternatives-we-tried-or-considered) |
| `maidr::maidr_on()` in knitted documents (R 4.6.0, maidr 0.4.0, rmarkdown 2.31, and knitr 1.51; October 2026) | ggplot2 plots in the HTML became maidr plots, but their `fig.alt` text and captions were dropped; ggplot2 plots disappeared from the knitted PDF; base R plots were unchanged; maidr's code loads from the web, unpinned, each time the page opens. | [R Markdown worksheets, alternatives](../guide/rmarkdown.md#alternatives-we-tried-or-considered) |

## Not yet tested

- JAWS and Narrator, with any of our materials.
- NVDA with the PDF exported from PowerPoint, and with knitted HTML.
- Any remediated knitted R Markdown PDF, or any remediated reading, by ear.
- Whether a screen reader honors the decorative flag on a PowerPoint table.
- Whether alt text survives a Google Slides download to .pptx.
