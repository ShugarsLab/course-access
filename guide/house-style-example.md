# House style: a worked example

This is the house style from our graduate quantitative methods course, filled in from [house-style-template.md](house-style-template.md). It is **one course's set of choices, not a set of defaults.** Some items are there because of the subject (statistics, taught in R), some because of what we learned listening with a screen reader, and some are our preference. Each item says which, using the labels in [Where each rule comes from](README.md#where-each-rule-comes-from).

Items marked **(course preference)** are this course's preferences. In the converter they are settings, not rules: other courses and other listeners may prefer otherwise.

It applies to everything written for students: alt text, figure and equation descriptions, text transcribed onto slides, the companion Word document, and alt text in R Markdown.

*Which of these we would recommend to other instructors, and which are this course's own choices, is still being decided; items marked (course preference) are the clearest examples of the second.*

---

## Language

- **American spelling.** color, gray, labeled, centered, recognizable. *Our choice.*
- **Normal distribution, never bell curve.** Likewise normally distributed and a roughly normal distribution; never bell-shaped, and never bell as a paraphrase of the shape (not a single-peaked normal distribution, rather than not one bell). The course teaches the term, and an informal synonym teaches a different vocabulary to the student who only hears the description. *Our choice.*
- **A stylized example,** not made-up, for illustration data invented for a figure. *Inferred from edits, then confirmed.*
- **Functional terms for assistive technology and its users:** screen-reader user, listener; for a specific person, their own preference. *Our choice.*

## Punctuation and symbols

- **Quote marks: keep to a minimum.** None in the companion Word document (removed when it is built). Write new descriptions without them where a plain phrase works: a red distribution labeled Pre, rather than the red "Pre" distribution. Apostrophes are unaffected. Where quotes remain, match the surrounding document. *Our choice; found in testing ([NVDA with PowerPoint](../testing/README.md#nvda-with-powerpoint), October 2026).*
- **Quotes inside R code are straight,** on slides too, so code runs when pasted. *Our choice.*
- **Spell out symbols in alt text; take the safest screen-reader reading every time.**
  - plus or minus, not ±
  - negative 3, not −3 or -3 (a hyphen can be read as dash, and the minus sign is skipped at some punctuation settings)
  - times or to the negative 8, never a bare x or ^
  - equals, percent, less than
  - r equals negative 0.7, not r = negative 0.7
  - the probability of squirrels is 0.31, not P(squirrels) = .31 (a leading decimal point can be dropped, and function parentheses are not read)

  Screen readers usually announce these glyphs, but whether they do depends on the program and its punctuation level, so words win. *Our choice.*
- **Numbers of 1,000 or more have no thousands commas in text outside code** *(course preference)*. A screen reader may read 140,000 as 140 comma 000.
  - Round or approximate numbers take a word for the magnitude: 140 thousand, about 1.2 million.
  - Exact whole numbers are written out in words, without *and*: two thousand four hundred thirteen houses. Some voices read a four-digit number like a year, and *and* can sound like a decimal is coming.
  - Exact numbers with decimals, and table cells, are digits without the comma: 15784.332, 215000.
  - Applies to the companion document's prose, figure descriptions and alt text, and worksheet text outside code. Not to code, R output, tables made from R output, or equations. Visible slide text keeps its commas for sighted readers; the companion document converts it. Years and numbers under 1,000 are unaffected.

  *Our choice; from a listener's feedback (long numbers were hard to follow).* Every number changed this way is listed for the instructor to check.
- **Greek letters in slide text need no spelled-out name.** NVDA read inline μ, σ, and α correctly, so alpha (α) on first use isn't needed in slide text. In alt text, the name is still used, per the previous rule. *Found in testing ([NVDA with PowerPoint](../testing/README.md#nvda-with-powerpoint), October 2026).*

## Notation and naming

- **Type I and Type II in the confusion matrix;** Type 1 and Type 2 elsewhere are left as written. The Roman form supports a visual mnemonic (the strokes in P and N), which the course pairs with a second, non-visual one. *Our choice.*
- **Words, not math, in figure descriptions and narration:** mu bar, sigma squared, not an inline equation. Equations themselves stay live math in the companion document. *Our choice.*
- **Degrees of freedom in words,** not df, in prose and descriptions. *Our choice.*
- **Letter case:** where both cases of a letter appear together, say capital N and lowercase n every time. *Our choice.*

## Code and output

- **R output keeps `[1]`.** When a code screenshot becomes text, console prompts (`>`, `+`) and knitr's `##` are dropped. *Our choice.*
- **What is stripped is logged.** When a code screenshot becomes text, whatever is dropped is recorded slide by slide beside the verbatim original, so it can be checked or put back. *Our choice.*
- **R code is marked.** Each block of R code or output starts with a paragraph, Begin R code block., in the Code style. When plain text follows, a paragraph, End R code block., closes it; no end marker is needed when a figure, an equation, a heading, or a table follows. *Our choice.* *(course preference)*
- **R output that is a table becomes a real table** (summary coefficients, anova tables, model estimates, named vectors), with a lead-in line, R output as a table, before it. Significance stars get their own column, and a column like Pr(>|t|) is headed p-value. The slides keep R's printed form. *Our choice.* *(course preference)*

## The companion document

These are the companion Word document's formatting choices. All are **(course preference)**.

- **Every slide gets a numbered heading.** Slide 37: followed by the slide's title exactly as it appears on the slide, so the companion and the slides say the same thing. Repeated titles get a heading each. A build that adds to one slide gets one heading with a range, Slides 37 to 40. Section headings sit above them, and slide numbers are the posted PDF's page numbers. A listener can jump between headings, and can talk about point 3 on slide 37 with classmates. Keep slide titles short: each is heard once per slide. *Our choice; from a listener's feedback. Replaces an earlier choice of no slide numbers.*
- **No short inline equations.** A symbol or two inside a sentence (mu, beta sub 1, alpha, y hat, alpha = 0.05) is written as words, because Word announces the start of each equation, which helps for a full equation and gets in the way for a character or two. Full equations stay live math. Slide text is unaffected. *Our choice; from a listener's feedback, after listening to a companion document together.*
- **Real bulleted lists,** nested as on the slide, so a listener hears how many items are coming. Numbered steps stay numbered lists. *Our choice; from a listener's feedback. Replaces an earlier choice of indents.*
- **Paragraph spacing, not blank lines.** NVDA announces an empty paragraph as blank, so space after code blocks and tables is paragraph spacing (12 pt). An empty paragraph stays only between two tables, where Word needs one. *Our choice; found in testing ([NVDA with Word](../testing/README.md#nvda-with-word), October 2026).*
- **Subscripted symbols and the times sign are words in prose:** beta sub 3, x sub k, a times b, not a × b, matching how equations are read, because a subscript is not reliably announced. A Greek letter with no subscript stays a symbol. Tables and code are unchanged. *Our choice.*

## Visual conventions

- **Table palette, all text centered:**

  | Element | Fill | Text |
  |---|---|---|
  | Column headers | light blue #D6EAF8 | black |
  | Row headers | light peach #FBE3D6 | black |
  | Total row and column | light gray #F2F2F2, bold | black |
  | Body | white | black |
  | Cells already determined in a worked example | mid-gray #BFBFBF | black |

  The header row (and column, where there is one) is always marked as a header. Color is never the only signal. *Our choice.*
- **Name a meme's source where possible,** then say what it stands for, in the teaching voice. The source is part of the reference. *Our choice.*

## Open

- **Punctuation and notation in slide text and alt text.** NVDA voices parentheses, quote marks, and colons, and did not read a superscript 2 as squared (found in testing, [NVDA with PowerPoint](../testing/README.md#nvda-with-powerpoint), October 2026). Our view: minimize them, but don't avoid them altogether; writing squared instead of a superscript 2 helps a listener and costs sighted students the notation.
- **Case on first mentions of common notation** (Pearson's r; lowercase mu): possibly worth stating for a listener learning the notation, even where the other case never appears.
- **The minus sign in the companion document's text and tables:** a true minus sign may be skipped at some punctuation settings, which would turn negative 0.307 into 0.307. Waiting on a listening test.
- **Alt text length:** awareness only. Some formats may cut off alt text beyond about 250 characters; our descriptions of new chart types run to about 280, and the companion document has no limit.
