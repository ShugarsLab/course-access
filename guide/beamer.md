# Beamer (LaTeX)

*Chapter in progress.* The [slides chapter](slides.md) is written for PowerPoint, and decks made in Keynote or Google Slides come to PowerPoint for remediation ([Keynote and Google Slides](keynote-google-slides.md)). Beamer needs a different route.

*Not yet tested by us.* Beamer is probably the most common way to make statistics and mathematics slides, so this chapter matters. What follows is our analysis and the documented status of LaTeX's tools; we plan to test it on a demo deck (see [What we plan to test](#what-we-plan-to-test), below).

## Why Beamer is different

- **The source is the document.** A Beamer PDF is rebuilt every time the source is compiled, so any fix made to the PDF afterwards (in Acrobat, say) is lost at the next compile. Remediation has to live in the `.tex` source.
- **The default PDF has no structure.** A PDF compiled the usual way (pdfLaTeX) is untagged: no headings, no reading order, no alt text. Equations are drawn as font glyphs, which a screen reader may read badly or not at all.
- **LaTeX can now make tagged PDFs, but not yet from Beamer.** With LuaLaTeX and `\DocumentMetadata{tagging=on}`, LaTeX writes a tagged PDF: headings, alt text on images (`\includegraphics[alt={…}]`, or `artifact` for a decorative image), and MathML for equations. Some universities publish setup guides (for example, [Rutgers Mathematics](https://math.rutgers.edu/images/Tagged_PDF_Instructions_2.pdf)). But the LaTeX tagging project does not yet support the Beamer class ([tagging status](https://latex3.github.io/tagging-project/tagging-status/full)).
- **Builds work the other way round from PowerPoint.** Beamer's overlays (`\pause`, `\only`, `\uncover`) put each step of a build on its own PDF page. Nothing is lost under later content, as it can be in a PowerPoint PDF, but a listener hears the repeated content again on every page, and there is no equivalent of PowerPoint's decorative flag to mark the repeats. Beamer's `handout` mode collapses each frame to its final state, which may suit a version for listening.
- **Drawn figures have no single object to describe.** TikZ and pgfplots figures are drawn as paths, not placed as images, so a description has to be attached to the figure as a whole.

## Routes

| Route | What it involves | Status and caveats |
|---|---|---|
| 1. Describe in the source; build a companion document | Descriptions written in the `.tex`; the source converted with pandoc to a Word document (with native Word equations) or to HTML | Closest to our slides model. Custom macros, TikZ, and overlays need handling. Under the federal rule, a separate accessible version is allowed only where the original can't be made accessible for technical or legal reasons; the current tagging limits may qualify, but check with your institution |
| 2. ltx-talk | A newer LaTeX presentation class with Beamer-like syntax, built for tagged PDF ([CTAN](https://ctan.org/pkg/ltx-talk)) | Marked experimental by its author; interfaces may change. Likely the long-term answer. Porting a deck takes some work |
| 3. Quarto or R Markdown slides | Instructors who write slides in Markdown can render the same source to HTML slides, or to .pptx for the slides pipeline | Many statistics instructors already work this way. To test: how equations, alt text, and builds come through |
| 4. Turn tagging on for Beamer anyway | LuaLaTeX tagging on a Beamer document | Unsupported: may fail to compile or produce partial tags. To test |

How equations read in a tagged LaTeX PDF (MathML, or alt text taken from the LaTeX source) also needs listening tests; LaTeX source read aloud ("backslash frac") would not serve a listener. The conventions in [Describing figures](describing-figures.md) and the writing rules in [Equations](equations.md) apply whatever the route.

## What we plan to test

One Beamer lecture made for this repository, with a chart, a TikZ figure, display and inline equations, and a build, taken through each route above and checked with a PDF tag audit and by ear. Results will replace this chapter's analysis.

**Evidence:** our analysis; published documentation (linked above); not yet tested.
