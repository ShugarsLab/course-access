# Equations

This chapter covers how to make the equations in lecture slides, and briefly in R Markdown documents, reach a student who uses a screen reader: where equations are read and where they are not, how to write a spoken reading, and what to do with equations that sit inside figures or sentences.

Short version:

- **In PowerPoint itself, a screen reader may say nothing useful about an equation.** In our testing, NVDA read neither PowerPoint's equations nor the alt text written on them.
- **Word reads equations well.** Native Word equations can be read and explored piece by piece with a math add-on. A text-only Word companion to each deck, with the equations kept as live equations, is the most reliable way to get equations to a listener.
- **Don't add alt text to PowerPoint's own equations.** PowerPoint's tagged PDF already gives each equation its own spoken reading. Alt text added on top made a listener hear the same equation up to four times. Where PowerPoint's reading is wrong, fix the equation itself.
- **Write a spoken reading where no native reading exists:** equations that exist only as pictures, equations in knitted R Markdown PDFs, and figure descriptions that quote an equation. Write it as you would say it aloud, with every symbol spelled out and no brackets.
- **An equation that is part of a figure gets no reading of its own.** The figure's description covers it.

This chapter is the detailed reference. Most readers should start with the [principles](principles.md) (P2 and P9 cover equations) and come here when a question comes up. Rules are numbered E1, E2, … so they can be cited. *The numbering is provisional until the first formal release, while the order is still being reviewed; from then on, numbers won't change.* Rules from one course's practice are a starting point, not a standard. The instructor's own house style decides the details ([house-style-template.md](house-style-template.md)).

### How to read each rule

Each rule gives the rule itself, the reason, and an **Evidence** line saying where it comes from, using the labels in [Where each rule comes from](README.md#where-each-rule-comes-from).

## Rule index

| ID | Rule | Section |
|---|---|---|
| [E1](#e1) | Post a Word companion with live equations | Getting equations to a listener |
| [E2](#e2) | Leave PowerPoint's own equations without alt text | Getting equations to a listener |
| [E3](#e3) | Fix a bad reading in the equation itself | Getting equations to a listener |
| [E4](#e4) | Review the readings after export | Getting equations to a listener |
| [E5](#e5) | Never Autotag a PDF that PowerPoint has tagged | Getting equations to a listener |
| [E6](#e6) | Read it aloud before saving it | Writing a spoken reading |
| [E7](#e7) | Spell out every symbol and operation | Writing a spoken reading |
| [E8](#e8) | Read fractions and roots by length | Writing a spoken reading |
| [E9](#e9) | No brackets: say the quantity, and end the group with a comma | Writing a spoken reading |
| [E10](#e10) | Say subscripts and powers, and always say accents | Writing a spoken reading |
| [E11](#e11) | Say the case when both cases of a letter appear | Writing a spoken reading |
| [E12](#e12) | Introduce notation in stages | Writing a spoken reading |
| [E13](#e13) | Check every reading against the equation | Writing a spoken reading |
| [E14](#e14) | An equation inside a group gets no reading of its own | Equations inside figures and groups |
| [E15](#e15) | Leave annotated equations ungrouped | Equations inside figures and groups |
| [E16](#e16) | Group, or rebuild, equations built from separate pieces | Equations inside figures and groups |
| [E17](#e17) | Leave symbols in the sentence on the slide | Symbols inside sentences |
| [E18](#e18) | Type the Greek letter, not a look-alike | Symbols inside sentences |
| [E19](#e19) | In the Word companion, a lone symbol becomes words | The Word companion |
| [E20](#e20) | Put the name-and-symbol pairing in the companion's text | The Word companion |
| [E21](#e21) | Confirm that a checker counts equations | Tools and formats |
| [E22](#e22) | Re-save Keynote exports in PowerPoint before remediating | Tools and formats |
| [E23](#e23) | Convert pictures of equations to real equations | Tools and formats |

---

## Where an equation reaches a listener

What a listener hears depends on the file, so the rules below start from these findings.

### In PowerPoint: often nowhere

PowerPoint stores an equation as live math plus a hidden picture of the same equation for programs that can't display the math. Neither carries a text alternative unless one is written. A screen reader can try to interpret the math, or fall back to the picture, which has no label.

In our testing, **NVDA read neither the equation nor alt text written on it** in PowerPoint. NVDA's documented math support covers native equations in Word and equations made with MathType, not PowerPoint's own equations.

**Evidence:** found in testing ([NVDA with PowerPoint](../testing/README.md#nvda-with-powerpoint), October 2026). Other screen readers were not tested.

### In Word: yes, and explorable

Native Word equations are read by NVDA with a math add-on such as [MathCAT](https://github.com/NSoiffer/MathCAT), and the listener can move through an equation piece by piece (term, numerator, subscript) instead of hearing it once at speed. STEM accessibility specialists often provide math-heavy content in Word for this reason.

**Evidence:** found in testing ([NVDA with Word](../testing/README.md#nvda-with-word), October 2026).

### In the PDF: read once, unless alt text is added

A PDF exported from PowerPoint with accessibility tagging on gives every equation a formula tag that carries **PowerPoint's own spoken reading** and the math itself as MathML. It does this whether or not anyone wrote alt text.

- **Alt text on top of it repeats the equation.** When the equation also has authored alt text, PowerPoint adds a second tag holding the authored reading followed by PowerPoint's reading again. Listening to such a PDF, we heard one equation up to four times. An equation with no authored alt text was read once.
- **PowerPoint's readings have defects of their own:** a function name spelled out letter by letter ("l o g sub e"), stray punctuation ("a. times b"), and "start equation mu" for a lone symbol in a sentence. These are fixed at the source (E3), not with alt text.
- **Equations inside a described figure** still get their own formula tags, read after the figure's description. This can't be fixed from the slides.
- **Acrobat's automatic readings can lose content.** On one deck, Acrobat read a long fraction as "numerator, 1 plus 1 plus 1 plus 3 … end numerator" and stopped: the denominator, the equals sign, and the result were missing. This matters for PDFs tagged by Acrobat rather than exported from PowerPoint, such as knitted R Markdown PDFs.

| Equation | Acrobat's automatic reading | Verdict |
|---|---|---|
| x ∈ S (a short expression) | "start equation element of" | awkward, no close |
| = 1/6 | "equals 1 sixth" | correct |
| (1 + 1 + 1 + 3 + 4 + 8 + 9 + 14) / 146 = 41 / 146 | "numerator, 1 plus 1 plus … 14 end numerator" | denominator and result lost |

**Evidence:** found in testing ([VoiceOver with Preview](../testing/README.md#voiceover-with-preview-on-a-pdf-exported-from-powerpoint), October 2026), and by inspecting the exported PDF's tags; Acrobat's readings found by [inspecting exported PDFs](../testing/README.md#found-by-inspecting-files).

---

## Getting equations to a listener

<a id="e1"></a>

### E1. Post a Word companion with live equations

**Post a text-only Word companion for each deck alongside the PDF.** Each equation is copied into it as a live Word equation on its own line, which a listener can hear and explore with a math add-on. Word and PowerPoint use the same equation format, so nothing has to be retyped. The companion is built from the remediated slides (`tools/pptx2notes.py` does this automatically); see [The Word companion](word-companion.md).

**Evidence:** found in testing ([NVDA with PowerPoint](../testing/README.md#nvda-with-powerpoint) and [NVDA with Word](../testing/README.md#nvda-with-word), October 2026); our practice.

<a id="e2"></a>

### E2. Leave PowerPoint's own equations without alt text

**Equations made with PowerPoint's equation tool get no alt text.** We used to write a spoken reading as alt text for every standalone equation. After listening to the PDF, we stopped: PowerPoint already supplies a reading, and ours only repeated it. Remove alt text from equations carried over from older slides before exporting the PDF.

This applies only to PowerPoint's own equations. Equations with no native reading still need one written (E6 to E13).

**Evidence:** found in testing ([VoiceOver with Preview](../testing/README.md#voiceover-with-preview-on-a-pdf-exported-from-powerpoint), October 2026); our practice since.

<a id="e3"></a>

### E3. Fix a bad reading in the equation itself

Where PowerPoint's reading is wrong, change how the equation is built:

- Build a function name such as log with the Equation tab's Function structure, so it is read as a word, not letter by letter.
- Set words inside an equation ("total effect") as normal text.
- Type a lone symbol in a sentence as plain text rather than as a one-character equation (E17).
- Check how letters were entered where a reading inserts stray punctuation.

**Evidence:** found in testing ([VoiceOver with Preview](../testing/README.md#voiceover-with-preview-on-a-pdf-exported-from-powerpoint), October 2026); our practice since.

<a id="e4"></a>

### E4. Review the readings after export

List each equation's reading from the exported PDF and read them through once. A script for this is planned for `tools/`; until then, a PDF checker that shows tag contents, or listening, does the job.

PowerPoint writes equation letters in a special mathematical alphabet (a mathematical italic μ, not the ordinary Greek μ). Screen readers cover that alphabet less consistently, so listen for how such letters are read.

**Evidence:** our practice.

<a id="e5"></a>

### E5. Never Autotag a PDF that PowerPoint has tagged

Acrobat's automatic tagging discards PowerPoint's tags, including every equation's reading, and its own readings can drop part of an equation (see the table above). Run it only on a PDF that has no usable tags, such as a knitted R Markdown PDF, and then check its equations.

**Evidence:** found by inspecting files (exported PDFs; [Test results](../testing/README.md#found-by-inspecting-files)).

---

## Writing a spoken reading

Write a reading where an equation has no native reading: an equation that exists only as a picture, an equation in a knitted R Markdown PDF (automatic tagging marks these as figures with no reading), and any figure description or narration that quotes an equation. The rules also help when judging PowerPoint's own readings.

The text is read out exactly as written. A screen reader does not interpret it as math, so it has to be in spoken form already. Readings are student-facing text like any other, so the course's [house style](house-style-template.md) applies to them too (spelling, preferred terms, quote marks).

<a id="e6"></a>

### E6. Read it aloud before saving it

Write the equation the way the instructor would say it in class, then read the text aloud. If it would confuse someone hearing it once, rewrite it.

**Evidence:** our practice.

<a id="e7"></a>

### E7. Spell out every symbol and operation

Never leave a glyph for the screen reader to interpret. Whether a screen reader announces a symbol depends on the program and its punctuation settings, so words are the safe choice.

| Instead of | Write |
|---|---|
| − (subtraction) | minus |
| −3 | negative 3 (a hyphen can be read as "dash," and the true minus sign is skipped at some settings) |
| ± | plus or minus |
| ≠ | not equal to |
| × or implied multiplication | times |
| x², 10⁻⁸ | x squared, 10 to the negative 8 |
| = | equals |
| % | percent |
| P(A) = .31 | the probability of A is 0.31 (a leading decimal point can be dropped, and function parentheses aren't read) |

The same applies to numbers quoted in figure descriptions: "r equals negative 0.7," "31 percent" ([F22](describing-figures.md#f22)).

**Evidence:** our practice; the punctuation problems were found in testing ([NVDA with PowerPoint](../testing/README.md#nvda-with-powerpoint), October 2026: parentheses, quote marks, and colons were voiced, and a superscript 2 was not read as "squared").

<a id="e8"></a>

### E8. Read fractions and roots by length

- **Short:** read it as a division. "sigma divided by the square root of n."
- **Long or nested:** "a fraction where the numerator is … and the denominator is …." This marks where the fraction starts and stops without a closing phrase.

> Z = ((μ̄ − μ)√n) / σ
>
> "Z equals a fraction where the numerator is the quantity mu bar minus mu, times the square root of n, and the denominator is sigma."

Say "end of the square root" only when nothing else shows where the root stops, as when a root over several terms is followed by more of the expression. Closing every fraction and root this way was too wordy.

**Evidence:** our practice.

<a id="e9"></a>

### E9. No brackets: say the quantity, and end the group with a comma

Parentheses read badly ("left paren … right paren"). Introduce a group with "the quantity" and end it with a comma:

> (vᵢ − μ)² → "the quantity v sub i minus mu, squared"

This still distinguishes it from vᵢ − μ² ("v sub i minus mu squared"). Leave out "the quantity" when the group already opens with its own lead-in word, such as "the sum of" or "a fraction where."

Spoken math styles that use explicit lead-in and closing words, such as ClearSpeak, follow the same principle (Frankel, L., Brownstein, B., Soiffer, N., & Hansen, E. G. (2016). *Development and initial evaluation of the ClearSpeak style for automated speaking of algebra* (ETS Research Report No. RR-16-23). [doi:10.1002/ets2.12103](https://doi.org/10.1002/ets2.12103)).

**Evidence:** our practice; adopted after reviewing a full week's readings written this way.

<a id="e10"></a>

### E10. Say subscripts and powers, and always say accents

- Subscripts: "v sub i," "beta sub 1."
- Powers: "squared," "cubed," "to the power k."
- **Accents change the meaning, so always say them:** "mu bar," "y hat," "x tilde." In a course where μ̄ is the sample mean and μ the population mean, a reading that drops the bar says the wrong thing.

**Evidence:** our practice. We found the accent problem in review: an automatic reader had been dropping bars and hats, so the sample mean was read as the population mean.

<a id="e11"></a>

### E11. Say the case when both cases of a letter appear

Where capital and lowercase forms of the same letter appear together, say which is which every time: "capital N samples of lowercase n observations." Where context keeps them apart, leave it alone.

**Evidence:** our practice. Open: whether to state the case on the first few mentions of common notation (Pearson's r, mu) even when only one case appears.

<a id="e12"></a>

### E12. Introduce notation in stages

A sighted student sees a symbol and its definition together on the slide. A listener needs the pairing spoken, and then needs to learn the symbol, not to be reminded of it forever.

1. **Name only,** until the slides introduce the symbol: "the denominator is the standard error."
2. **Name and symbol together** at the introduction and for the next two or three *spoken* mentions: "the standard error, SE."
3. **Symbol alone** after that: "SE."

Count what is heard: a repeated slide marked decorative doesn't count; visible slide text that pairs the two does. Pair them again after a long stretch with no spoken mention, and at the first mention in each new deck. Use the same name for a symbol everywhere: equation readings, figure descriptions, and any narration written for the listener.

**Evidence:** inferred from edits, then confirmed. The figures chapter applies the same rule to descriptions ([F21](describing-figures.md#f21)).

<a id="e13"></a>

### E13. Check every reading against the equation

This applies to readings carried over from earlier materials and to readings drafted automatically: `tools/mathspeech.py` drafts readings from PowerPoint equations following the rules above, for figure descriptions that quote an equation and for checking PowerPoint's own readings. The instructor reviews every one.

Look for a literal "/", a digit right after ")" or a letter with no "squared" or "to the" before it, and any untranslated symbol. Then compare the reading against the equation itself. A reading that sounds smooth but puts the end of a root or fraction in the wrong place is worse than an awkward one that is correct.

**Evidence:** our practice.

---

## Equations inside figures and groups

<a id="e14"></a>

### E14. An equation inside a group gets no reading of its own

When an equation is part of something larger, the larger thing's description carries it:

- symbols labeling parts of a chart (μ on one line, μ̄ on another);
- an equation built by hand from several pieces and grouped (E16);
- a group that contains math, which PowerPoint stores as a single equation object.

Describe the group like any other figure, and use the equation's spoken reading as raw material. Readings on the pieces as well would make the listener hear the same math twice.

**Evidence:** our practice. In PowerPoint, NVDA read neither group alt text nor the pieces' equation text (found in testing, [NVDA with PowerPoint](../testing/README.md#nvda-with-powerpoint), October 2026), so in practice the description reaches the listener through the Word companion and the PDF. In the PDF, the equations inside a group are also read after the description (found in testing, VoiceOver with Preview, October 2026); this can't be prevented from the slides.

<a id="e15"></a>

### E15. Leave annotated equations ungrouped

An equation with labels and arrows pointing at its terms ("this is the intercept") is **not** grouped. The equation stays a live equation, read by PowerPoint's own reading in the PDF and as math in the Word companion. The labels stay readable text, and the arrows can carry short narration that leads into the label they point at ([F24](describing-figures.md#f24)).

**Evidence:** our practice.

<a id="e16"></a>

### E16. Group, or rebuild, equations built from separate pieces

Some equations are assembled from separate objects: a fraction bar drawn as a line with text boxes above and below it, or pieces placed side by side so that parts can be colored differently. A screen reader meets these as scattered fragments, such as a dangling "=" or a numerator with no denominator.

- **Group the pieces** and describe the group as one equation.
- Where possible, **rebuild it as one live equation**, keeping any colors. It then reads as math in the Word companion. `tools/pptx2notes.py` rebuilds two common hand-built shapes automatically (a drawn fraction, and rows of equations with small pictures in the gaps) and lists each one for checking.

**Evidence:** our practice.

---

## Symbols inside sentences

A sentence such as "If μ̄ is more than 2 SE from μ, reject the null" can't carry alt text for its symbols. Alt text belongs to a whole object, and a reading on the text box would replace the whole sentence.

<a id="e17"></a>

### E17. Leave symbols in the sentence on the slide

In the slides, leave the symbols in the sentence. In our testing NVDA read Greek letters typed as ordinary text correctly, so "alpha (α)" on first use is not needed for the screen reader's sake. (It may still be good teaching; see E12.)

**Evidence:** found in testing ([NVDA with PowerPoint](../testing/README.md#nvda-with-powerpoint), October 2026).

<a id="e18"></a>

### E18. Type the Greek letter, not a look-alike

A mu typed on a Mac with Option-M is the micro sign, which NVDA's symbol list reads as "micro." Use the Greek letter μ, for example from the Symbol menu or an equation.

**Evidence:** published documentation (NVDA's symbol list); not yet checked by ear.

---

## The Word companion

The companion document carries the equations themselves, not their readings. Standalone equations are live Word equations on their own line, which the listener hears through the math add-on and can explore. A group of pure equation pieces becomes one live equation; a group with words or drawn parts stays a figure description.

<a id="e19"></a>

### E19. In the Word companion, a lone symbol becomes words

A symbol or two inside a sentence (mu, beta sub 1, alpha = 0.05) becomes words in the companion. Word stores even one symbol as an equation and announces "begin equation" each time, which helps for a full equation and gets in the way for a single letter. Full equations stay live math.

**Evidence:** found in testing ([NVDA with Word](../testing/README.md#nvda-with-word), October 2026).

<a id="e20"></a>

### E20. Put the name-and-symbol pairing in the companion's text

Readings written as alt text don't reach the companion, so the pairing from E12 has to be in the companion's text (slide text, a symbol key such as "n means sample size", or a figure description) before the first equation that uses the symbol alone.

**Evidence:** our practice; found in testing ([NVDA with Word](../testing/README.md#nvda-with-word), October 2026).

---

## Tools and formats

<a id="e21"></a>

### E21. Confirm that a checker counts equations

Many automated checkers never look at PowerPoint equations. The equation sits inside an "alternate content" wrapper that common software libraries skip, so a checker can report every object as handled while ignoring every equation. When auditing a deck, confirm the checker counts equations. `tools/` includes one that does.

**Evidence:** our practice; found by inspecting files (our own decks).

<a id="e22"></a>

### E22. Re-save Keynote exports in PowerPoint before remediating

Decks written in Keynote and exported to PowerPoint can carry equations in a form some tools cannot see until the file has been opened and re-saved in PowerPoint. A hat or bar can also come through drawn far above its letter. Re-save the export in PowerPoint before remediating, and check equations there rather than in other viewers.

**Evidence:** our practice.

<a id="e23"></a>

### E23. Convert pictures of equations to real equations

Scanned handouts, screenshots, and other people's slides may hold equations only as images. Convert them to real equations rather than describing them: math OCR tools such as MathPix can turn a PDF into editable math, which can then go into Word.

**Evidence:** our practice.

### R Markdown

How equations come through in knitted HTML and PDF, and how to fix them, is in [R Markdown worksheets](rmarkdown.md): [the HTML](rmarkdown.md#3-check-the-knitted-html) and [inline symbols in the PDF](rmarkdown.md#4d-fix-inline-symbols-a-screen-reader-would-misread). Display equations in a knitted PDF need written readings (E6 to E13).

---

## Untested or open

- **PowerPoint's PDF with other screen readers.** Settled for VoiceOver with Preview: no alt text on PowerPoint equations (E2). How NVDA or JAWS read the same PDF's formula tags is untested.
- **Equations inside described figures** are read again after the description in the PDF. Whether to accept that or work around it (for example, flattening the figure to a picture) is open.
- **Where an automatic draft can be trusted.** We treat one-symbol and flat equations (μ = 190) as safe to draft automatically and anything nested as needing a careful check. That line is a judgment, not a tested threshold.
- **Other screen readers.** Slides and Word were tested with NVDA; the PDF and R Markdown HTML with VoiceOver. JAWS was not tested.
- **R Markdown HTML equations with NVDA,** and whether inline math stays within the sentence when read straight through; the inline-symbol fix for knitted PDFs has not been heard by a screen reader.
- **Explaining what a symbol means.** A reading says "mu," not "mu, the population mean." Where meanings belong (the reading, the slide text, or a first-mention convention) is partly answered by E12 and not settled.

## Retired IDs

None yet. Until the first formal release, rules may still be reordered and renumbered. After it, a dropped rule's ID is listed here and never reused.
