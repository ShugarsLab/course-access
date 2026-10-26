# Readings

This chapter walks through the [pipeline](pipeline.md) for assigned readings: journal articles and book chapters as PDFs from a publisher. A reading is someone else's document. The goal is access to it, not improving it, so every change is the smallest one that gets there: add what is missing, and keep what the publisher built.

How readings differ from the other materials in this guide:

| | Slides | R Markdown worksheets | Readings |
|---|---|---|---|
| Who made the structure | The deck's author; alt text is often a file name or placeholder | Nobody: a knitted PDF has no tags | The publisher, often competently |
| What to do with existing tags | Correct them in the deck | Autotag, then correct | **Keep them** |
| Figures | Slide objects, described from the rendered slides | Plots, described from the knitted HTML | Usually images at print resolution |
| Text around a figure | The slide's text sets how much to say | The worksheet's prose | The paper already discusses every figure |

**Status:** draft, based on only a few articles, one of them taken through every step below. Treat every step as provisional until more readings confirm it. Nothing here has yet been heard with a screen reader.

Acrobat Pro's menu and panel names change between versions, so the steps below name the tools (the tags panel, the accessibility check, the reading-order tool) rather than menu paths.

---

## Before you start

- **Check with your library before posting a reading.** Whether you may post a copy of an article or chapter at all, and whether you may post a copy you have changed, depends on the library's license with the publisher and on copyright law, including its provisions for accessibility. Your library (often through its course reserves or copyright staff) can tell you what is allowed. The library may also be able to link the course to its licensed copy instead of a posted file, obtain an accessible version from the publisher, or work with your institution's disability services office, which can often request accessible files for a student. This chapter covers how to make a reading accessible, not whether a remediated copy can be posted; that question is for your library.
- **Look for a better version first.** Many journals publish an HTML version of each article, which often has real tables and sometimes figure descriptions, and some publishers supply accessible files on request. If there is one, it may be worth linking beside the PDF. We have not yet compared one with a remediated PDF.
- **Keep the original, untouched,** exactly as downloaded. Every later step writes a new copy. If Acrobat's Autotag has already been run on the file, go back to the download.
- **A scanned reading has no text at all,** only pictures of pages. It needs optical character recognition (OCR) before anything else in this chapter applies. We haven't yet had one.

---

## 1. Audit the existing tags

**What and why.** The publisher's tags decide what a screen reader can do with the paper: move between headings, read a table with its headers, hear a figure's description. Find out what is there before changing anything.

Look for:

- **Real structure:** paragraphs, headings in a sensible hierarchy, tables with header cells. A PDF reporting itself as tagged proves nothing either way; look at the tags themselves.
- **Figures with no alt text,** and which of them are real figures and which are logos and icons.
- **The language.** It should be a language code, such as `en`; publishers sometimes write the word English instead.

**By hand.** Open the PDF in Acrobat Pro and look through the tags panel, and run Acrobat's accessibility check.

**With the scripts.** `tools/pdf_audit.py` lists the language, how many of each tag there are, each figure with the start of its alt text, and (with `--headings`) the headings in order.

```
python3 pdf_audit.py paper.pdf
python3 pdf_audit.py --headings paper.pdf
```

**Keep the publisher's tags.** If the tags are usable, don't run Acrobat's Autotag. On the article we remediated, the publisher's tagging was complete: headings, about 570 paragraphs, 9 tables with 102 header cells, and 23 figure tags. Autotag made it worse: it renumbered the headings so that sections and subsections dropped two levels, tagged the author's name as a heading, and tagged the title twice. Autotag is for a file with no tags at all; then the corrections in [R Markdown worksheets, stage 4](rmarkdown.md#4-remediate-the-knitted-pdf) apply.

**Evidence:** our practice; Autotag's effect found by inspecting files (comparing the two files' tags; [Test results](../testing/README.md#found-by-inspecting-files)).

---

## 2. Look at every figure

Journal figures are dense and small on the page. Look at each one at full resolution: zoom well in, or extract the embedded images (Acrobat can export them, and so can command-line tools such as `pdfimages`). Then read what the paper itself says about the figure, in its caption and in the text, because the text usually already states the main finding.

**Evidence:** our practice.

---

## 3. Draft descriptions for approval

The conventions in [Describing figures](describing-figures.md) apply, house style included. Three things are different for readings:

- **Add what the prose leaves out.** The paper already says what each figure shows ("Figure 1 shows…"), so the description gives what a reader of the text alone would miss: the layout, the actual values, the panels the text skips.
- **Describe paired figures in parallel.** Where two figures share a layout (the same chart for two countries, say), describe them in the same order, the second referring back to the first, as for a series of figures in a lecture ([F7](describing-figures.md#f7)).
- **Describe the figure, not the method.** A reading may use methods students haven't met yet. Teaching the method is the lecture's job; the description says what the figure shows.

Where a figure lists items (the words in a word-frequency chart, say) and the text discusses only some of them, the description lists all of them: a sighted reader can see the rest.

Show the instructor every description together, before anything is written into the file.

**With an AI assistant.** The assistant reads each figure at full resolution alongside the paper's discussion of it and drafts the descriptions. The instructor approves every one.

**Evidence:** our practice.

---

## 4. Write the descriptions and the language

Add the alt text and the language code, and change nothing else.

**By hand.** In Acrobat Pro's tags panel, open each figure tag's properties and enter the approved text as its alternate text; set the document's language in the document properties.

**With the scripts.** Our script, planned for `tools/`, writes approved descriptions into the figure tags, page by page, and sets the language. It refuses a page with more than one figure tag rather than guessing which is which, and then checks its own work: each description reads back exactly, the tags are otherwise unchanged, every page looks the same, and the text is identical.

Don't run Autotag on the finished file.

**Evidence:** our practice.

---

## 5. Mark logos and icons decorative

Cover-page logos, ORCID icons, and open-data badges carry nothing a reader needs. Mark them as artifacts in Acrobat: in the tags panel, change each one's tag to an artifact (or use the reading-order tool's background setting). On our article, that was 17 figure tags, 11 of them on the cover page.

This stays a manual step even with the scripts. In a PDF, marking something decorative means three coordinated changes: removing it from the tags, re-marking its drawing on the page as an artifact, and updating the index that links tags to page content. Acrobat makes all three together. A script doing it edits the page content itself, where a mistake can misalign tags and content without changing how the page looks. For logos and icons, the risk isn't worth it.

**Evidence:** our practice.

---

## Untested or open

- **Only a few articles so far.** Every step is provisional until more readings confirm it.
- **Not heard with a screen reader.** The checks are structural.
- **Text in another language.** Passages in another language, such as names in Cyrillic in a table, carry no language marking, so an English voice mispronounces them. Marking them is structure editing; whether it is worth doing is open (WCAG 3.1.2, Language of parts; see [WCAG coverage](wcag-coverage.md)).
- **The publisher's HTML.** Whether it is a better route than a remediated PDF is untested.
- **Equations in readings,** whether as text, as images, or as tagged math, have not yet come up.
- **Scanned readings** have not yet come up.
