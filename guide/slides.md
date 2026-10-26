# Slides

This chapter walks through the [pipeline](pipeline.md) for a lecture deck. The baseline is PowerPoint: it has the accessibility features the work needs (alt text, a decorative flag, control of reading order, tagged PDF export), and the companion Word document is built from a .pptx.

- **Decks authored in Keynote or Google Slides** are exported to .pptx and remediated there. Keynote's own PDF export failed our audit: no document language, every bullet tagged as a top-level heading, fewer than half the figures with alt text, and table headers lost. So the PDF is exported from PowerPoint. **Evidence:** found by inspecting files (a Keynote PDF export, October 2026; [Test results](../testing/README.md#found-by-inspecting-files)). Carrying fixes back into the source file is covered under [After posting](#after-posting).
- **Decks authored in Beamer** are a different case; see [Beamer](beamer.md).

After some preparation ([Before you start](#before-you-start)), the work has four stages:

1. **[Structure](#1-structure).** Group the pieces of each drawn figure, ungroup callout boxes so their text is read as text, and split builds whose later steps cover earlier content.
2. **[Plan](#2-plan).** Proofread; turn pictures of text and code into real text; rebuild pictures of tables as real tables with header rows; empty table cells hidden under shapes; check text contrast, meaning carried by color alone, link text, and wording that only works by sight; decide which figures need a description and which repeats are decorative.
3. **[Draft and review](#3-draft-and-review).** Write descriptions from the slides as students see them, one build at a time, in the course's house style, and review them in place.
4. **[Reading order and decorative](#4-reading-order-and-decorative).** Title first, then the order the lecture follows; repeated content marked decorative.

The finished deck then [ships](#ship) as an accessible PDF and a text-only [Word companion](word-companion.md), each checked as students will receive it. Fixes made later go into every output ([After posting](#after-posting)).

Each stage is described in more detail below, along with instructions on how to do it by hand, with the scripts, and with an AI assistant. Menu paths are for recent versions of PowerPoint on Windows and Mac; they vary between versions.

## Before you start

**What and why.** Two habits save the most time later: working from what students see, and not redoing work already done. The picture stored in a slide file and the slide a student sees are different: crops, overlays, arrows, labels, and shaded regions are drawn on top in PowerPoint. In one lecture deck, most of the objects that needed a description had no picture file behind them at all; they were shapes and text drawn over a chart. Describing from the stored images produced descriptions of the wrong thing.

**By hand.**

1. **Put the Accessibility tab on the ribbon.** PowerPoint's Accessibility tab gathers most of the tools this chapter uses: Check Accessibility, the Reading Order Pane, Alt Text, Mark as Decorative, Group, and Insert Header Row. By default it appears only while the Alt Text, Reading Order, or Check Accessibility pane is open (for example, after right-clicking a picture › View Alt Text, or Review › Check Accessibility). To keep it on the ribbon all the time, turn it on in PowerPoint's ribbon settings: on a Mac, PowerPoint › Preferences › Ribbon & Toolbar, then check **Accessibility** in the list of tabs; on Windows, File › Options › Customize Ribbon. Which tools it holds depends on your version of PowerPoint.
2. **Keep an untouched copy** of the deck before anything changes. Later stages compare against it, and it is the only record of what the export looked like.
3. **Decide what happens to speaker notes.** Notes travel with a .pptx and screen readers read them. Clear notes no longer used for teaching, or keep the ones that are; decide once, at the start.
4. **Carry over slides already remediated** in an earlier deck rather than redoing them. Copy them from the remediated deck and paste with **Keep Source Formatting**, which keeps alt text, groups, decorative flags, and table settings. Then review them in the new deck like any other slide: a description that was right in one lecture can be wrong in the next (it may refer to a slide that is no longer there).
5. **Work from the slides as students see them.** PowerPoint's Normal view, with its slide thumbnails, shows each slide with everything drawn on top of its pictures, which is what students see in the posted PDF. Describe from the slide there, not from a picture file opened on its own. To see a build step by step, play it in Slide Show. An AI assistant can't see your screen, so it needs the slides exported as images instead (File › Export, as PNG).
6. **Have a house style** before writing anything: spelling, preferred terms, how symbols are spelled out. See the [template](house-style-template.md).
7. **For decks from Keynote,** open the exported .pptx in PowerPoint and save it once before starting: until then, some tools cannot see Keynote's equations.
8. **Check the theme's colors once per course.** Most contrast problems come from a theme or template: light gray text, pale callout fills, colored text on colored backgrounds. Text needs a contrast ratio of at least 4.5:1 against its background (3:1 for large text: 18 pt, or 14 pt bold). Fix the colors in the theme, and in the source file if the deck is authored elsewhere, so the fix is made once rather than slide by slide every year.

**With the scripts.** 
`alt_audit.py` gives a first measure of the job: how many pictures have real descriptions, how many carry a file name or a placeholder, and how many look like repeats that could be decorative. Reuse matching across decks is planned.

**With an AI assistant.**

| Assistant | Instructor |
|---|---|
| Matches slides to earlier remediated decks and proposes which to carry over | Confirms the plan; pastes the slides in PowerPoint; settles conflicts between versions |
| Renders every slide to an image; writes short labels ([a], [b]) into object names | Decides the speaker-notes policy |

## 1. Structure

**What and why.** This stage decides which objects exist. Two rules cover most slides: **the pieces of a figure are grouped, and callout boxes are ungrouped.** A figure drawn from many pieces (curves, axes, labels, arrows pointing into it) needs one description, which goes on the group. A callout box exported as a text box plus a background shape is text, and should be read as text, with the background marked decorative. Builds are the third concern: a PDF shows each slide only in its final state, so where a later step of an animation covers earlier content, that content is lost from the PDF unless the build is split into separate slides.

Grouping has a cost worth stating whenever it is proposed: **PowerPoint cannot animate a piece inside a group**, so grouping an animated piece removes its animation. If the .pptx is not one of the posted files, no student sees those animations anyway.

**By hand in PowerPoint.**

1. Open the **Reading Order Pane** (Accessibility › Reading Order Pane). It lists the objects on the slide in the order a screen reader reads them, shows each group as a single item, and marks objects with no alt text; you will use it again at stage 4. To see what is inside a group, or to pick out pieces that are hard to click on the slide, open the **Selection Pane** as well (Home › Arrange › Selection Pane), where groups expand to show their members.
2. **Group a figure:** select its pieces (Shift-click them on the slide, or Ctrl-click or Cmd-click them in the Selection Pane), then right-click › Group › Group (or Shape Format › Group, or Accessibility › Group). Include labels and arrows that point into the figure; leave out sentences and slide-level text.
3. **Ungroup a callout box** made of text plus a background shape: select it, then right-click › Group › Ungroup (or Shape Format › Group › Ungroup). Its background is marked decorative at stage 4.
4. **Group every copy of a repeated figure the same way,** even copies that will end up decorative. Grouped objects are much easier to work with in the Reading Order and Selection panes, and the alt-text-or-decorative decision is then made once per figure.
5. **Split a build that covers content:** duplicate the slide once per step that matters (right-click its thumbnail › Duplicate Slide), and on each copy keep only what is visible at that step.

**With the scripts.** None released yet. Checks for content covered later in a build, and for loose figure pieces, are planned.

**With an AI assistant.**

| Assistant | Instructor |
|---|---|
| Proposes groups and ungroups, shown on the slide image with each proposal outlined and lettered; says which animations a group would remove | Approves, changes, or skips each proposal |
| Flags content a later build step covers, with the slides involved | Decides whether to split the build |
| Carries out the approved grouping | Checks the result on the slide |

**Evidence:** our practice. The grouping rule came from a deck in which we undid most of the proposed changes, because every existing group had been treated as a figure.

## 2. Plan

**What and why.** Before anyone writes a description, settle what each object *is*. In our first full deck, a quarter of the descriptions drafted were for objects that later turned out to be decorative, deleted, or pictures of text that became real text. Planning also catches problems that are not about description at all:

- **Typos and errors** in slide text, titles, table cells, and code comments. Code is checked for curly quotes, which break code students paste.
- **Pictures of text become real text.** A screenshot of code, a definition, or a quotation is carrying text; a real text box reflows, scales, can be searched, and exports to the PDF as text, and needs no alt text. The exception is a screenshot kept to show a highlighted part in context; then its alt text says what is highlighted.
- **Pictures of tables become real tables** with the header row (and first column, where it has headers) marked, so a screen reader announces each cell with its headings. Two exceptions keep the picture, with alt text saying what it shows: the same table repeated with selected cells highlighted, and a table that is illustrative rather than there to convey its data.
- **Table cells hidden under shapes are emptied.** A table revealed a cell at a time, by covering the rest with shapes, still holds every answer in its cells, and a screen reader reads them on every slide of the build, starting with the first. Emptying the covered cells changes nothing on screen.
- **Which figures need a description, and which repeats are decorative.** A figure repeated unchanged on the very next slide is usually marked decorative, so the listener isn't asked to hear it again. Identical content on non-consecutive slides is usually kept: by then a listener can't be expected to hold it. See [Describing figures](describing-figures.md).
- **Placeholder alt text is cleared:** file names, the word *Image*, text added automatically.
- **Contrast and color.** Text that falls below the contrast ratios above, including text over pictures and on highlighted or colored fills; and slides where color is the only thing telling items apart (chart series, highlights), which need a label, pattern, or wording as well.
- **Wording that only works by sight:** the red line, on the right, this box. Name the thing instead.
- **Link text** that says where it goes, not a bare web address or click here. A web address on a slide is fine where the surrounding text makes its purpose clear.
- **Moving content.** Animated GIFs (memes are the usual source) need a way to pause, or a still image instead, and nothing may flash more than three times a second.

**By hand in PowerPoint.**

1. Proofread every slide, including notes you will keep.
2. Replace each picture of text with a text box (monospace for code), and delete the picture.
3. Rebuild pictures of tables with Insert › Table. On every table, select it and turn on **Table Design › Header Row** (and **First Column** where it applies), or use Accessibility › Insert Header Row.
4. For a table revealed under covering shapes, delete the text in each covered cell on each slide of the build; the covering shapes stay, so the slide looks the same.
5. Open the **Alt Text** pane (Accessibility › Alt Text, or right-click an object › View Alt Text). Clear placeholder text. Note which figures need a description and which will be marked decorative.
6. Check contrast where text sits on color or on a picture. Recent versions of PowerPoint's **Check Accessibility** (on the Accessibility or Review tab) flag hard-to-read text contrast, including text over images; a free contrast checker with an eyedropper covers the rest.

**With the scripts.** `cells.py detect` lists table cells hidden under a covering shape, and `cells.py blank` empties the ones the instructor names. `alt_audit.py` lists placeholder alt text by slide.

**With an AI assistant.** The assistant's plan for each slide is written into that slide's speaker notes as a numbered list (see [The speaker-notes review loop](../ai-assistant/review-loop.md)).

| Assistant | Instructor |
|---|---|
| Proofreads every slide and lists each fix | Skips any fix that isn't wanted |
| Measures text contrast on the rendered slides; flags color-only meaning, wording that only works by sight, bare links, and animated GIFs | Skips any finding; carries visible fixes back to the source file if the deck is authored elsewhere |
| Transcribes pictures of text and code; proposes real tables with header rows; finds hidden cells | Skips a swap where the picture shows a highlighted part in context, saying what the description should cover instead |
| Recommends which repeated figures to mark decorative, once per figure family | Skips any recommendation; says "done" to approve the rest |
| Carries out everything not skipped | — |

**Evidence:** our practice; hidden cells and placeholder alt text found by inspecting files (our own decks).

## 3. Draft and review

**What and why.** Descriptions are written from the slides as students see them, not from the picture files inside them, and **one build at a time**: across a build, each slide's description says only what changed, so the descriptions depend on each other and are written as a sequence. How much to say follows the lesson, not the figure: a chart type seen for the first time needs its axes explained, the tenth needs a sentence. The conventions are in [Describing figures](describing-figures.md) and [Equations](equations.md), and the house style is applied as each description is written, not corrected afterwards.

Review happens in the same pass, and covers **every** alt text in the deck, including descriptions carried over from an earlier deck: a description signed off in one lecture can be wrong in the next.

**Equations made with PowerPoint's equation tool get no alt text** ([E2](equations.md#e2)): PowerPoint writes its own spoken reading of each equation into the PDF, and alt text added to an equation made a listener hear it up to four times. Equations reach a listener in the Word companion, as live Word equations. Figures that contain equations, such as a chart with a symbol on its axis, are still described as figures.

**By hand in PowerPoint.**

1. Work through each build in order, in Normal view, using the slide thumbnails to see what each step adds.
2. Select the figure (the group, for a grouped figure) and write the description in the **Alt Text** pane.
3. Read the descriptions of a build in order, aloud if possible: does each say what changed, and would a listener know what is being pointed at?
4. Where an arrow joins two callouts in an argument, the instructor may give the arrow a short phrase of narration leading into the next item. Narration is the instructor's voice; see [Describing figures](describing-figures.md).

**With the scripts.** `alt_audit.py` shows what still has no real description. Drafting descriptions is not scripted: it means looking at the figure.

**With an AI assistant.**

| Assistant | Instructor |
|---|---|
| Drafts descriptions from the rendered slides, one build at a time, house style applied, and writes them into the alt-text fields | Reviews each description in place: edits it, or leaves it to approve |
| Lists every alt text in the deck in the speaker notes, marked by who wrote it, including descriptions carried over | Decides what each figure is for, and says so where a draft misses it |
| Marks any draft that reveals a conclusion the slide sets up for students to reach (REVEALS) | Decides whether to keep, soften, or cut it |
| Never writes narration on arrows unless asked | Writes narration on arrows |

**Evidence:** our practice. The share of drafts kept unchanged rose as the conventions were written down, from a sixth in the first full deck to most of them in the next.

## 4. Reading order and decorative

**What and why.** A screen reader reads a slide's objects in its reading order, which is not necessarily the order they appear on screen. Reading order goes last because any structural change undoes it. The rules we follow:

1. Title first.
2. Within a box or column, top to bottom: a header before its body.
3. The order the lecture tells it, over the layout: the setup before the figure it sets up; a question before the table that answers it; a table's note after the table.
4. A legend straight after its figure's title, not after the figure.
5. A narrated arrow between the two items it joins.
6. Rows of similar panels left to right.

This is also where repeated **text** is marked decorative: a title repeated across a build, a callout unchanged from the previous slide. The screen reader we tested still announced the slide number when the title was decorative. **Evidence:** our practice (the rules came from our own reordering of one deck, then confirmed); repeated titles, found in testing ([NVDA with PowerPoint](../testing/README.md#nvda-with-powerpoint), October 2026).

**One PowerPoint quirk:** the reading order is the stacking order. Moving an object earlier in the reading order moves it further back on the slide, and can push text behind a background shape. Check the slide after reordering. Placing each decorative background just before the text it sits behind keeps the list readable and the text on top.

**By hand in PowerPoint.**

1. Open the **Reading Order Pane** (Accessibility › Reading Order Pane). Drag objects into order, or select one and use Move Up and Move Down.
2. Mark repeated text and pure decoration decorative: select it, then Accessibility › **Mark as Decorative** (or the **Mark as decorative** checkbox in the Alt Text pane).
3. Check each reordered slide on screen for text that has slipped behind a shape.

**With the scripts.** None released yet. A check for the title-first and left-to-right rules is planned.

**With an AI assistant.**

| Assistant | Instructor |
|---|---|
| Checks title first and rows left to right; proposes decorative flags for repeated text | Checks the order the lecture tells it, slide by slide, and adjusts |
| Checks slides for text pushed behind shapes after reordering | — |

## Ship

**What and why.** The posted files are checked as students will receive them. We post two files per deck: the PDF of the slides, designed for most students, and the Word companion, designed for listening. Every file we post is made accessible, and each is designed for different readers.

**By hand.**

1. **Clear working notes** from the speaker notes, and remove any labels written into object names.
2. **Set the document title:** File › Info › Properties › Title (Windows) or File › Properties › Summary › Title (Mac). Readers announce it; without it they announce the file name.
3. **Export the PDF from PowerPoint** with the accessibility option: on Windows, File › Save As › PDF › Options, with **Document structure tags for accessibility** checked; on Mac, File › Save As › PDF › **Best for electronic distribution and accessibility**. On a Mac, that option sends the file to a Microsoft online service to make the PDF, so it needs an internet connection and uploads the deck; check that your institution allows this for course materials.
4. **Check the PDF:** tagged, language set, title shown, alt text on every figure, header cells on tables, a heading for each slide. Acrobat's accessibility checker does this. Before exporting, PowerPoint's own **Check Accessibility** is a quick baseline (missing titles, contrast, alt text); it checks that alt text exists, not that it is any good.
5. **Never run Acrobat's Autotag on a PowerPoint export.** It discards the tags PowerPoint wrote from the remediated deck, including every equation's reading ([E5](equations.md#e5)).
6. If the .pptx itself is shared: remove animations, give objects short meaningful names (the screen reader we tested read object names aloud), and remove comments.

**With the scripts.** `pdf_audit.py` lists the PDF's tags: language, headings, figures, and their alt text. PowerPoint also appends an object type to some alt text in the PDF (for example "(Grouped Object)"); a script to remove it is planned.

**With an AI assistant.**

| Assistant | Instructor |
|---|---|
| Clears notes and labels; sets the document title; lists differences from the untouched copy for the instructor to settle | Exports the PDF from PowerPoint |
| Checks the PDF's tags, language, alt text, and header cells; flags figures with no alt text | Fixes what it flags in the deck and exports again |
| Builds the Word companion and its review list | Reviews the companion; posts both files |

## The Word companion

Built last, from the finished deck, and posted beside the PDF: a text-only Word document designed for listening, with each figure as its description and equations as live Word equations. What goes in it, the formatting choices, and how to build it are in its own chapter, [The Word companion](word-companion.md).

## After posting

- **A fix goes into every output:** the deck, a fresh PDF export, and the Word companion.
- **And back into the source,** if the deck was authored in Keynote or Google Slides, so it is not redone next year. Wording fixes and picture descriptions can usually be carried back by hand; groups, reading order, and decorative flags generally cannot, which is the cost of remediating in a .pptx exported from another program.
- **Keep the posted copies,** so later fixes can be compared against what students received.
