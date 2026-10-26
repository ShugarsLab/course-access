# Describing figures in teaching materials

This chapter is about the text that stands in for a figure: the alt text on a slide, the description in a companion document, the caption a screen-reader user hears instead of seeing a chart. It collects the conventions we've developed while making one semester of lecture slides and worksheets for our graduate quantitative methods course accessible to a screen-reader user.

Most of these conventions were not imported from a style guide. We derived them from the descriptions one of us (the course instructor) had already written, then refined them each week from edits to draft descriptions and from listening with a screen reader. They are written here as recommendations, but every course will make some choices differently. Choices that are a matter of taste (spelling, preferred terms, how to write symbols) belong in a house style, kept separately: see [house-style-template.md](house-style-template.md) and the worked example in [house-style-example.md](house-style-example.md).

This chapter is the detailed reference: for looking things up, and for an AI assistant to follow. Most readers should start with the [principles](principles.md) and come here when a question comes up. Rules are numbered F1, F2, … so they can be cited. *The numbering is provisional until the first formal release, while the order is still being reviewed; from then on, numbers won't change.*

## Why figures in teaching are a different problem

Most guidance on describing figures is written for documents that report results to readers who already know the field. A figure in a lecture often teaches how to read that kind of figure, is usually part of a build, and sits inside a lecture students hear in the instructor's voice. The [principles](principles.md) and [How screen readers read course materials](screen-readers.md) explain why that changes the answer.

Three things we found along the way shaped everything below:

- **Having alt text is not the same as having a description.** Decks exported from Keynote arrive with the alt-text field already filled in, usually with the picture's file name or the word *Image*. Accessibility checkers count these as present. One of our lecture decks reported alt text on 112 of 112 images and contained no real descriptions at all.
- **Raw counts overstate the work.** Of 99 objects first flagged as needing a description in one lecture, 61 contained no picture at all (shapes and text grouped together for an in-class animation), and the rest came down to about five distinct images, one of them repeated 17 times. Count distinct figures, not objects, before estimating the job.
- **Where a description is written is not always where it is heard.** See the next section.

### How to read each rule

Each rule gives the rule itself, the reason, an example from our own slides, and an **Evidence** line saying where it comes from, using the labels in [Where each rule comes from](README.md#where-each-rule-comes-from).

## Rule index

| ID | Rule | Section |
|---|---|---|
| [F1](#f1) | Match depth to how new the idea is | How much to say |
| [F2](#f2) | Let the slide's own text set the register | How much to say |
| [F3](#f3) | Name the kind of figure | How much to say |
| [F4](#f4) | Lead with the key fact | How much to say |
| [F5](#f5) | Give real numbers, hedged the way you would say them aloud | How much to say |
| [F6](#f6) | State the interpretation, and flag what it reveals | How much to say |
| [F7](#f7) | Across a build, describe only what changed, and name it | Builds and repetition |
| [F8](#f8) | Signal a sequence before it starts | Builds and repetition |
| [F9](#f9) | Describe what is visible at this stage | Builds and repetition |
| [F10](#f10) | Mark repeats on consecutive slides decorative | Builds and repetition |
| [F11](#f11) | Describe the rendered slide, not the image file | What to describe |
| [F12](#f12) | Axes first, then the marks | What to describe |
| [F13](#f13) | One description, one figure | What to describe |
| [F14](#f14) | Transcribe text set as an image | What to describe |
| [F15](#f15) | Mark table headers; don't describe a table's contents | What to describe |
| [F16](#f16) | Carry in words what color carries | What to describe |
| [F17](#f17) | Describe a visual mnemonic, and offer a second one | What to describe |
| [F18](#f18) | Describe legends and keys inside the figure | What to describe |
| [F19](#f19) | Gloss a labeled symbol with what it stands for | Symbols and notation |
| [F20](#f20) | Gloss new terms too | Symbols and notation |
| [F21](#f21) | Introduce notation progressively | Symbols and notation |
| [F22](#f22) | Spell out symbols, following the house style | Symbols and notation |
| [F23](#f23) | Keep the teaching voice | Voice and length |
| [F24](#f24) | Narrate an arrow between the items it joins | Voice and length |
| [F25](#f25) | Describe a feature by what it means in the lesson | Voice and length |
| [F26](#f26) | Keep the small words that paint the picture | Voice and length |
| [F27](#f27) | Long is fine where the idea is new | Voice and length |

## Where descriptions are read

Where a description is written is not always where it is heard. In our testing, NVDA reading a PowerPoint file did not read alt text on groups, arrows, other shapes, or equations; it read the pieces of a group one by one instead. In a PDF exported from PowerPoint, VoiceOver read the descriptions. The full results are in [Test results](../testing/README.md).

So we write every description into the slides, where it reaches the tagged PDF, and every file we post is made accessible, each designed for different readers: the PDF for everyone, and a text-only [Word companion](word-companion.md), in which each figure becomes its description, for listening. Students choose the format that works for them.

---

## How much to say

<a id="f1"></a>

### F1. Match depth to how new the idea is

**Explain how a figure encodes its information the first time students meet that kind of figure, then drop the explanation once it is established.** The same chart can need a long description in one lecture and a short one a few weeks later.

> First appearance: "The horizontal axis lists the possible outcome values, 1, 2, 3, 4, 5, and 6, and the vertical axis indicates the probability of getting each outcome…"
>
> Later: "Probability distribution for a fair die."

In our decks a new chart type got a description of about 280 characters; an established one, about
40. This is the most distinctive thing about describing teaching figures, and it applies across materials: a plot students already met in an earlier worksheet or lecture is already established.

Two refinements:

- **Follow the lesson's focus.** A figure students have seen before keeps only what this lesson uses from it. When a plot type is new, explain the plot before its data (what a Q-Q plot shows, then what this one shows).
- **Name individual points only when the instructor would point them out in class.** A reference to a point in the surrounding text is one signal; otherwise, labels a program prints beside points (row numbers, case IDs) are left out.

**Evidence:** our practice; the two refinements inferred from edits, then confirmed.

<a id="f2"></a>

### F2. Let the slide's own text set the register

**Read the slide before describing its figure.** If the slide already names the concept, the figure illustrates a stated idea and wants a sentence. If the figure *is* the evidence, it wants the numbers.

> Too much, on a slide titled The uniform distribution: "Bar chart titled 'Probability of Rolling x.' Values 1 to 6 along the horizontal axis, probability on the vertical axis. All six bars are exactly level with a gray dashed line at 1/6 — the uniform distribution of a fair die, where every outcome is equally likely."
>
> Right: "The uniform distribution expected for rolling a fair six-sided die. All values 1 through 6 have an equal 1/6 probability of being rolled."

This is F1 keyed to what the slide is doing rather than to where it sits in the course. The heaviest cuts to draft descriptions in our first remediated lecture were all this mistake.

**Evidence:** inferred from edits, then confirmed.

<a id="f3"></a>

### F3. Name the kind of figure

The first time a kind of figure appears, name it: "a path diagram", "a histogram", "a scatterplot with a fitted line for each group". The name tells the listener how to picture what follows, and gives later descriptions and the lecture something to refer back to ("the same path diagram, now with estimates on each arrow").

**Evidence:** inferred from edits, then confirmed (the instructor's blind review of drafts).

<a id="f4"></a>

### F4. Lead with the key fact

**Open with what the figure is there to show, and cut what the lesson doesn't use.** On a histogram of bootstrap estimates used to judge whether an effect differs from zero, where zero falls relative to the tails is the point; a word like lopsided is decoration. Don't mention what isn't there unless its absence matters ("the paths have no letter labels"). Accurate detail beyond what the lesson needs still costs the listener time.

**Evidence:** inferred from edits, then confirmed (the instructor's blind review of drafts).

<a id="f5"></a>

### F5. Give real numbers, hedged the way you would say them aloud

**Give concrete values, approximated the way you would say them aloud.**

> "a minimum around 204 and a maximum of 232. Values peak at a mean of about 215mm."

The hedging tells the listener which numbers matter and which are only there to give a sense of scale.

**Evidence:** our practice.

<a id="f6"></a>

### F6. State the interpretation, and flag what it reveals

**State what the figure shows: the interpretation the instructor would give aloud.**

> "This group appears to have even longer flippers."

A sighted student gets the interpretation from the instructor's voice while looking at the chart. Leaving it out of the description doesn't remove an advantage; it creates one.

**When the slide sets the point up for students to find.** Some slides ask students what they notice, or what they predict. Stating the interpretation there hands a listener the answer the class is working toward. But withholding it is hard to do well, and many questions on slides are ones the lecture asks of itself and answers a moment later. So we state the point by default and **flag any description that reveals a conclusion the slide sets up**; the instructor decides whether to keep it, soften it, or cut it. An AI assistant can mark these as it drafts.

**Evidence:** our practice; the flag adopted after a prompt test, where withholding the answer by rule was stricter than the instructor's own judgment.

---

## Builds and repetition

### Why: listening is serial

A sighted student meeting the same table or chart for the ninth time does roughly constant work to find what changed: the eye lands on the one row that differs. A listening student does linear work: to reach the ninth cell, they pass through the first eight. The information is identical and the cost of reaching it is not, and the whole difference falls on the listener.

This asymmetry is easy to talk yourself out of, because both students are receiving the same content. It is the reason behind most of the rules in this section (F7 to F10), and it is also why text that points instead of naming (the probability of ending up in *this box*, *these three regions*) fails: it assumes a reader who can look back at will. The fix for that kind of text belongs in the visible slide text, naming what is meant, not in alt text on an arrow.

**Evidence:** our analysis.

<a id="f7"></a>

### F7. Across a build, describe only what changed, and name it

**Each slide in a build states only what changed from the slide before.**

> "Same histogram plot as last slide, but now with the data filled in."

But the change has to be named, not gestured at. "Same plot as the previous slide" is not a description of what changed; the listener can't see the previous slide either. In our first remediated lecture, every draft that stopped there was rewritten, and those rewrites were the largest edits in the set. Where nothing changed at all, the answer is usually the decorative flag rather than a description (F10).

Descriptions written this way depend on each other: rewriting one can leave the next saying "the same result again" about something no longer described anywhere. Draft and review a build as a unit.

**Evidence:** our practice; the "name the change" rule inferred from edits, then confirmed.

**Purpose comes first.** Most of the time, and always across a build or a repeat of the same figure, what changed is the key thing. But a figure that introduces a new idea stands on its own: describe it as that idea, not as a change from the slide before. A slide introducing a standard diagram for a new concept, the kind students will meet again and again, is described as that diagram, even if the previous slide showed a combined diagram that happened to contain it ("a diagram of moderation: an arrow runs from x to y, and an arrow from z points at the middle of that arrow", not "the moderation half of the last diagram").

**Evidence:** inferred from edits, then confirmed (the instructor's blind review of drafts).

<a id="f8"></a>

### F8. Signal a sequence before it starts

**Tell the listener when a build is coming.**

> "Sections of data will be highlighted in the next several slides."

Telling the listener a build is coming lets them pace themselves, rather than discovering mid-sequence that four near-identical descriptions are on the way.

**Evidence:** our practice.

<a id="f9"></a>

### F9. Describe what is visible at this stage

**Where a build reveals an object a piece at a time, the description covers what is visible on this slide only.** Parts still hidden are described on the slide that reveals them. Describing the whole object on the first slide would give away the ending and make the rest of the build redundant.

A later addition to an object already revealed is itself a change: once a table is complete, a slide that adds a bracket over two of its rows describes the bracket, not the table again.

A related trap: cells hidden under shapes in a table build are still read, so the listener hears the answers early. Empty the covered cells ([Slides, stage 2](slides.md#2-plan)).

**Evidence:** our practice.

<a id="f10"></a>

### F10. Mark repeats on consecutive slides decorative

When a slide repeats something from the slide just before it (an unchanged chart, callout, bullet, or table), mark that copy **decorative** so a screen reader skips it, and keep the first copy readable. There will be exceptions. **Identical content on slides that are not consecutive should almost always be repeated**: by then the listener can't be expected to hold it in mind.

The reasoning: many repeated elements are there mainly as visual decoration, or so sighted students can glance back at them. A listener can't glance; they have to hold the relevant information in mind, and hearing it again adds noise that makes that harder.

Practical notes:

- **Group every copy of a figure first, then decide.** Grouped objects are much easier to work with in PowerPoint's Selection Pane, and making the description-or-decorative decision once per figure keeps neighboring slides consistent.
- **Repeated slide titles can be marked decorative** in the slides: in our testing the screen reader still announced the slide number. **In the Word companion, they are kept:** every slide gets a numbered heading with its title, repeats included, so students can refer to the same slide as their classmates ([P7](principles.md#p7); [the companion document](house-style-example.md#the-companion-document) in the worked house style).

**Evidence:** our practice; slide titles found in testing ([NVDA with PowerPoint](../testing/README.md#nvda-with-powerpoint), October 2026); titles in the Word companion from a listener's feedback.

---

## What to describe

<a id="f11"></a>

### F11. Describe the rendered slide, not the image file

**The picture stored inside a .pptx and what a student sees on the slide can be different images.** Between them sit crops, overlays, arrows, labels, and shaded regions drawn in PowerPoint, and on a build slide most of the meaning often lives there rather than in any picture. In one of our lectures, most of the figures needing descriptions were overlays with no image file behind them at all, and one cropped picture showed only a chart's legend while the stored file held the whole chart.

So describe from the slide as it appears (in PowerPoint's Normal view or Slide Show, or a PDF export), and look at the stored image only when the slide is too small to read a dense plot. This matters most when an AI tool drafts descriptions from the file: it can describe the stored picture rather than the slide. Give it images of the rendered slides instead.

**Evidence:** inferred from edits, then confirmed.

<a id="f12"></a>

### F12. Axes first, then the marks

For a chart, give the horizontal axis, then the vertical axis, then what the marks are: "living area on the horizontal axis, log sale price on the vertical axis; each gray circle is a house." Saying what a circle is before the listener knows where it sits leaves them nowhere to put it.

**Evidence:** inferred from edits, then confirmed (the instructor's blind review of drafts).

<a id="f13"></a>

### F13. One description, one figure

**Where two panels on a slide are separate objects, each with its own description, each description covers its own panel.** Opening the first with "two scatterplots sit side by side" promises the listener both, then delivers one. If the panels are to be described together, group them and give the group one description.

**Evidence:** inferred from edits, then confirmed (the instructor's blind review of drafts).

<a id="f14"></a>

### F14. Transcribe text set as an image

**A screenshot of a pull quote, an article, an encyclopedia entry, a definition, or a block of code is carrying *text*.** The right fix is a verbatim transcript placed in a real text box on the slide, not a description in the alt-text field. A text box reflows, scales, can be selected and searched, is exported to PDF as text, and needs no alt text at all. Write the transcript plainly: no "Screenshot of…" framing, no summary.

- **Code is always text.** Screenshots of code and output become monospace text boxes, and the change is made in the source deck so it doesn't have to be redone next year.
- **The exception is the instructor's call:** a screenshot can stay a picture when it highlights a snippet and shows it in context (a highlighted region of program output). Then its alt text says what is highlighted. A clue: the same screenshot on several consecutive slides usually means a different part is highlighted on each.
- **A picture of a table becomes a real table** (F15), not a transcript, since plain text would lose its rows and columns. Two exceptions keep the picture: the same table repeated across slides with selected cells highlighted, and a table that is illustrative rather than there to convey its data. The description then says what is highlighted, or what the table is for, not its values ("a dense grid of 200 values, 20 rows by 10 columns, standing in for a typical dataset").
- **An annotated figure** keeps its picture and is described as a figure.

**Evidence:** inferred from edits, then confirmed; code as text is our practice.

<a id="f15"></a>

### F15. Mark table headers; don't describe a table's contents

**A real PowerPoint table is exposed to a screen reader as a table, read cell by cell, so describing its contents in alt text duplicates what is already there.** What a table needs is its **header row (and header column, if it has one) marked as headers**, a checkbox in PowerPoint's Table Design tab. Without it, landing on a cell announces "Type II error" with no hint of which row and column it belongs to. In our decks the header flags survived into the exported PDF as header cells.

Caveats:

- Marking headers applies the table style's header formatting (bold header row and first column), so it is a visible change.
- Header flags help a listener who navigates to a particular cell. They do nothing for one reading straight through.
- If a table gets alt text at all, it says what the table is *for*, never what is in it.
- **Two-way tables with a spanning label** (a label over all the column headers, or beside all the row headers) read as two header levels mixed in with data. Move the spanning label out of the table into a text box in the same place, styled like the headers it labels, and flag the inner headers.
- **Tables revealed over a build:** keep a real table and empty the cells not yet revealed (F9). Where the build instead highlights selected cells of a table already shown, the repeats can stay pictures, each with alt text naming what is highlighted (F14). The companion document shows the finished table once, as a real table.

Color is never the only signal in a table: every colored header is also a marked header cell. (Our table colors are in [house-style-example.md](house-style-example.md).)

**Evidence:** our practice; header flags in the PDF found by inspecting files (the exported PDF's tags), not by ear.

<a id="f16"></a>

### F16. Carry in words what color carries

**Where color links two things (a colored wash behind a line of text and a matching region on a plot), name the regions in both places and describe them in the same order as the list.** Order plus shared wording does what color does visually. The washes themselves are decorative.

This is not only an accommodation: a link made by color alone already fails for sighted students with color-vision deficiencies, who lose it silently and rarely say so.

**Evidence:** our practice.

<a id="f17"></a>

### F17. Describe a visual mnemonic, and offer a second one

Some memory aids are purely visual: tracing the one vertical stroke in **P** and the two in **N** to remember that a false Positive is a Type I error and a false Negative a Type II error. The trick can be put into words, so state it rather than dropping it. But it depends on knowing printed letter shapes, which a braille reader may not share. The sturdier answer is a **second mnemonic that doesn't depend on seeing**, so every student has one that works.

**Evidence:** our practice; which second mnemonics work best is open.

<a id="f18"></a>

### F18. Describe legends and keys inside the figure

**A legend or symbol key is described as part of its figure, rather than read one entry at a time after it.**

**Evidence:** advice we received, adopted as our practice.

---

## Symbols and notation

<a id="f19"></a>

### F19. Gloss a labeled symbol with what it stands for

**When a figure labels something with a symbol, say what the symbol stands for, not only its name:**

> "a dotted line labeled mu, indicating a potential true population mean"; "mu bar (observed)"; "the mean, mu"

A sighted student connects the label to its meaning at a glance, using the slide and the lecture. A listener hears a bare "mu" in the middle of a description and has to recall it. Gloss the symbol where it first matters and wherever the chart's meaning turns on it; once it is established within a run of slides, the name alone is enough.

**Evidence:** inferred from edits, then confirmed.

<a id="f20"></a>

### F20. Gloss new terms too

**Terms need the same care as symbols.** A box labeled mediator or moderator means little to a student meeting the idea for the first time; say what each does ("a mediator, which carries part of the effect of x on y"). And never refer to something the listener hasn't been told: "a diagram of the two roles" assumes they know which two.

**Evidence:** inferred from edits, then confirmed (the instructor's blind review of drafts).

<a id="f21"></a>

### F21. Introduce notation progressively

**Notation is explained a few times before it is used alone.** Assume a listener who doesn't yet know the standard notation and needs to learn it, but doesn't need reminding every time. We found three stages work, in figure descriptions and equation readings alike:

1. **Name only** until the slides introduce the symbol: "the denominator is the standard error".
2. **Name and symbol together** at the introduction and for the next two or three *spoken* mentions: "standard error, denoted SE, equals …".
3. **Symbol alone** after that.

Details:

- Count what is heard. A decorative repeat doesn't count; visible slide text does (a slide title reading Standard Error (SE) is a pairing).
- Pair the name and symbol again after a long stretch with no spoken mention, and at the first mention in each new lecture.
- A new form of the symbol (squared, a new subscript) gets one gloss on first use if it means something new.
- Use lowercase for common terms ("standard error"), whatever capitals the slide title uses.
- Where both cases of a letter appear together, say "capital N" and "lowercase n" every time.
- In a companion document whose equations are live math, the pairing has to appear in the text (a slide's words, a symbol key, a figure description) before the first equation that uses the symbol alone.

**Evidence:** our practice, worked out from how we revised descriptions over several lectures; the guidance for equation readings is newer and still being refined.

<a id="f22"></a>

### F22. Spell out symbols, following the house style

How symbols, signs, and numbers are written in descriptions ("plus or minus", "negative 3", "r equals negative 0.7") is a house-style decision. Our rule is to take the safest screen-reader reading every time; see [house-style-example.md](house-style-example.md).

---

## Voice and length

<a id="f23"></a>

### F23. Keep the teaching voice

**Write the way the instructor talks in class.**

> "The data follows a normal (ish) distribution"

A description written in the voice of a journal article is a different lecture from the one sighted students attend.

**Evidence:** our practice.

<a id="f24"></a>

### F24. Narrate an arrow between the items it joins

Where callout boxes build an argument across a slide, we sometimes give an arrow a short phrase that leads into the next item, and place the arrow between the two items in the reading order: "mu indicates the", followed by the box the arrow points to; "Power is:", followed by its definition. A description can end the same way, with a trailing ellipsis or a colon marking the break as intentional, so it doesn't sound cut off.

- **Symbols in narration are named exactly as the equation readings name them** ("beta sub 0", not "beta not", if the equations say "beta sub 0"). A listener hears both, and two names for one symbol teach two notations.
- An arrow carrying narration is a deliberate choice, not a missed decorative flag.
- In our testing the screen reader did **not** read alt text on arrows in PowerPoint, so narration reaches a listener only in the companion document, where it is joined to the sentence it leads into. For a .pptx shared as the accessible document itself, narration would have to be visible slide text.

**Evidence:** our practice; arrows not read found in testing ([NVDA with PowerPoint](../testing/README.md#nvda-with-powerpoint), October 2026).

<a id="f25"></a>

### F25. Describe a feature by what it means in the lesson

**Describe a feature by what it means in the lesson,** not by its geometry. In a mediation diagram, "an arrow runs directly from x to y" carries the idea of a direct effect; "an arrow runs straight across" describes only the drawing.

**Evidence:** inferred from edits, then confirmed (the instructor's blind review of drafts).

<a id="f26"></a>

### F26. Keep the small words that paint the picture

**Keep the small words that paint the picture.** Articles and labels make a description easier to follow by ear, even when they make it longer: "an arrow labeled a runs from x up to m", not "arrow a from x to m"; "box x at the lower left"; "y on the vertical axis"; "black circles show cases where z equals 0". Clarity beats brevity, and two short sentences beat one long one.

**Evidence:** inferred from edits, then confirmed (the instructor's blind review of drafts).

<a id="f27"></a>

### F27. Long is fine where the idea is new

**Long descriptions are fine where the idea is new.** We were advised that some screen readers and export formats may cut off alt text beyond about 250 characters; in the companion document, where descriptions are ordinary text, length is not a problem. We keep this in mind but have not shortened descriptions because of it.

**Evidence:** advice we received; truncation not observed in our testing.

---

## Untested or open

These are stated plainly so no one mistakes them for settled practice.

- **The slide PDF has been heard only with VoiceOver in Preview.** How NVDA and JAWS read it is inferred from its tags.
- **Only NVDA (with PowerPoint and Word) and VoiceOver (with Preview) were tested.** JAWS and other combinations may behave differently.
- **Whether a screen reader honors the decorative flag on a PowerPoint table** is untested. Several ways of reducing the cost of a repeated table depend on it (F10, F15).
- **Header cells in the PDF** were confirmed in the file's tags, not by ear (F15).
- **Repeated titles marked decorative** rest on a single test (F10).
- **Prompt slides:** how much to describe when the class is being asked what it notices remains a judgment call (F6).
- **Second mnemonics:** which ones work is a teaching judgment we haven't settled (F17).
- **Repeated tables in slides and PDF:** whether a repeated table can be skipped, and how, is open.
- **Punctuation and notation in slide text and alt text.** Screen readers voice parentheses, quote marks, and colons, and NVDA did not read a superscript 2 as "squared". Our current view: minimize them but don't avoid them altogether, since writing "squared" instead of a superscript costs sighted students the notation, which is worth seeing where it can be seen.
- **Letter case on first mentions** of common notation (Pearson's r; lowercase mu) may be worth stating for a listener learning the notation, even where the other case never appears. Not yet a rule.

## Retired IDs

None yet. Until the first formal release, rules may still be reordered and renumbered. After it, a dropped rule's ID is listed here and never reused.
