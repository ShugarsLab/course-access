# Prompt: draft figure descriptions for a set of slides

**Version 1.2** (2026-10-24): rules from the instructor's blind review of version 1's drafts (purpose before change, naming the figure type, terms glossed, axes first, one figure per description, leading with the key fact, connecting words); not yet tested. Version 1.1 added the REVEALS flag, shorter notes, and the leading zero. Version 1 was tested with Claude on 13 figures.

**Stage:** 3. Draft and review. **Use with:** any AI chat tool that can read images. **Give it:** images of the slides (exported from PowerPoint as PNG), in order, 10 to 20 at a time, with each build kept together; the course context; the house style. **You get back:** a table with one description per figure, and notes on anything to check. Review every description before putting it in the deck. See [Describing figures](../../guide/describing-figures.md) for the full conventions.

Copy everything in the box below into the chat. Replace the three bracketed sections first.

```text
You are helping an instructor write descriptions of the figures in their lecture slides, for
students who use screen readers. A student who is listening, not looking, hears your description
in place of the figure. Write what that student needs in order to learn from the slide, the way
the instructor would explain the figure aloud in class.

COURSE CONTEXT
[The course, its level and subject, and what this lecture covers. What students have already
learned. Which kinds of figures they have already seen in earlier lectures (for example,
histograms, scatterplots with a fitted line) and which are new in this lecture.]

HOUSE STYLE
[Paste the course's house style. If there is none, use: American spelling. Spell out symbols
and signs in words: "plus or minus", "negative 3", "equals", "percent", "times", "mu", "beta sub
1". No quotation marks. Write numbers of 1,000 or more without commas: "140 thousand" when round,
otherwise digits with no comma. Write a zero before a decimal point: 0.31, not .31.]

THE SLIDES
[Say which slides these are, for example "slides 45 to 47, in order" or "slides 56, 65, and 79
from the same lecture; the slides between them are left out".]

YOUR TASK
For each slide, in order:
1. Find each figure that needs a description: charts, plots, diagrams, photographs, or pictures
   that carry meaning, and figures drawn from shapes and arrows. Do not describe text you can read
   on the slide, typed equations, logos, decoration, or real tables (a screen reader reads those
   itself).
2. If a figure repeats unchanged from the slide just before it, do not describe it again. Say in
   the notes that it can be marked decorative.
3. Write one description for each remaining figure, following the rules.

RULES
1. Depth follows how new the idea is. The first time students meet a kind of figure, name it ("a
   path diagram", "a histogram") and say how to read it (what the axes, boxes, arrows, colors, or
   symbols stand for) before what it shows. For a kind of figure they have already seen, skip the
   reading instructions and say what this one shows.
2. Let the slide's own text set how much to say. If the slide's text already makes the point, the
   figure illustrates it: one or two sentences. If the figure is the evidence, give the numbers.
3. Describe what is on the slide, including labels, arrows, highlights, and notes drawn on or
   around the figure. For a chart, give the horizontal axis, then the vertical axis, then what
   the marks are.
4. Purpose decides the framing. Across a build, or a repeat of the same figure, say what is new or
   different and name it; never write "same as before" without saying what changed. But a figure
   that introduces a new idea stands on its own: describe it as that idea, not as a change from
   the previous slide, especially when it is a standard diagram students will meet again.
5. Give real numbers, rounded the way you would say them aloud ("about 215", "from roughly 10 to
   13"). Use only values you can read. If a value is not legible, leave it out and say so in the
   notes.
6. Lead with the point: what the figure is there to show, the way the instructor would say it.
   Cut what the lesson doesn't use, including decorative adjectives and things that are absent
   but don't matter. If the slide sets that point up for students to work out themselves (a
   question to answer, a prediction to make, a pattern to notice), still write the full
   description, and put REVEALS in the notes with the sentence that gives the point away, so the
   instructor can decide whether to keep it.
7. Anything shown by color, line style, or marker shape, say in words, matching the legend.
8. Gloss symbols and terms at first mention: "mu, the population mean"; "a mediator, which carries
   part of the effect of x on y". Never refer to something the listener hasn't been told ("the
   two roles"). After the first mention, the symbol or term alone.
9. Keep the teaching voice: plain, spoken sentences. Describe a feature by what it means in the
   lesson ("an arrow runs directly from x to y"), not its geometry ("straight across"). Keep the
   small words that paint the picture ("an arrow labeled a runs from x up to m", "at the lower
   left", "y on the vertical axis", "black circles show cases where z equals 0"); clarity beats
   brevity, and two short sentences beat one long one. Do not begin with "This image shows",
   "Screenshot of" or "Slide showing".
10. One description, one figure. If two panels are separate figures, each description covers only
    its own panel; don't open with "two plots sit side by side" unless the description covers both.
11. Usually one to three sentences. Up to about five for a new kind of figure or a figure dense
    with data.
OUTPUT
A table with four columns: Slide | Figure | Description | Notes.
- Figure: a few words saying which figure ("scatterplot, left half").
- Description: the text to paste into the figure's alt text.
- Notes: short, and empty when there is nothing to check. Values you could not read; REVEALS
  (rule 6); a suggestion to mark a repeat decorative; a question about what the figure is for.

Before you answer, check each description against rules 1, 3, 4, 6, 8, and 10 and the house style,
and fix what does not fit.

EXAMPLES (from a different lecture; do not copy their wording)
- Too much, on a slide whose text already says "The uniform distribution": "Bar chart titled
  Probability of Rolling x. Values 1 to 6 along the horizontal axis, probability on the vertical
  axis. All six bars are exactly level with a gray dashed line at one sixth." Better: "The
  uniform distribution expected for a fair six-sided die: every value from 1 to 6 has the same
  one-in-six chance."
- First time students see a probability distribution: "The horizontal axis lists the possible
  outcomes, 1 through 6, and the vertical axis gives the probability of each. All six bars are
  the same height." The next time: "Probability distribution for a fair die."
- In a build, not this: "Same histogram as the previous slide." This: "The same histogram, now
  with the data filled in: most values fall between 200 and 230."
- A new idea, not a change: after a slide showing several kinds of sampling distribution together,
  a slide introducing the confidence interval. Not this: "The left part of the last diagram, now
  alone." This: "A confidence interval: a horizontal line marks the range of plausible values for
  the mean, with a dot at the sample mean in its center."
- Small words help: not "Box x lower left, arrow a to m." This: "Box x is at the lower left. An
  arrow labeled a runs from x up to box m."
```
