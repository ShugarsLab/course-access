# The Word companion

A text-only Word document built from a remediated slide deck and posted beside its PDF. It reads like lecture notes: the slides' text in reading order, each figure replaced by its description, and equations kept as live Word equations. The PDF is made accessible for everyone; the companion is designed for listening. Students choose the format that works for them.

## Why a companion

**What is written into a deck isn't always what is heard** ([P2](principles.md#p2)). In our testing, NVDA in PowerPoint skipped the descriptions on grouped figures, shapes, and equations, while in Word, equations could be read and explored piece by piece with a math add-on such as MathCAT ([Test results](../testing/README.md)).

A screen reader also handles a long Word document well: a listener can jump between headings, count the items in a list, and read a table with its headers. So the companion carries everything the deck says, in the form that reaches a listener most reliably.

**The companion is in addition to an accessible PDF, not instead of one.** Every file we post is made accessible, and each is designed for different readers. Under the federal rule, a separate accessible version is allowed only where the original can't be made accessible, so the PDF is remediated too ([What every posted file needs](pipeline.md#what-every-posted-file-needs)).

**Evidence:** found in testing ([NVDA with PowerPoint](../testing/README.md#nvda-with-powerpoint); [NVDA with Word](../testing/README.md#nvda-with-word); October 2026).

## What goes in it

- Slide text in reading order, with decorative objects skipped, and content repeated from the previous slide dropped, so a build contributes only what it adds.
- Each figure as its description, in place.
- Equations as live Word equations, which a screen reader with a math add-on can read and step through ([E1](equations.md#e1)). A symbol or two inside a sentence becomes words, since Word announces the start of every equation ([E19](equations.md#e19)), and the pairing of a symbol with its name has to be in the text ([E20](equations.md#e20)).
- Code marked where it begins and ends, with straight quotes, so it runs when pasted.
- Tables as real tables, with a repeating header row.
- Narration on arrows, joined to the sentence it leads into.
- A document title and a language, like every other posted file, so a screen reader announces the title rather than the file name and reads in the right voice. In Word, the title is under File › Info › Properties (Windows) or File › Properties › Summary (Mac); the language is under Review › Language › Set Proofing Language, with all the text selected. `pptx2notes.py` sets both.

## Formatting choices

Beyond that list, the companion's format is a matter of house style. These are our course's preferences; [P7](principles.md#p7) explains why slide numbers and real bullets matter:

- every slide gets a numbered heading ("Slide 37:" plus its title, repeated titles included), matching the PDF's page numbers;
- lists use real bullets, and numbered steps stay numbered;
- R output that is a table becomes a real table;
- no quote marks, and large numbers written so a screen reader doesn't voice their commas;
- paragraph spacing in place of blank lines, which a screen reader announces as "blank".

These are offered as settings, not rules: another course, or another listener, may choose differently. Our choices and their reasons are in the worked house style, [The companion document](house-style-example.md#the-companion-document); the questions to decide are in the template, [The companion document](house-style-template.md#the-companion-document).

## Building it

**By hand.** Copy the slide text into Word in reading order, replacing each figure with its description and retyping equations with Word's equation tool (Insert › Equation). Use Word's heading styles for slide titles, so a listener can move between them.

**With the scripts.** `pptx2notes.py` builds the companion from the deck, with the formatting choices above as its default settings, and keeps a generated copy beside the instructor's edited one. It prints a review list (figures without descriptions, equations it rebuilt, anything else to check by hand) and every number and symbol it rewrote for listening, with where it was and what it became. It converts the remediation already in the deck; it does not do the remediation. See the [tools](../tools/README.md).

**With an AI assistant.**

| Assistant | Instructor |
|---|---|
| Runs the converter; fixes what the review list flags; lists every number it rewrote | Reviews the companion; edits wording |
| Removes comments and tracked changes from the copy that will be posted | Posts it |

## Checking it

- **Build it last,** from the finished deck, so it carries every fix ([Slides: Ship](slides.md#ship)).
- **Listen to part of it** with a screen reader, especially the equations and any tables.
- **Keep the generated copy and the edited copy apart.** Once the companion has been edited by hand, regenerating over it loses the edits; compare the two instead.
- **After posting, a fix goes into every output:** the deck, a fresh PDF, and the companion ([After posting](slides.md#after-posting)).

**Evidence:** our practice.
