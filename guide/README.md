# Guide for accessible teaching

This page organizes our guidance and advice for making learning materials accessible, with a focus on accessibility for students who use screen readers.

Everything here can be done by hand, though the Python [tools](../tools/) can be used to speed up parts of it. Additionally, we provide support for instructor-led remediation with an [AI assistant](../ai-assistant/README.md).

## Start here

Approaching accessibility for students who use screen readers.

| Chapter | What it's for |
|---|---|
| [Principles](principles.md) | The principles behind the guide |
| [How screen readers read course materials](screen-readers.md) | An orientation for anyone who has never used a screen reader *(early draft)* |
| [The remediation pipeline](pipeline.md) | The order of the work, why it matters, and each kind of material at a glance |

## By material

Step-by-step workflows for what's in front of you. Before starting, settle the course's [house style](house-style-template.md) (see [P1](principles.md#p1)).

| Chapter | What it's for |
|---|---|
| [Slides](slides.md) | A PowerPoint deck, from structure to the posted PDF |
| [The Word companion](word-companion.md) | A text-only Word document built from the finished deck, designed for listening |
| [Readings](readings.md) | Journal articles and book chapters as PDFs: adding what is missing and keeping what the publisher built |
| [R Markdown worksheets](rmarkdown.md) | Documents knitted from R Markdown: describing plots in the source, the HTML, and the knitted PDF |
| [Keynote and Google Slides](keynote-google-slides.md) | Decks made in Keynote or Google Slides, remediated in PowerPoint *(planned)* |
| [Beamer](beamer.md) | Decks written in LaTeX: why they need a different route, and the routes to test *(drafted as analysis)* |

## Reference

For looking up a rule while working, or for giving to an AI assistant along with the principles and the house style.

| Chapter | What it's for |
|---|---|
| [Describing figures](describing-figures.md) | Rules F1, F2, …: how much to say, builds and repetition, what to describe, symbols, and voice |
| [Equations](equations.md) | Rules E1, E2, …: where equations are heard, writing spoken readings, and equations in figures and sentences |
| [House style: template](house-style-template.md) and [worked example](house-style-example.md) | The course's own choices (spelling, terms, symbols, the companion's format), decided up front and refined as the course goes |
| [WCAG coverage](wcag-coverage.md) | The parts of WCAG 2.1 AA beyond screen-reader access, and how far the pipeline covers them |

## Where each rule comes from

Every rule in the reference chapters ends with an **Evidence** line using these labels, and every item in the worked house style ends with one of them, so a reader can tell a tested result from a habit:

- **Our practice:** how we already wrote descriptions or readings, or a decision made while remediating and kept since.
- **Our choice:** a house-style decision; another course may reasonably decide differently.
- **Our analysis:** reasoning about the problem rather than a tested result.
- **Inferred from edits, then confirmed:** a pattern we noticed in how drafts were revised (including the instructor's blind review of AI drafts), adopted as a rule once we confirmed it.
- **Found in testing:** heard with a screen reader. These give the screen reader, the program, and the month, and link to [Test results](../testing/README.md), because results can change with versions.
- **Found by inspecting files:** checked in a file's structure (PDF tags, HTML, the .pptx), not by ear.
- **From a listener's feedback:** what a screen-reader user told us about materials they used.
- **Advice we received:** from accessibility specialists, adopted after review.
- **Published documentation:** what a program's or standard's own documentation says, not yet checked by us.

A line can combine labels ("our practice; found in testing"). Anything not yet tested is listed in each chapter's *Untested or open* section.

## Related

- [Working with an AI assistant](../ai-assistant/README.md): what to give an assistant, and prompts for any AI chat tool (very preliminary).
- [Test results](../testing/README.md): what we heard with screen readers and found by inspecting files, with the software and dates; the evidence the rules cite. The [test kits](../testing/kits/README.md) are in the same folder.
- [Tools](../tools/README.md): the Python scripts.
- [Working in R with a screen reader](../students/working-in-r-with-a-screen-reader.md), for students.
