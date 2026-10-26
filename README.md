# course-access: Accessible teaching materials

**Draft. Shared for review.**

This repository aims to help instructors make their content more accessible. We focus specifically on making quantitative content—including equations, figures, and code—accessible to students using a screen reader. However, the included guidance and tools are developed more broadly for instructors working to meet the federal accessibility requirements for course materials at public colleges and universities (WCAG 2.1 Level A and AA, under the ADA Title II rule). Support for specific elements of WCAG is tracked in [WCAG coverage](guide/wcag-coverage.md).

This repository is designed to enable three possible implementation approaches:

- **By hand.** Everything in the [guide](guide/README.md) can be done manually, with no technical background: slides in PowerPoint and Word, and PDFs in Adobe Acrobat Pro. Materials for working with R and RStudio are also included.

- **With scripts.** The [tools](tools/README.md) speed up parts that are tedious to manually check or implement. Scripts can be run by anyone with Python 3.10 or later.

- **With an AI assistant.** Any AI tool that can read images can draft and check text, starting with figure descriptions, using the prompts in [Working with an AI assistant](ai-assistant/README.md). An assistant that can work on the files themselves can also carry out changes such as grouping and reading order, checked with the [tools](tools/README.md). Either way, the instructor makes the teaching decisions and reviews everything the assistant writes.

## Making learning accessible

Our pipeline aims to make every student-facing document accessible, but our broader goal is to ensure that every student has access to the ideas, information, and intellectual content of a course. With a focus on students who rely upon a screen reader, everything here starts from the question: _what does a student who is listening, rather than looking, need in order to learn?_

Most accessibility guidance assumes an audience that already knows a field. Teaching materials are inherently different: they teach the field, often a step at a time, to students meeting it for the first time. This leads to key pedagogical insights that drive our approach:

- **Viewing allows skimming, but listening is serial.** A sighted student sees what a build adds at a glance; a listening student hears everything again from the start. Repeated equations or visualizations can serve as a helpful quick reference for a sighted student, but add noise for a listening student who has to hold all relevant information in their head. Focus on what changed, and spare the listener repetitive content.

- **How much to say depends on the goal of the lesson.** Descriptions should focus on the ideas being communicated: a figure illustrating the shape of a distribution doesn't need the nuances of its data. When the goal is for students to discover patterns on their own, give them raw, explorable data, figures, and equations.

- **How much to say depends on how new the idea is.** The first time a type of chart appears, a listening student needs to learn how to read it. By the tenth chart of that kind, a sentence is enough.

- **Notation should be learned by ear first.** A symbol read aloud before it has been named is just a sound. Name the concept, then pair the name with its symbol, then use the symbol alone.

These are four of the [principles](guide/principles.md) behind the guide; each principle links to the detailed rules.

## What existing tools miss

We developed this pipeline in part because existing accessibility tools failed to adequately identify and address the needs of students who use a screen reader:

- **A filled-in alt-text field is not a description.** Many accessibility checkers count "image.jpg" as completed alt text. [`alt_audit.py`](tools/README.md#alt-text-audit) sorts real descriptions from file names and placeholder text.

- **Checkers often miss equations.** Many automated checkers never look at PowerPoint's equations, so a deck can pass every check with none of its equations checked. See [Equations](guide/equations.md), especially [E2](guide/equations.md#e2) and [E21](guide/equations.md#e21).

- **Hidden is not silent.** A table revealed one cell at a time, by covering cells with shapes, still holds every answer, and a screen reader reads them on every slide of the build, starting with the first. [`cells.py`](tools/README.md#covered-cells) finds and empties the covered cells.

- **What is written isn't always what is heard.** In our testing, raw PowerPoint slides and remediated PDFs didn't reliably deliver content to a screen reader ([test results](testing/README.md)). We recommend slides come with a text-only Word companion built for listening, beside a tagged PDF for everyone; see [The Word companion](guide/word-companion.md). [`pptx2notes.py`](tools/README.md#word-companion) builds one from a remediated deck.

## The pipeline

Whether done by hand, by scripts, or with an AI assistant, our remediation pipeline follows an ordered process in which the instructor makes every decision. We have developed related pipelines for [slides](guide/slides.md), [R Markdown](guide/rmarkdown.md), and [readings](guide/readings.md); the [pipeline overview](guide/pipeline.md) compares them. All pipelines share conventions for describing [figures](guide/describing-figures.md) and [equations](guide/equations.md), and draw from a [house style](guide/house-style-template.md) that can be customized for each course.

## What's here

| Folder | What | Status |
|---|---|---|
| [`guide/`](guide/) | Principles, the pipeline, house style, rules for figures and equations, WCAG coverage, and chapters for slides, the Word companion, R Markdown, and readings; all doable by hand | Draft |
| [`tools/`](tools/) | Python scripts: deck checks, a PDF tag audit, and the Word companion converter | Working; tested on one course's decks |
| [`ai-assistant/`](ai-assistant/) | Working with an AI assistant: what to give it, prompts for any AI chat tool, a rubric | Very preliminary: one prompt, tested once |
| [`students/`](students/) | Guides for students: working in R with a screen reader | Draft |
| [`testing/`](testing/) | What we found when we tested our materials (the evidence the guide's rules cite), and test kits to run with a screen reader | Two screen readers so far; one kit, partly tested |

Also at the top level: the [roadmap](ROADMAP.md), how to [contribute](CONTRIBUTING.md), and the [changelog](CHANGELOG.md).

**Start here:** the [principles](guide/principles.md), then the [guide](guide/README.md).

## Status and limits

**WCAG is the floor, not the goal.** A 2024 federal rule requires public institutions to meet WCAG 2.1 AA for course materials. The pipeline doesn't yet cover all of it, and the gaps are tracked in [WCAG coverage](guide/wcag-coverage.md). For students who use screen readers, though, it goes well beyond what WCAG asks. WCAG requires a text alternative for every figure, but not one that teaches. It requires headings and a meaningful reading order, but says nothing about a listener hearing the same chart six times across a build, or meeting a symbol before anyone has named it. Our conventions start from what a listening student needs in order to learn.

These materials come from one course, one semester, and testing with two screen readers (NVDA on Windows, VoiceOver on a Mac); the results are in [Test results](testing/README.md). Each rule in the guide says [where it comes from](guide/README.md#where-each-rule-comes-from): our practice, a pattern confirmed from our edits, a result found in testing (with the date and software), and so on. What has not been tested is listed as such. The readings pipeline rests on only a few articles, and our one prompt has been tested with one AI tool. Rule numbers (F1, E1, …) are provisional until the first formal release; from then on, changes are recorded in the [CHANGELOG](CHANGELOG.md). The scripts were written for decks exported from Keynote and PowerPoint and carry some of one course's habits; their README lists them.

## Feedback

This is a draft, shared so it can be improved. We would welcome:

- **Corrections:** anything wrong, unclear, or out of date, including menu paths in newer versions of the software.
- **What happened when you tried it,** on your own slides, worksheets, or readings, in another subject, or with other software.
- **Test results** from the [test kits](testing/kits/README.md), or from [trying an AI prompt](CONTRIBUTING.md#test-an-ai-prompt).
- **From screen-reader users:** what works for you and what doesn't. Anything you choose to share is welcome; nothing is expected.

**How:** open an issue on GitHub (there are templates for general feedback, test-kit results, and prompt test results), or email [sarah.shugars@rutgers.edu](mailto:sarah.shugars@rutgers.edu). [Contributing](CONTRIBUTING.md) has the details, including how to test a prompt and send results.

**Please don't share** anything about students (names, grades, accommodations, or their work), or material you don't have the right to share, such as figures from published papers.

## How this was developed

We developed the conventions and workflow while remediating our own course materials. Much of the code, and first drafts of many descriptions and of this documentation, were written with an AI assistant (Claude, by Anthropic). Much like our full pipeline, this repository was developed through a pedagogy-centered, instructor-led process, with AI assistance to make the tools scalable and replicable. Every rule here was decided by us, and every description used in the course was reviewed by the instructor.

## Authors

Sarah Shugars ([ORCID 0000-0002-1917-4313](https://orcid.org/0000-0002-1917-4313)) and Philip So, Rutgers University.

## Citing

Shugars, S., & So, P. (2026). *course-access: Accessible teaching materials* (Version 0.0.1) [Computer software]. GitHub. https://github.com/ShugarsLab/course-access

GitHub's "Cite this repository" button gives the same citation in other formats, from [CITATION.cff](CITATION.cff). A DOI will be added at the first formal release.

## License

Code: MIT ([LICENSE](LICENSE)). Guide and other documentation: CC BY 4.0 ([LICENSE-docs.md](LICENSE-docs.md)).

## Acknowledgements

We thank [Rutgers Access and Disability Resources (RADR)](https://radr.rutgers.edu) for their advice and for a listening session that shaped several of these conventions.
