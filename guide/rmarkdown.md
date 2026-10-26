# R Markdown worksheets

This chapter walks through the [pipeline](pipeline.md) for documents knitted from R Markdown: worksheets, problem sets, solutions, and examples. Unlike a slide deck, an R Markdown document can be knitted again every semester, so fixes belong in the source wherever possible. The knitted PDF is the exception: knitting regenerates it without tags, so it is remediated after every knit.

We post every R Markdown document in three formats, and each reaches a listener differently:

| Format | Figure descriptions | Equations | Structure |
|---|---|---|---|
| The .Rmd file | Shown as text in each chunk's header (`fig.alt`) | LaTeX source | Markdown headings, read as text |
| Knitted HTML | Real alt text on every plot, from `fig.alt` | MathJax, which screen readers can read | Real headings, if the source's levels are right |
| Knitted PDF | None until remediated | Untagged until remediated | None until remediated: pdfTeX writes no tags |

**Evidence:** our practice; the HTML and PDF behavior found by inspecting files (knitted HTML and PDFs).

Which of these to post, and what the .Rmd's default output is, are the instructor's choices. Ours defaults to `output: pdf_document`, because that suits most of our students; a student who knits it gets a PDF without alt text, while the descriptions stay in the chunk headers, the posted HTML, and the remediated PDF.

The stages below follow one order: describe and repair in the source, check the HTML, then remediate the PDF. Everything in stages 1 to 3 can be done in RStudio. Stage 4 needs Adobe Acrobat Pro. The scripts we use for stage 4 are not yet in [tools](../tools/README.md); until they are, it is described here as done by hand. Rules from [Describing figures](describing-figures.md) and [Equations](equations.md) apply throughout and are cited by ID.

**Status:** draft. Nothing in the knitted PDFs has yet been heard with a screen reader.

---

## Before you start

- **Keep a copy of the .Rmd before any edits,** and later the PDF exactly as Acrobat's Autotag left it, so every change can be checked against it.
- **Have a house style.** The worksheet's prose is student-facing text like any other, so the [house style](house-style-template.md) applies to it as well as to descriptions.
- **Knit to HTML** and work from that: it shows each figure as students will see it.

---

## 1. Describe figures in the source

**What and why.** The chunk option `fig.alt` gives a plot alt text in the knitted HTML. Written once in the source, it survives every re-knit, and the same approved text is reused when the PDF is remediated.

**Describe from the knitted HTML, not from the code.** The code says what was asked for; the figure shows what came out, including values. Check any value quoted in a description against the printed output. ([F11](describing-figures.md#f11) makes the same point for slides.)

**Write fixed text.** `fig.alt` can be computed from the data, but then every student reads extra code that has nothing to do with the lesson. We write descriptions as plain text, so students new to R see only the code the lesson is about.

````
```{r score-hours, fig.alt="Scatterplot of exam score against hours studied, for 120 students. Scores rise with hours, steeply up to about 10 hours and then more slowly; the points spread more widely at higher hours."}
plot(df$hours, df$score)
```
````

- **Double quotes delimit the string,** so the description itself uses none. The house style applies as in any description: symbols spelled out ([F22](describing-figures.md#f22)), the course's preferred terms.
- **One plot, one description.** Where a chunk draws two plots, split it into two chunks, each with its own `fig.alt`.
- **Depth follows how new the figure is** ([F1](describing-figures.md#f1)). A plot students have already met, in an earlier worksheet or in lecture, needs no explanation of how to read it.
- **Offer the numbers too,** where the values in a plot matter: a `knitr::kable()` table of the plotted data, with column names and a caption, can be read cell by cell in both HTML and PDF.

**With an AI assistant.** The assistant reads each plot from the knitted HTML, drafts the `fig.alt` text, and checks quoted values against the printed output. The instructor approves every description before it goes into the source.

**Evidence:** our practice.

---

## 2. Repair the source

**What and why.** HTML output, and screen readers, depend on things that a PDF tolerates or hides. These are the problems we found in our own worksheets:

- **Heading levels.** The document's title is the top-level heading, so sections start at `##`, not `#`. Lines starting with `#` inside R chunks are R comments, not headings; leave them alone.
- **Headings followed directly by a chunk.** In a knitted PDF, a `####` heading is a run-in heading: where a code chunk follows it directly, LaTeX holds the heading back and prints it *after* the chunk and its output. A `####` heading must be followed by prose; otherwise use `###`.
- **A blank line before every list.** Without one, a list is knitted as a single run-on line with literal asterisks, in both HTML and PDF.
- **Math that won't render in HTML.** LaTeX commands MathJax doesn't support (`\url{}`: write a Markdown link instead), unclosed `$…$`, and text symbols written as math.
- **Links.** Check every `[text](url)` for stray brackets, and give links text that says where they go.
- **Wording that assumes one format,** such as "this PDF" in a document that is also posted as HTML ("the knitted document").
- **Package messages and warnings** that bury the output a lesson is about: `message = FALSE` in the setup chunk, `warning = FALSE` on the chunk that loads packages.
- **A title and a language.** Set `title:` in the YAML header, and `lang: en` (or the document's language), which R Markdown leaves out of the HTML unless it is set.
- **Typos and house style** in the prose.

**With an AI assistant.** The assistant lists each fix; the instructor accepts or skips each one and makes the content decisions (what a hypothesis should say, what to cut).

**Evidence:** our practice; the run-in heading and list problems found by inspecting files (our own knitted PDFs). The `lang` setting is our analysis: we have not yet checked our own HTML for it.

---

## 3. Check the knitted HTML

After the instructor re-knits, open the HTML and check:

- every plot has the intended alt text (in the browser's inspector, or by viewing the page source and finding each `<img>`'s `alt`);
- headings nest: the title, then the sections, with no levels skipped;
- the math renders, with no stray `$` signs;
- package messages are gone.

The worksheet is not finished until this check is done on the re-knitted file.

**Equations in the HTML.** MathJax, which shows the equations, adds hidden math markup that screen readers can use. With VoiceOver in Safari, display equations were read well and could be explored piece by piece, but inline math in a sentence was read as a separate item, breaking up the sentence, and every equation was a Tab stop. NVDA has not been tested ([Test results](../testing/README.md#voiceover-with-safari-on-knitted-html)).

**Evidence:** our practice; equations found in testing ([VoiceOver with Safari](../testing/README.md#voiceover-with-safari-on-knitted-html), October 2026).

---

## 4. Remediate the knitted PDF

**What and why.** pdfTeX, which knits R Markdown to PDF, writes no tags: no headings, no reading order, no alt text. A screen reader gets the page's text as one undifferentiated stream, and every plot and display equation is silent. A first set of tags has to come from somewhere, and for us that is Acrobat Pro's Autotag. Autotag guesses structure from the page's layout, and on knitted worksheets it guesses wrong in consistent ways, so its tags are corrected in four passes.

Because every knit produces a new untagged PDF, keep the approved figure descriptions and equation readings in one place (a text file beside the .Rmd), ready to paste in again after the next knit.

Acrobat Pro's menu and panel names change between versions, so the steps below name the tools (Autotag, the tags panel, the reading-order tool) rather than menu paths.

### 4a. Autotag once, on the fresh knit

Run Acrobat's Autotag (the accessibility tools' automatic tagging) on the knitted PDF, and keep a copy of the result. Never Autotag a file that has already been corrected: it discards the corrections ([E5](equations.md#e5) gives the same rule for slides).

### 4b. Sort what Autotag called a figure

Autotag tags anything that doesn't look like ordinary text as a figure. On one of our worksheets it found 27 figures: 6 plots, 10 display equations, and 11 lines of code or output.

| Autotag's tag | What it is | Fix |
|---|---|---|
| Figure | A plot | Keep as a figure; add the approved `fig.alt` text as its alternate text |
| Figure | A display equation | Retag as a formula, with a written reading ([E6](equations.md#e6) to [E13](equations.md#e13)) |
| Text | A display equation | Retag as a formula, with a written reading |
| Figure | A line of code or console output | Retag as a paragraph, so it is read as text |
| Aside, Table, or List | A code chunk or its output (with `##` read as table cells) | Retag as paragraphs and spans, read as text, as in the HTML |
| Heading | The subtitle or date | Retag as a paragraph |
| Nothing | Page numbers | Mark as artifacts |

The plot descriptions are the ones already approved for `fig.alt`: the PDF's plots come from the same code, so they need no new review beyond checking that the PDF shows the same figures in the same order. Equation readings are new work, because the HTML needs none. Without one, a display equation's text comes out as a jumble of symbols; one chi-squared sum read as "χ 2= K X i=1 z 2i".

**Evidence:** found by inspecting files (the tags of our knitted PDFs after Autotag).

### 4c. Fix headings and reading order

- **Headings:** match the PDF's heading tags to the .Rmd's headings, level for level. Autotag sometimes runs a run-in heading together with the text after it; split them.
- **Reading order:** look for text read out of visual order. On our worksheets, lines of code with aligned columns were read column by column, a code line could be split across two blocks, and the first words of a sentence were read after the rest of it. Acrobat's reading-order tool can merge and reorder these blocks.

**Evidence:** found by inspecting files (the tags of our knitted PDFs).

### 4d. Fix inline symbols a screen reader would misread

Autotag leaves math inside sentences as text, and some of pdfTeX's characters read wrongly:

| In the .Rmd | In the PDF's text | Likely heard as | Should be |
|---|---|---|---|
| `\neq` | A slash drawn over "=" | "equals" | "not equal to" |
| `\mu` | The micro sign | "micro" | "mu" |

Not every symbol is a problem: `\ll` came through as the much-less-than character, which is likely read correctly ("much less than").

The not-equal problem matters most: an alternative hypothesis sounds like its null. We fix these in the PDF by giving each symbol its own replacement text (a span with `ActualText`), which leaves the page looking the same. This is impractical by hand in Acrobat and is done by one of the planned scripts. Two source-level fixes may remove the need, though we have not tried them: LaTeX's `accsupp` package can attach replacement text to `\neq` in the source, and the newer LaTeX tagging route (below) handles math differently.

Students who use screen readers can also work from the HTML, where MathJax stores these symbols correctly; past worksheets with the problem are a lower priority than new ones.

**Evidence:** the characters found by inspecting files (our knitted PDFs); "micro" from published documentation (NVDA's symbol list). Not yet heard with a screen reader, before or after the fix.

### 4e. Check before posting

- every page looks exactly as it did after Autotag;
- every figure and formula has its approved text, read back from the file;
- the headings match the .Rmd;
- the document has a title and a language;
- nothing is read out of order;
- Acrobat's accessibility checker runs clean, apart from fonts reported as not embedded (the R plots' labels), which don't affect reading.

`tools/pdf_audit.py` lists a PDF's tags, figures with their alt text, and headings in order, for the checks that don't need Acrobat.

**With an AI assistant or the scripts.** Our scripts, planned for `tools/`, carry out 4b to 4d from a list of the approved texts and run the checks in 4e. An assistant drafts the equation readings for the instructor to approve. The instructor knits, runs Autotag, and approves every text before it is written.

**Evidence:** our practice.

---

## Alternatives we tried or considered

**Printing the HTML to a tagged PDF.** We printed a knitted HTML worksheet to PDF from Chromium with tagging on. The result was tagged: figures carried their alt text, headings mirrored the HTML, the title and bookmarks were set, and code was readable as text. We kept the knitted LaTeX PDF anyway, because we preferred how it looks. Two notes for anyone trying this: only Chrome's own Save as PDF tags the file (the macOS print dialog does not), and math was not tested. **Evidence:** found by inspecting files (a PDF saved from Chromium, October 2026).

**maidr in every setup chunk.** `maidr::maidr_on()` makes the ggplot2 plots in the knitted HTML explorable by keyboard, sound, and braille. In our test it also dropped those plots' `fig.alt` text and captions from the HTML, removed them from the knitted PDF, left base R plots unchanged, and loaded its code from the web, unpinned, every time the page opened. We don't use it in posted documents. Turning it on for HTML output only (`if (knitr::is_html_output()) maidr::maidr_on()`) may avoid the PDF problem; we have not tested that. **Evidence:** found in testing and found by inspecting files (R 4.6.0, maidr 0.4.0, rmarkdown 2.31, and knitr 1.51, October 2026): a maidr plot opened from the console was explored by keyboard and heard ([test results](../testing/README.md#maidr-from-the-r-console)); what `maidr_on()` does to knitted documents was found in the [knitted files](../testing/README.md#found-by-inspecting-files). For students using maidr themselves, see [Working in R with a screen reader](../students/working-in-r-with-a-screen-reader.md).

**Tagging at the source.** Quarto can render to a tagged PDF (`pdf-standard: ua-2`, with a recent TeX Live or Typst), where `fig-alt` reportedly carries into the PDF; LaTeX's own tagging (`\DocumentMetadata{tagging=on}`) does the same for documents written in LaTeX. Either could retire the Autotag step. We have not tried them.

---

## Untested or open

- **Nothing in the remediated PDFs has been heard with a screen reader.** The checks are structural: correct tags are necessary for a good listening experience, not proof of one.
- **The inline-symbol fix** (4d) has not been heard with a screen reader.
- **Equations in the HTML with NVDA.** VoiceOver in Safari read MathJax equations well; NVDA has not been tested ([Test results](../testing/README.md#voiceover-with-safari-on-knitted-html)).
- **The language setting** in our own knitted HTML has not been checked.
- **Whether students should knit to HTML themselves,** rather than to PDF, is a teaching decision we have left at our default.
- **Autotag requires Acrobat Pro,** a commercial product. A route without it is the main reason to try tagging at the source.
