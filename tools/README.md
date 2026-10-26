# Tools

Five Python scripts that support the accessibility work described in the guide. None of them uses AI, and none of them is needed to follow the guide: everything they check can be done by hand. They save time on the parts of remediation that are tedious to check by eye, and the converter builds a companion document that would take hours to make by hand.

| Script | What it does |
|---|---|
| `alt_audit.py` | Checks whether a deck's alt text is *useful*, not just present |
| `cells.py` | Finds table cells hidden under a shape during a build, which a screen reader still reads |
| `pdf_audit.py` | Lists what is tagged in a PDF: language, headings, figures, and their alt text |
| `pptx2notes.py` | Turns a remediated .pptx into a text-only Word document with live equations |
| `mathspeech.py` | Reads an equation aloud as words; used by `pptx2notes.py`, not run on its own |

## Install

The instructor needs Python 3.10 or later. In a terminal, from this folder:

```
pip install -r requirements.txt
```

`pptx2notes.py` needs `mathspeech.py` in the same folder. The other scripts stand alone.

<a id="alt-text-audit"></a>

## alt_audit.py: is the alt text any good?

Decks exported from Keynote fill PowerPoint's alt-text field with the picture's file name (`Screen Shot 2021-03-24 at 8.39.33 PM.png`) or the word `Image`. Checkers that only ask whether alt text *exists*, PowerPoint's own included, count those as done. We found a deck that reported alt text on 112 of 112 images and had no real descriptions at all. This script sorts every picture's alt text into real descriptions, file names, generic labels, and empty, estimates how many pictures need a real description and how many should be marked decorative (repeats across slides, for example), and prints a worklist by slide.

```
python3 alt_audit.py lecture.pptx
python3 alt_audit.py --csv findings.csv lecture.pptx
```

<a id="covered-cells"></a>

## cells.py: does a table build give away the answer?

A table revealed a piece at a time is usually built by covering the parts not yet shown with an opaque shape. That hides them from the eye only. The text is still in the cells, so a screen-reader user hears the finished table on every slide of the build, often before the class has reached the answer. `detect` lists covered cells; `blank` empties the ones you name, leaving the slide looking exactly the same.

```
python3 cells.py detect lecture.pptx
python3 cells.py blank lecture.pptx --slide 12 --cells '1,2;2,2' -o lecture_fixed.pptx
```

Run `detect` first and check each finding against the slide: a rectangle drawn as an outline around a row is not a cover, and the script tells the two apart, but the instructor decides which cells to empty.

<a id="pdf-tags"></a>

## pdf_audit.py: what does the PDF actually carry?

A PDF is read by a screen reader through its tags. This lists them: whether the PDF is tagged, its language, how many of each tag it has (figures, formulas, tables, headings, and so on), and the start of the alt text on each page's figures. `--headings` lists the headings in order. Use it on a PDF exported from PowerPoint, on a knitted R Markdown PDF, or on a publisher's PDF of a reading.

```
python3 pdf_audit.py lecture.pdf
python3 pdf_audit.py --headings lecture.pdf
```

<a id="word-companion"></a>

## pptx2notes.py: the companion document

Screen readers handle a Word document, and especially its equations, far better than a slide deck. This converter writes a Word version of a deck that reads like lecture notes: slide text in reading order, each figure as its description, tables as real tables, and equations as live Word equations that a math-aware screen reader (for example NVDA with the MathCAT add-on) can read and step through. Every slide gets a numbered heading ("Slide 37: " and its title), so a listener can move from slide to slide and talk about the same slide as classmates.

```
python3 pptx2notes.py lecture.pptx
python3 pptx2notes.py lecture.pptx --changes lecture_changes.csv
```

This writes `lecture.docx` beside the deck, and a copy as generated to `_snapshots/` beside it. If `lecture.docx` already exists, it is treated as the instructor's edited version and is not overwritten; only the generated copy is updated, so the two can be compared in Word (Review › Compare). `-o other.docx` writes only that file. The script prints a review list of things to check by hand (figures without descriptions, equations it rebuilt, and similar), then every number and symbol it rewrote for listening, with the slide, the original, and the new wording. `--changes` also saves that list as a CSV file.

**It converts the remediation already in the deck; it does not do the remediation.** Descriptions come from the alt text, what is skipped comes from the decorative flags, and the order comes from the deck's reading order. A deck with no remediation produces a document with `Figure. [No description]` in place of every picture.

### Settings

The converter's defaults are one course's preferences for the companion document, described in [The Word companion](../guide/word-companion.md#formatting-choices). Each can be changed or turned off:

| Setting | Default |
|---|---|
| `SLIDE_HEADINGS`, `BUILD_RANGES` | A heading for every slide, "Slide 37: " and the title as on the slide; one heading for a build that only adds to the slide before, "Slides 37 to 40: " |
| `REAL_BULLETS` | Bullets as real Word bulleted lists, nested as on the slide |
| `NUMBER_RULE`, `NUMBER_WORD_HYPHENS` | Numbers of 1,000 or more outside code: "140 thousand" when round, words when exact, digits without the comma for decimals and table cells; years and page numbers left as digits |
| `R_OUTPUT_TABLES` | R output that prints as a table (`summary()` coefficients, `aov()`, `anova()`, lavaan estimates, named vectors) as a real Word table |
| `SUPERSCRIPTS_AS_WORDS`, `SUBSCRIPTS_AS_WORDS`, `TIMES_AS_WORD` | "R-squared", "beta sub k", and "times" in prose |
| `COLONS_TO_COMMAS`, `QUOTES` | Quote marks removed from text; colons in sentences become commas |
| `CODE_LANGUAGE` | Code marked "Begin R code block." and "End R code block." |
| `AGENDA_RE` | Slides titled "Today's agenda" mark the document's sections |
| `LANGUAGE`, `BODY_FONT`, `CODE_FONT` | en-US; Times New Roman and Consolas |

Each is described in the "Settings you may want to change" block at the top of `pptx2notes.py`. There is no settings file yet; the instructor edits the values in the script.

## Known limits

- **English only.** The rules that rejoin sentence fragments, and the equation readings, use English word lists.
- **Built around one course.** The heuristics come from one instructor's decks: decks authored in Keynote, exported to .pptx, re-saved in PowerPoint (which Keynote's equations need) and remediated in PowerPoint. Decks from other sources may surface cases the scripts don't handle. The review list is there to catch them.
- **Tested** with Python 3.10.12, python-pptx 1.0.2, python-docx 1.2.0, lxml 6.1.3, and pikepdf 10.13.0.post1.

## How these were developed

See [How this was developed](../README.md#how-this-was-developed) in the main README.
