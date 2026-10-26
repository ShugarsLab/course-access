# Contributing

This repository is a draft, shared so it can be improved. Corrections, results from your own courses and tools, and suggestions are all welcome. Short notes are enough.

## What we would welcome

- **Corrections:** anything wrong, unclear, or out of date, including menu paths in newer versions of the software.
- **What happened when you tried it,** on your own slides, worksheets, or readings, in another subject, or with other software.
- **Test results** from the [test kits](testing/kits/README.md), or from trying the [AI prompts](ai-assistant/README.md) (both below).
- **From screen-reader users:** what works for you and what doesn't. Anything you choose to share is welcome; nothing is expected.
- **Ratings by colleagues,** including sighted instructors who teach the same material, of AI drafts or of finished descriptions.

## How to send it

- **Open an issue** on GitHub. There are templates for general feedback, test-kit results, and prompt test results.
- **Email** [sarah.shugars@rutgers.edu](mailto:sarah.shugars@rutgers.edu).
- **Open a pull request** for a correction or a new test result. For a larger change to the guide or the tools, open an issue first so we can talk it through.

## Share test-kit results

Each kit's README says what to run and what to report: the screen reader and its version, the operating system, the program and its version, and what you heard. Use the *Test kit results* issue template. New results are added to [Test results](testing/README.md).

## Test an AI prompt

1. **Run it on your own slides** with whatever AI tool you use, following the prompt's instructions. Note the prompt's version (at the top of the file) and your tool and version.
2. **Rate each draft** with the 0 to 3 edit score in the [rubric](ai-assistant/rubric.md): 3 usable as is, 2 light edit, 1 substantive edit, 0 rewrite. A note on what you changed is the most useful part.
3. **If you can, rate blind.** Put each draft beside a description you wrote yourself, in random order, and score both without knowing which is which. That's how we tested, and it showed that a draft that looks good on its own can still lose to the instructor's own version.

Share results with the *Prompt test results* issue template, or a pull request adding a row to the results table in the [prompt test log](ai-assistant/prompt-test-log.md). Suggested changes to a prompt are welcome too, with the drafts or ratings that show why.

## What not to share

- **Anything about students:** names, grades, accommodations, or their work.
- **Material you don't have the right to share publicly,** such as slides or figures from published papers and publisher material. Share scores and short notes in your own words instead of images.
- **Before testing an AI tool on course materials,** check your institution's policy on using AI tools with course materials.

## Style, for pull requests to the guide

Write one line per paragraph in Markdown, use the serial (Oxford) comma, and give a rule's evidence with the labels in [Where each rule comes from](guide/README.md#where-each-rule-comes-from). Rule numbers (F1, E1, …) are provisional until the first formal release; see the [CHANGELOG](CHANGELOG.md).
