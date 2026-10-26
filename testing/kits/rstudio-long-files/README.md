# RStudio long-file test

A screen reader has been observed to stop reading after roughly 200 lines in RStudio's editor. The cause is not confirmed. One explanation is that the editor, like other code editors built on web technology, shows a screen reader only a window of lines around the cursor; if so, the lines past the window are not lost, but continuous reading stops and the rest has to be reached by moving or jumping. These files test that, and whether the limit counts lines or characters.

**Status:** partly tested. Moving line by line with VoiceOver on a Mac read every line of both .R files to the end; continuous reading did not work in either of RStudio's editing modes (Source or Visual) (VoiceOver on macOS Tahoe 26.6.2, RStudio 2026.09.0+174, October 2026). Not yet run with NVDA or JAWS on Windows.

## The files

| File | What it is |
|---|---|
| `short_lines.R` | 400 numbered lines, each short (`line_001 <- 1  # line 1`). |
| `long_lines.R` | 400 numbered lines of about 200 characters each, roughly the length of a figure description. If reading stops at a different point than in `short_lines.R`, the limit counts characters or screen rows, not lines. |
| `prose_and_chunks.Rmd` | 40 sections of numbered prose lines and code chunks, about 900 lines, with three tests written at the top: continuous reading in Source and Visual mode, folding, and jumping. |

In the .R files, each line carries its number in a comment at the end. RStudio's announced line number is 9 higher, because of the instructions at the top of the file.

## How to run it

Keys are given for Windows, then for a Mac.

| To | Windows | Mac |
|---|---|---|
| Go to the top of the file | Control+Home | Command+Up arrow |
| Go to the bottom | Control+End | Command+Down arrow |
| Read continuously from the cursor | NVDA key+Down arrow (NVDA); Insert+Down arrow (JAWS) | Control+Option+A (VoiceOver) |
| Switch between Source and Visual mode (.Rmd) | Control+Shift+F4 | Command+Shift+F4 |
| Fold all sections (.Rmd, Source mode) | Alt+O | Command+Option+O |
| Unfold the section at the cursor | Shift+Alt+L | Command+Shift+Option+L |
| Jump To menu of sections | Shift+Alt+J | Command+Shift+Option+J |

1. Turn on RStudio's screen-reader support (Help › Accessibility › Screen Reader Support).
2. Open `short_lines.R` and go to the top.
3. Read down with the Down arrow. Then go back to the top and read continuously.
4. Note the last number you hear each way, and whether the Down arrow still moves the cursor after reading stops.
5. Repeat with `long_lines.R`.
6. Open `prose_and_chunks.Rmd` and follow the three tests written at its top.

If NVDA goes silent, open the NVDA menu, Tools, View log, and save the last part of the log. With VoiceOver, note where the VoiceOver cursor ends up when reading stops (in our test, continuous reading in Source mode left the editor after the current line).

## What to report

- Screen reader and version (NVDA: NVDA menu, Help, About; VoiceOver: the macOS version), operating system, and RStudio version (Help, About RStudio).
- For each file and each way of reading (line by line, continuous): the last line number heard, and whether the cursor could still move past it.
- For the .Rmd: results of each of its three tests, in Source and in Visual mode.

Report results with the *Test kit results* issue template on GitHub, or see [Feedback](../../../README.md#feedback) for other ways to send them.
