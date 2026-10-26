# Roadmap

Planned in stages. Dates are aims, not commitments.

## 0.1: first formal release (aim: early 2027)

- Broader WCAG 2.1 AA coverage, starting with color and contrast; the gaps are tracked in [WCAG coverage](guide/wcag-coverage.md). Next: a reusable text-contrast script that measures each text box against what is behind it on the rendered slide; a graphics-contrast and color-vision check for figures, as flags for the instructor to judge; a short chapter pointing to captioning and description practice for video and audio; guidance for forms and interactive HTML.
- The guide: the chapter on how screen readers read course materials (now an early draft), and short sections for decks authored in Keynote and Google Slides. Drafted so far: the principles, the pipeline, house style, describing figures, equations, slides, R Markdown worksheets, readings, the Word companion, test results, WCAG coverage, and Beamer.
- The R and readings pipelines tested on more documents, with the student guide to working in R.
- For students: a short guide to reading equations in Word with NVDA and MathCAT.
- More prompts, and test results from other AI tools and from screen-reader users.
- The scripts as they are, each with instructions and tested versions.
- A demo deck, made for this repository, before and after remediation.
- A DOI for the release (Zenodo).

## 0.2: a package

- One installable command-line tool (`pip install …`) with the checks: alt-text quality, covered table cells, content covered by later build steps, PDF tags, and the Word companion.
- A settings file for house style and for the habits now built into the scripts (agenda slides, code markers, fonts).
- Tests on the demo decks.
- The review loop that writes findings into a deck's speaker notes and reads replies, without an AI assistant.
- The R Markdown PDF tools: retagging what Autotag calls a figure, fixing headings and reading order, and replacement text for inline symbols ([R Markdown worksheets](guide/rmarkdown.md#4-remediate-the-knitted-pdf), 4b to 4e).
- The readings tool: approved descriptions and the language written into a publisher's PDF, with its own checks ([Readings](guide/readings.md#4-write-the-descriptions-and-the-language)).
- Smaller checks named in the guide: content covered by later build steps and loose figure pieces (slides, stage 1); title-first and left-to-right reading order (stage 4); matching slides already remediated in earlier decks (before you start); listing each equation's spoken reading from the exported PDF ([E4](guide/equations.md#e4)); removing the object type PowerPoint appends to some alt text in the PDF (ship).

## Working with an AI assistant

- A prompt pack: each stage of the workflow as a prompt, with what to give the model (slide images, the deck's text) and what to ask back, usable with any chat model that reads images. The first, for drafting figure descriptions, is in [Working with an AI assistant](ai-assistant/README.md).
- A plugin for Claude that runs the stages with the package's checks and keeps a running record of decisions.

## Later

- Learning a house style from an instructor's own descriptions and from what they decline.
- Writing alt text back into Google Slides and Keynote files.
- Beamer: descriptions kept in the LaTeX source, and the Word companion built from it.
- Piloting with other instructors.
