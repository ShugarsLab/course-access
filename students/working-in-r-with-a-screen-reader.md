# Working in R with a screen reader

This guide is for students who use a screen reader in a course taught in R, and, in its last section, for the instructors teaching them. It covers setting up RStudio, three tools that make plots and tables readable by ear, reading long files, and what to do when a package won't install.

| To… | Use | Install once |
|---|---|---|
| Move around RStudio by keyboard | RStudio's screen-reader mode | Built in |
| Explore a plot by sound, text, or braille | maidr | `install.packages('maidr')` |
| Read the data behind a plot, cell by cell | `knitr::kable()` | Comes with R Markdown |
| Hear a written description of a plot | BrailleR | From GitHub (see below) |

## Set up RStudio

RStudio has many panes, and tabbing through all of them is slow. Two changes help most: turn on screen-reader mode, and jump straight to the pane you want instead of tabbing.

**Turn on screen-reader support.** Help › Accessibility › Screen Reader Support (on Windows, Alt+Shift+/ also works). RStudio reloads. Under Help › Accessibility › Accessibility Options, also turn on Entire page has application role and Reduce user interface animations.

**Jump to a pane.** These are the same on Windows and Mac:

| Pane | Move focus | Fill the window |
|---|---|---|
| Editor (your .Rmd or script) | Ctrl+1 | Ctrl+Shift+1 |
| Console | Ctrl+2 | Ctrl+Shift+2 |
| Help | Ctrl+3 | Ctrl+Shift+3 |
| Plots | Ctrl+6 | Ctrl+Shift+6 |
| Environment | Ctrl+8 | Ctrl+Shift+8 |
| Viewer (where maidr plots open) | Ctrl+9 | Ctrl+Shift+9 |

To read console output, press Alt+Shift+2 on Windows (Ctrl+Option+2 on a Mac). Alt+Shift+K (Option+Shift+K on a Mac) lists every shortcut.

**Other tips.**

- Hide panes you don't use: View › Panes.
- Turn off your screen reader's browse or virtual cursor while editing code or using menus.
- If the arrow keys don't respond in the editor, press End first.
- Ctrl+L clears the console, so new output is easy to find.

Source: [Posit's screen-reader guide](https://docs.posit.co/ide/user/ide/guide/accessibility/screen-reader.html) and [keyboard shortcut list](https://docs.posit.co/ide/user/ide/reference/shortcuts.html).

## Reading long files

RStudio's editor may not let a screen reader read a long file straight through.

- **Reading line by line works.** Moving down a line at a time with the Down arrow read every line to the end of a 400-line file, with short lines and with long ones. *Tested with VoiceOver on macOS Tahoe 26.6.2 and RStudio 2026.09.0+174, October 2026.*
- **Continuous reading is unreliable.** With VoiceOver, reading continuously in the source editor read the current line and then left the editor, and in the Visual editor it stopped after about 30 lines. *Same test.* A screen reader on Windows has been observed to stop after about 200 lines when reading continuously; the cause is not confirmed and that behavior has not yet been tested systematically.

What works around it:

1. **Read a worksheet in the browser, and use RStudio for code.** If your instructor posts the knitted HTML version, open it in a web browser, where your screen reader can read the whole page and move by heading. Use RStudio only to run and edit code.
2. **In RStudio, read by line, or jump to a section first.** Folding helps: Alt+O folds every section to its heading, Shift+Alt+L unfolds the one under the cursor, and Shift+Alt+J opens a Jump To menu of sections. On a Mac: fold all Cmd+Option+O, unfold Cmd+Shift+Option+L, Jump To Cmd+Shift+Option+J, Go to line Cmd+Shift+Option+G. *Untested with a screen reader.*

## Explore a plot by sound: maidr

[maidr](https://r.maidr.ai/) turns a ggplot2 or base R plot into an interactive version you can move through with the keyboard, hearing each data point as a tone, as text, or in braille. It works with bar charts, histograms, line plots, scatterplots, box plots, and several other common types.

**Install once,** in the console:

```r
install.packages('maidr')
```

**Use it in the console.** Run maidr in the console to explore a plot, rather than adding it to an .Rmd file you knit (see *Keep maidr out of files you knit*, below):

```r
library(maidr)
library(ggplot2)

p <- ggplot(mpg, aes(x = class)) +
  geom_bar()
show(p)
```

maidr works most reliably with ggplot2 plots. For a base R plot, its documentation says to draw the plot first (for example `hist(x)`), then run `show()` with nothing in the parentheses. If a base R plot doesn't respond, make it with ggplot2 instead, or get a description of it with BrailleR (below).

The plot opens in the Viewer pane. Press Ctrl+9 to move there, then Tab to put focus on the plot. maidr needs an internet connection: the plot loads its code from the web each time it opens.

| Key | What it does |
|---|---|
| Left and right arrows | Move from one data point to the next |
| Up and down arrows | Move between groups or series |
| L, then X, Y, or T | Read the x-axis label, y-axis label, or title |
| S | Turn sound on or off |
| T | Turn text on or off |
| B | Turn braille on or off |
| Ctrl+/ (Cmd+/ on a Mac) | List every key |

**Keep maidr out of files you knit.** Don't add `library(maidr)` to an .Rmd file you knit or hand in. In a test, maidr removed plots' alt text and captions from the knitted HTML, and ggplot2 plots disappeared from the knitted PDF. Explore the plot in the console, then knit as usual. *Tested October 2026 with R 4.6.0, maidr 0.4.0, rmarkdown 2.31, and knitr 1.51. Exploring a plot from the console was tried by ear; the knitted files were checked by inspecting them.*

## Read the data behind a plot: kable

Sometimes the clearest way into a plot is the numbers it shows. `knitr::kable()` turns a data frame into a table in the knitted document, with a header row, so a screen reader can move through it cell by cell. It comes with R Markdown, so there is nothing to install, and it works in HTML and PDF alike, which makes it the most dependable option here.

For example, the counts behind a histogram of 100 dice rolls:

```r
knitr::kable(
  as.data.frame(table(sample_100)),
  col.names = c('Outcome', 'Count'),
  caption = 'Counts of each outcome in 100 dice rolls'
)
```

`col.names` sets the column headers and `caption` gives the table a title. In the console, printing the data frame shows the same numbers as plain text.

## Hear a description of a plot: BrailleR

[BrailleR](https://r-resources.massey.ac.nz/BrailleRInAction/) writes a text description of a plot into the console: its type, axes, ranges, and shape. It tends to work better with ggplot2 plots than base R ones. The author's online book, *BrailleR in Action*, covers it in depth.

**Install once.** BrailleR isn't on CRAN, R's main package library, so it installs from GitHub in two steps:

```r
install.packages('remotes')
remotes::install_github('ajrgodfrey/BrailleR')
```

On Windows you may see a warning that Rtools is required. For BrailleR this is usually only a warning; see *If an install fails*, below.

**Use it.** Load it near the top of your file (the capital B and R matter), save a plot as an object, and pass it to `VI()`:

```r
library(BrailleR)

h <- hist(x)
VI(h)
```

The description prints in the console. Press Alt+Shift+2 on Windows (Ctrl+Option+2 on a Mac) to read it.

## If an install fails

Installing packages is often the hardest part of getting started in R. Some common messages:

- **Rtools is required to build R packages but is not currently installed.** Rtools is a Windows toolkit for building packages from source. Installing BrailleR from GitHub usually prints this as a warning and finishes anyway. Check by running `library(BrailleR)`: if no error appears, it worked.
- **Do you want to install from sources the package which needs compilation?** Answer `no`. R then installs a ready-built version, which doesn't need Rtools.
- **there is no package called …** Check the capitalization (`BrailleR`, not `brailleR`) and that the install finished without an error.
- **unexpected input, or unexpected symbol,** when pasting code from an email or document: curly quotes have usually replaced straight ones. Retype the quotes in RStudio.

If it still fails, ask for help with the exact command you ran and the full message. To copy the message, press Alt+Shift+2 on Windows (Ctrl+Option+2 on a Mac) to reach the console output, then select and copy.

## For instructors: R Markdown documents you post

Instructors posting worksheets, solutions, or examples knitted from R Markdown: see [R Markdown worksheets](../guide/rmarkdown.md) in the guide. It covers fixed-text alt text with `fig.alt`, `kable()` tables of plotted data, posting the knitted HTML alongside any PDF, and why we don't yet put maidr in posted documents.
