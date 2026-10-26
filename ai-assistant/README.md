# Working with an AI assistant

> **Very preliminary.** This part of the repository is just getting started, and almost nothing in it has been tested. One prompt is written, for drafting figure descriptions. It has been tested once: one AI tool (Claude), on 13 figures from one statistics lecture, rated by one instructor. Later versions of that prompt, other AI tools, other subjects, other raters, and ratings by screen-reader users are all untested. Expect what is here to change, and review everything an assistant writes. Details in the [prompt test log](prompt-test-log.md).

This area will bring together what an instructor needs to do parts of the [remediation pipeline](../guide/pipeline.md) with an AI assistant: what to give it, plain-text prompts for each task, and later a plugin for Claude. The prompts work with whatever AI chat tool the instructor has (Microsoft Copilot, ChatGPT, Gemini, Claude, or another model that can read images) and need no programming.

## Before using an AI tool on course materials

- Use a tool your institution has approved, and follow its policy on what may be uploaded.
- Don't upload anything about students: names, grades, accommodations, or their work.
- Slides can contain other people's material (figures from papers, publisher images). Check whether your tool keeps or trains on what you upload.

## What to give an assistant

An assistant needs much the same material a person would. Together, it is a lot to give: a short prompt is only one piece.

| Give it | Why | Status |
|---|---|---|
| The course context: subject and level, what students have learned so far, which kinds of figures are new | How much to say depends on how new an idea is ([P5](../guide/principles.md#p5)) | Part of the prompt |
| The course's [house style](../guide/house-style-template.md) | So drafts follow the course's own choices (spelling, terms, symbols) | Part of the prompt |
| Images of the slides as students see them, a build at a time | So it describes what students see, not the files inside ([P10](../guide/principles.md#p10)) | Part of the prompt |
| A prompt for the task | Says what to do and what to send back | One written: [draft figure descriptions](prompts/draft-descriptions.md) |
| The [principles](../guide/principles.md), and the [figures](../guide/describing-figures.md) and [equations](../guide/equations.md) chapters | The full rules; each prompt carries only a short summary of them | **Untested.** Plausibly better than the summary alone, but we haven't compared the two |

The [guide](../guide/) remains the source of the rules. Each prompt summarizes the conventions it relies on and links to the full chapter.

## Two ways an AI assistant can work

AI tools work with your materials in one of two ways. The same product can do either, depending on its features, your plan, and your institution's settings.

- **In the chat only.** You paste text or attach images of your slides, and the assistant replies with text: draft descriptions, a checklist, suggested fixes. You make every change yourself in PowerPoint, Word, or Acrobat. Almost every AI tool can work this way, so the prompts here are written for it.
- **On the files themselves.** Some tools can also open a file, change it, and give it back: a deck with the alt text written in, figures grouped, or the reading order set. A quick test: if the tool can return a changed .pptx, or change the slides inside PowerPoint, it works on files. If it can only reply in the chat, it doesn't. We worked this way in our own course; the *Assistant* and *Instructor* columns in the [slides chapter](../guide/slides.md) show how the work was divided. Check every change in the file itself, against an untouched copy of the deck.

Either way:

- **It can draft and check text:** figure descriptions from slide images, a plan of what each slide needs, a review of descriptions against a house style, proposed house-style rules drawn from patterns in the instructor's edits, and a first house style drawn from descriptions the instructor has already written.
- **In the chat, structure is yours to change.** Tasks that depend on a file's internal structure (grouping, reading order, PDF tags) get a checklist from a chat-only assistant, not a fix. You carry them out, and the [tools](../tools/README.md) can check some of them.
- **It decides nothing.** What a figure is for, what a prompt slide should withhold, and what stays decorative are teaching decisions. The prompts tell the assistant to ask when it can't tell, and the instructor reviews everything it writes.

## Keeping the conversation beside the slides

The [speaker-notes review loop](review-loop.md) keeps each of the assistant's findings, and the instructor's reply, in the speaker notes of the slide it concerns.

## How to use them (planned)

1. **Set up once per course.** Paste the setup prompt (planned; until it exists, the course context section of the [description prompt](prompts/draft-descriptions.md) does this job), the course's house style, and a short note on what students have learned so far into the tool's project or custom-instructions feature (most tools have one), so every later chat starts with them. Where the tool accepts files, the principles and the figures and equations chapters can go there too (untested; see above).
2. **Export the slides as images** (File › Export in PowerPoint) and work a build or 10 to 20 slides at a time. Descriptions across a build depend on each other, so a build goes in one chat.
3. **Paste the prompt for the task, attach the images, and review what comes back** before putting any of it into the deck.
4. **Close out each week.** After the week's materials are posted, give the assistant its drafts beside your final versions (or a list of what you changed) and ask it to name the patterns in your edits and propose new house-style rules, or changes to existing ones, each with the edits it rests on. You decide which to adopt. Adopted rules go into the [house style](../guide/house-style-template.md), marked *inferred from edits, then confirmed*, so the next week's drafts start from them. This is how most of our own conventions were found; the step as a prompt is planned.

## Planned contents

Prompts live in the [`prompts/`](prompts/) folder, one file per task.

| File | Task | Stage |
|---|---|---|
| `prompts/setup.md` | Course context, house style, what students know so far | Before you start |
| `prompts/house-style-from-examples.md` | Draft a house style from descriptions the instructor has already written | Before you start |
| `prompts/plan.md` | Per slide: pictures of text, tables, contrast, color-only meaning, wording that works only by sight, links, likely repeats | 2. Plan |
| [`prompts/draft-descriptions.md`](prompts/draft-descriptions.md) | Figure descriptions for a build, one slide at a time, saying only what changed (drafted; first test with Claude) | 3. Draft and review |
| `prompts/review-descriptions.md` | Check existing descriptions against the conventions and house style | 3. Draft and review |
| `prompts/structure-checklist.md`, `prompts/reading-order-checklist.md` | What to group, ungroup, or split; the order a slide should be read in | 1 and 4 |
| `prompts/readings.md` | Descriptions for figures in a publisher PDF, filling in what the paper's text leaves out | Readings |
| `prompts/rmarkdown.md` | Alt text for plots in an R Markdown worksheet | Worksheets |
| `prompts/weekly-review.md` | Compare the assistant's drafts with the instructor's final versions; propose house-style rules from the patterns in the edits | After each week |

Each prompt will say which models and versions it was tested with. Prompts are scored with the [rubric](rubric.md): mainly, how much editing a description needs before it can go in the deck.

## Contributing results

Tried a prompt on your own slides? Results from other courses, tools, and raters are what will improve these prompts. See [Test an AI prompt](../CONTRIBUTING.md#test-an-ai-prompt) for how to rate the drafts and what not to share, and report through the *Prompt test results* issue template or a pull request to the [prompt test log](prompt-test-log.md).

## Coming later

- The rest of the task prompts above, each tested before it is marked ready.
- A plugin for Claude that runs the stages with the [tools](../tools/)' checks and keeps a running record of decisions ([roadmap](../ROADMAP.md)).
