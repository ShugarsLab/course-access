# House style template

A **house style** is the short list of choices about wording and notation that apply to everything written for students in a course: alt text, figure and equation descriptions, text transcribed onto slides, the companion document, alt text in R Markdown. It is where instructor- and course-specific preferences live, so the conventions about describing [figures](describing-figures.md) and [equations](equations.md) can stay about what to describe and why.

**Decide it up front, and apply it as descriptions are written.** We found that correcting style in review is expensive: in our first remediated lecture, a sixth of the draft descriptions needed a review round for nothing but spelling variants and one informal synonym. A list decided before drafting, kept beside the deck, removes that round.

**Keep it short and keep it current.** Record a choice when the instructor makes it, mark what is still undecided as open, and note where each rule came from (the instructor's choice, something learned in testing, a pattern noticed in edits; see [Where each rule comes from](README.md#where-each-rule-comes-from)), so a rule can be questioned later instead of being inherited by accident.

**Let it grow through the semester.** Deciding up front covers what you can anticipate; the rest shows up in your edits. A word you keep replacing, a kind of figure you keep describing the same way, a correction you make every week: each is a rule waiting to be written down. Set a regular point to look for these, such as after each week's materials are posted, and add what you find to the house style so the next week starts from it. Most of the rules in our [worked example](house-style-example.md) marked *inferred from edits, then confirmed* came about this way. If you work with an AI assistant, it can do the first pass: give it its drafts beside your final versions and ask it to propose rules from the patterns in your edits, for you to accept, change, or reject (see [Working with an AI assistant](../ai-assistant/README.md#how-to-use-them-planned)).

Copy this file, fill in the blanks, and delete the items that don't apply. For one course's filled-in version, see [house-style-example.md](house-style-example.md).

---

## Language

### Spelling variety

- **Question:** which variety of English (or other language) do descriptions use?
- **Options:** American; British; Canadian; Australian; other.
- **Where it matters:** consistency across a document; a screen reader pronounces variants identically, so this is about the written record and searchability.
- **Our choice:** ______

### Preferred terms and banned synonyms

- **Question:** which technical terms does the course teach, and which informal synonyms should descriptions avoid?
- **Options:** list each term with the synonyms not to use (for example: normal distribution, not bell curve).
- **Where it matters:** a student who only hears descriptions learns the vocabulary the descriptions use. An informal synonym teaches a different vocabulary to that one student.
- **Our choice:**

  | Use | Not |
  |---|---|
  | ______ | ______ |

### Terms for disability and assistive technology

- **Question:** how do course materials refer to students who use assistive technology?
- **Options:** functional terms (screen-reader user, listener); identity-first (blind students); person-first (students with visual impairments). Preferences vary by community and by person.
- **Where it matters:** instructions and notes for students; follow an individual's own preference when writing about them.
- **Our choice:** ______

---

## Punctuation and symbols

### Quote marks

- **Question:** are quote marks used in descriptions and slide text, and which kind?
- **Options:** avoid where a plain phrase works; curly; straight; match the surrounding document.
- **Where it matters:** screen readers may announce quote marks aloud, depending on settings. Quotes inside code should stay straight so the code runs when pasted.
- **Our choice:** ______

### Symbols, signs, and numbers in alt text

- **Question:** are symbols written as glyphs (±, −3, =, %) or spelled out (plus or minus, negative 3, equals, percent)?
- **Options:** spell out everything; spell out only signs that are read unreliably; use glyphs.
- **Where it matters:** whether a screen reader announces a glyph depends on the program and its punctuation setting. A hyphen used as a minus sign may be read as dash, a leading decimal point may be dropped, and function parentheses (P(A)) may not be read.
- **Our choice:** ______

### Large numbers

- **Question:** how are numbers of 1,000 or more written in text meant for listening?
- **Options:** digits with commas; digits without commas; a word for the magnitude for round numbers (140 thousand); exact whole numbers in words; leave visible slide text as it is and convert only the companion document and alt text.
- **Where it matters:** depending on its punctuation setting, a screen reader may read 140,000 as 140 comma 000, and some voices read a four-digit number like a year. Code, program output, and equations should keep their digits.
- **Our choice:** ______

### Punctuation and notation in visible slide text

- **Question:** should slide text minimize parentheses, colons, superscripts, and similar notation for listeners?
- **Options:** minimize; avoid; leave as written.
- **Where it matters:** these are voiced or skipped by screen readers (a superscript 2 may not be read as squared), but writing everything in words costs sighted students the notation.
- **Our choice:** ______

### Greek letters and other symbols in slide text

- **Question:** do Greek letters in ordinary slide text need their names written beside them?
- **Options:** never; on first use; always.
- **Where it matters:** test with the screen readers students use; in our testing NVDA read inline Greek letters correctly.
- **Our choice:** ______

---

## Notation and naming

### Roman or Arabic numerals for named concepts

- **Question:** Type I error or Type 1 error (and similar)?
- **Options:** Roman throughout; Arabic throughout; Roman where a mnemonic depends on it.
- **Where it matters:** Roman numerals are the field's standard in some disciplines; Arabic numerals are unambiguous aloud. The two can't both be satisfied in the same text.
- **Our choice:** ______

### Words or math in figure descriptions

- **Question:** inside a description, is a quantity written as words (mu bar, sigma squared) or as math?
- **Options:** words; math; words for single symbols, math for longer expressions.
- **Where it matters:** alt text can't hold live math; words are read reliably.
- **Our choice:** ______

### Abbreviations and units

- **Question:** which abbreviations are written in full (degrees of freedom, not df; standard deviation, not SD), and how are units written?
- **Where it matters:** abbreviations are read letter by letter or mispronounced; a listener can't see that df is an abbreviation.
- **Our choice:** ______

### Letter case

- **Question:** when do descriptions say capital or lowercase?
- **Options:** whenever both cases of a letter appear together; on first mentions; never.
- **Where it matters:** N and n, or X and x, often mean different things and sound identical.
- **Our choice:** ______

---

## Code and output

### Code shown on slides

- **Question:** what happens to console prompts and output markers when a code screenshot becomes text?
- **Options:** keep exactly; drop prompts (`>`, `+`) and knitr's `##`; keep R's `[1]` index or drop it.
- **Where it matters:** stripped characters change what is pasted and run; keeping a record of what was dropped lets someone check or restore it.
- **Our choice:** ______

### Code in the companion document

- **Question:** how is a listener told where code begins and ends?
- **Options:** spoken markers (Begin R code block. / End R code block.); a heading; a code style only.
- **Where it matters:** a monospace style is invisible to a listener.
- **Our choice:** ______

### Program output that is a table

- **Question:** in the companion document, does output that prints as a table (regression coefficients, ANOVA tables, model estimates) stay as code text, or become a real table?
- **Options:** keep it as code; make it a real table, with a lead-in line saying so; both.
- **Where it matters:** a screen reader reads printed output line by line, with the columns run together; a real table can be read cell by cell with its headers.
- **Our choice:** ______

---

## The companion document

### Slide numbers and headings

- **Question:** does each slide get a heading in the companion document, and does it carry the slide number?
- **Options:** a heading for every slide, with its number and title (Slide 37: …); headings only where the title changes; headings only at section breaks; one heading for a run of build slides (Slides 37 to 40).
- **Where it matters:** headings are how a screen-reader user moves through a long document. Slide numbers let a listener talk about the same slide as classmates, but if the deck taught from has slides the posted files don't, the numbers drift from what is on screen.
- **Our choice:** ______

### Inline equations

- **Question:** does a symbol or two inside a sentence (mu, alpha = 0.05) become a live equation or words?
- **Options:** words for short inline math, live equations for full equations; live equations everywhere.
- **Where it matters:** Word announces the start and end of each equation, which helps for a full equation and gets in the way for a single character.
- **Our choice:** ______

### Lists and bullets

- **Question:** are bullets kept, or turned into plain paragraphs or indents?
- **Options:** real bulleted lists, nested as on the slide; indents; plain paragraphs. Numbered steps as numbered lists either way.
- **Where it matters:** screen readers announce bullets and list levels, which some listeners find noisy; but real lists tell a listener how many items are coming and let them refer to a point by its place. Indents carry no structure a screen reader can report.
- **Our choice:** ______

### Spacing

- **Question:** how is space between blocks (after code, after tables) made?
- **Options:** paragraph spacing; empty paragraphs.
- **Where it matters:** some screen readers announce each empty paragraph as blank.
- **Our choice:** ______

### Symbols in the companion's prose

- **Question:** are subscripts, superscripts, and signs such as × written as words in the companion's sentences (beta sub 3, R-squared, a times b)?
- **Options:** words; symbols as on the slide.
- **Where it matters:** a subscript or superscript may not be announced, so beta sub 3 can be heard as beta 3, and R² as R 2.
- **Our choice:** ______

---

## Visual conventions

### Table palette and header flags

- **Question:** what colors and alignment do tables use, and are header rows and columns always marked as headers?
- **Where it matters:** headers marked as headers are announced with each cell; color must never be the only signal.
- **Our choice:**

  | Element | Fill | Text |
  |---|---|---|
  | Column headers | ______ | ______ |
  | Row headers | ______ | ______ |
  | Totals | ______ | ______ |

### Images from popular culture

- **Question:** when a slide uses a meme or a still from a film or show, does the description name its source?
- **Options:** name the source, then what it stands for; describe only what it stands for.
- **Where it matters:** the source is often part of the joke or the reference.
- **Our choice:** ______

---

## Open questions

List decisions not yet made, so no one treats them as settled:

- ______
