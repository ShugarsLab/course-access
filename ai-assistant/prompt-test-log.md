# Prompt test log

What has been tested, how, and what we changed as a result. Results from other instructors are welcome: see [Test an AI prompt](../CONTRIBUTING.md#test-an-ai-prompt).

## Summary

| Prompt | Versions | Tested with | Status |
|---|---|---|---|
| [Draft figure descriptions](prompts/draft-descriptions.md) | 1 tested; 1.1 and 1.2 not yet | Claude, October 2026 | One test, 13 figures, one lecture |
| All other prompts | — | — | Planned, not yet written |

## Test 1: figure descriptions, version 1 (Claude, October 2026)

**Material.** Thirteen figures from one lecture of a graduate statistics course: path diagrams, scatterplots with a fitted line for each group, a histogram of bootstrap estimates, and a figure reproduced from a published article.

**Method.** Each set of slides went into a fresh chat containing only the prompt (with the course context and house style filled in) and the slide images. The instructor then rated each draft blind, side by side with the description they had approved for the course, in random order, using the 0 to 3 edit score in the [rubric](rubric.md).

**Caveat.** The descriptions the drafts were compared with were the instructor's own, written or edited for the course, and the same instructor did the rating. Even rating blind, a rater may recognize, and prefer, their own wording, so the comparison may favor the course's descriptions. Ratings by other instructors and by screen-reader users are needed.

**Results, as rated by the instructor:**

- 12 of 13 drafts were usable with at most a light edit; 4 of 13 were usable as is.
- The instructor preferred their own approved description on 8 figures, the draft on 3, and either on 2.
- An AI grader given the same rubric disagreed with the instructor: it matched the instructor's preference on only 3 of 13 figures. We don't use AI grading in place of people's ratings.

**What we changed.**

- **Version 1.1:** descriptions always state the figure's point, and the assistant flags any sentence that reveals a conclusion the slide sets up for students to reach (REVEALS), so the instructor decides. Withholding the point by rule proved stricter than the instructor's own judgment. Shorter notes; a leading zero before decimals in the default house style.
- **Version 1.2:** eight rules from the instructor's ratings and edits, including: say what a figure is for when it introduces a new idea; explain terms, not only symbols; name the kind of figure the first time; describe a feature by its meaning in the lesson; axes before data; one description per figure; lead with the key fact; and small words (the, labeled) that help a listener picture the figure.

Versions 1.1 and 1.2 have not yet been tested.

## Not yet tested

- Other AI tools: Gemini, ChatGPT, and Copilot are planned.
- Other subjects and kinds of slides.
- The other prompts (planned).
- Ratings by screen-reader users, and by other sighted instructors.

## Results

Add one row per test. Scores are the number of drafts with that edit score or better.

| Date | Prompt and version | Tool and version | Material | Figures | Usable as is | Usable after light edit | Rated by | Notes |
|---|---|---|---|---|---|---|---|---|
| 2026-10 | Draft figure descriptions 1 | Claude | Graduate statistics lecture | 13 | 4 | 12 | Course instructor, blind | Instructor preferred own descriptions on 8 of 13 |
