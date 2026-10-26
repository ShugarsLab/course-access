# The speaker-notes review loop

When an AI assistant, or a collaborator, does part of the work on a deck, the slide's own speaker notes are a good place for the conversation between it and the instructor: each finding sits beside the slide it concerns, and replies go in the same place. This works best with an assistant that can read and write the deck file itself; with a chat tool, the instructor copies the blocks in and out.

A block for one slide might read:

```
=== ACCESSIBILITY NOTES ===
Stage 2 · plan (SKIP any item you don't want)

1. Fix the typo "the the default" to "the default".
2. Turn [b] (a picture of R code) into a text box.
3. Describe [a].
4. Mark [c] decorative (same chart as the previous slide).

--- replies below this line ---
SKIP 2: keep the screenshot; describe the highlighted line instead
```

- **Every item is a plan the instructor can skip.** A skip reason can say what to do instead. Saying "done" with the stage approves everything not skipped.
- **Every slide gets a block,** even one with nothing to do, so there is always a place to write.
- **Objects are named by labels both sides can see.** Short labels such as [a] and [b] are written into the objects' names, which the Selection Pane shows, so a finding and the pane point at the same object. Never refer to an object by an internal id: PowerPoint shows it nowhere.
- **Clear the review blocks before shipping** (screen readers read speaker notes), and the labels from the object names. Speaker notes kept for teaching stay.

The stages these blocks follow are in [Slides](../guide/slides.md).

**With the scripts.** Writing and reading these blocks automatically is planned.
