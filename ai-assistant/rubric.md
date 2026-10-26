# Scoring rubric for figure descriptions

For testing prompts: score each description an AI tool drafts, against the slide and, where one exists, a reference description the instructor approved. The same rubric works for comparing tools or prompt versions. Score from the slide image first, then look at the reference.

## Per description

**Overall: how much editing before it could go in the deck?** This is the main score. The rubric has not yet been shown to match a human reviewer; in our first check, a model grading with an earlier version agreed with the instructor's preference on 3 of 13 figures. Use human ratings.

| Score | Meaning |
|---|---|
| 3 | Usable as is |
| 2 | Light edit: wording, house style, a detail added or cut |
| 1 | Substantive edit: a fact wrong, the point missed, the wrong depth |
| 0 | Rewrite, or describes the wrong thing |

**Criteria** (each 0, 1, or 2; "n/a" where it doesn't apply). These say *why* a description got its overall score.

| # | Criterion | 2 | 1 | 0 |
|---|---|---|---|---|
| C1 | Accuracy | Everything stated is on the slide or follows from it; covers only its own figure (doesn't introduce a panel another description holds) | A minor imprecision (a rounded value slightly off, a vague label) | A wrong fact, an invented value, a misread label or direction |
| C2 | Coverage and order | Everything that matters for the lesson, including labels, arrows, and highlights; leads with the key fact; for a chart, axes (horizontal, then vertical) before the marks | Misses a secondary element, or the order makes it harder to follow | Misses what the figure is there to show |
| C3 | Depth for novelty | Names and explains a new kind of figure; skips that for a familiar one; glosses new terms and symbols | Slightly too much or too little | Explains a familiar figure at length, leaves a new one unexplained, or refers to something not yet named |
| C4 | Fit and focus | Doesn't repeat what the slide's text already says; adds what the text needs; no flourishes, irrelevant absences, or detail the lesson doesn't use | Some repetition or extra detail, or thin where the figure is the evidence | Largely repeats the slide text, buries the point in detail, or omits the evidence |
| C5 | Framing: what changed or what is new | For builds and repeats of a figure, names what changed; for a figure introducing a new idea, describes it as that idea | Right framing, vaguely done | "Same as before" with no change named; re-describes a repeat from scratch; or frames a new idea as a change from the last slide |
| C6 | The point | States the interpretation the instructor would give | Point implied, not stated | No point, or the wrong point |
| C7 | Color, line style, symbols in words | Every encoding is put in words and matched to the legend; symbols glossed at first use | One encoding left out | Meaning depends on color or a bare symbol |
| C8 | House style | Follows the house style it was given | One or two slips | Many slips (symbols, quote marks, number format) |
| C9 | Voice and length | Plain and spoken; describes features by their meaning (directly, not straight across); keeps the small connecting words that make it easy to follow; right length | A little long, stiff, or clipped | "This image shows…", telegraphic, or far too long or short |

**Flag, not scored: Reveals.** Yes if the description states a conclusion the slide sets up for students to reach themselves (a question, a prediction, a pattern to notice). Whether that is acceptable is the instructor's call: often the question is one the lecture asks of itself, and withholding the point is hard to do well. Report the flag; don't lower the score for it. Did the writer flag it in its notes?

## Per run

- **Figures found:** figures that needed a description and got one; figures missed; things described that shouldn't be (slide text, typed equations, decoration).
- **Notes:** were uncertain values, repeats, and prompt slides flagged?
- **Format:** did the output follow the requested table?

## Reporting

For each run: the tool and version, the prompt version, the date, the mean overall score, the share scored 3 or 2, and the criteria that most often scored 0. Keep the drafts and scores with the run.
