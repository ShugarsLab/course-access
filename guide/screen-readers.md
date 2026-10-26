# How screen readers read course materials

An orientation for instructors who have never used a screen reader. It explains what a screen reader does, what learning through one is like, and why the rest of this guide asks for what it does. The detailed findings from our own testing are in the chapters they affect, linked below.

**Status:** draft. Most of this chapter is general background on how screen readers work, not our own testing.

---

## What a screen reader is

A screen reader is software that turns what is on a screen into synthetic speech, or into braille on a refreshable braille display. It doesn't look at the screen the way a person does. It reads the structure underneath: the text, the headings, lists, and tables a document declares, and whatever text has been attached to pictures.

Common screen readers:

| Screen reader | Runs on | Cost |
|---|---|---|
| NVDA | Windows | Free, open source |
| JAWS | Windows | Commercial |
| Narrator | Windows | Built in |
| VoiceOver | macOS, iPhone, iPad | Built in |
| TalkBack | Android | Built in |

Students who are blind are not the only learners who use screen readers. Many students with low vision use a screen reader alongside magnification, and some students with reading or attention disabilities listen to text to take it in. A student may use different tools for different programs, and may combine listening with braille.

## Listening, not looking

The most important difference is that **listening is serial.** A sighted reader takes in a slide's layout at a glance, picks out what matters, and skips the rest. A listener hears one thing at a time, in the order the file presents it, and has to hold earlier parts in mind to make sense of later ones. Going back costs time: there is no glancing at the top of the slide.

While many experienced users can listen at speech rates a new listener would find hard to follow, instructors should be aware that students may need to listen slowly as they learn new and unfamiliar content.

## Navigating by structure

A document's underlying structure determines the order in which a screen reader delivers content, and how a listener can move through it. Anything that isn't in that structure doesn't exist for the listener.

Screen reader users often move around a document with the keyboard:

- **Reading straight through** from the cursor, or line by line, word by word, or letter by letter when something needs checking or particular attention.
- **Jumping by structure:** to the next heading, list, table, link, or figure, each with a single key. In NVDA, for example, H moves to the next heading and T to the next table.
- **Listing the structure:** a list of every heading or link in a document, to pick one from.
- **Reading tables cell by cell,** hearing each cell's row and column headers when the table declares them.
- **Navigating equations:** stepping through the parts of an equation, when the equation is properly encoded and the screen reader has math support.

Structure is how a listener skims. A document with real headings can be scanned by heading to review selected elements. One whose headings are only bold text has to be heard from the start.

All of this means that properly structuring a document (for example, marking headings and tables, ordering content in the way it is intended to be received, and indicating decorative items a screen reader ought to skip) is critical to making a document accessible.

Few instructors have been trained to encode structure, and doing it perfectly by hand takes time. This is one reason why automated [tools](../tools/README.md) or support from an [AI assistant](../ai-assistant/README.md) can be so beneficial, **as long as those tools are instructor-led**. While structural decisions should be made by an instructor, automated tools can be better at implementing those decisions.


## What a listener can and can't get

**Text** comes through, read as written, including punctuation. Depending on the screen reader's settings, parentheses, quote marks, and colons may be spoken aloud. In our testing, NVDA voiced all three in PowerPoint ([Describing figures](describing-figures.md#where-descriptions-are-read)).

**Pictures** come through only as the alt text attached to them. A chart with no description is silent, announced as "graphic," or announced by its file name. A student cannot learn from a poor description. The [figures chapter](describing-figures.md) goes into depth on writing alt text for educational content.

**Decoration** that has been marked decorative is skipped; decoration that hasn't is announced, often as "graphic" or by an internal name.

**Math** is hard. An equation that is a picture is silent, and one typed as plain text loses its structure: where a fraction, a root, or a subscript starts and stops. Math made with the right tools can be read properly, and explored piece by piece, with a math add-on such as MathCAT for NVDA. Where that works, and where it doesn't, depends on the program: see [Where an equation reaches a listener](equations.md#where-an-equation-reaches-a-listener).

**Code** is mostly punctuation, and screen readers' default settings say little of it. Reading code means turning punctuation up, which makes everything else noisier.

**Things that appear and disappear,** such as builds and animations, may be read all at once or not at all. A table revealed one cell at a time can give away its answers on the first slide ([Slides, stage 2](slides.md#2-plan)).

## The same file sounds different in different places

What a listener hears depends on the file format, the program it is opened in, and the screen reader, not only on what was written. In our testing:

- In PowerPoint, NVDA skipped descriptions written on grouped figures, shapes, and equations, and read the objects inside a group one by one instead.
- A PDF exported from PowerPoint carried the descriptions, and every equation got PowerPoint's own spoken reading; descriptions added to equations made them heard up to four times.
- In Word, equations could be read and explored with a math add-on.

The details, with the software we used, are in [Test results](../testing/README.md). This is why we post a text-only Word companion, designed for listening, beside a PDF that is accessible for everyone ([P2](principles.md#p2)).

## Learning through a screen reader

Put together, these shape what a lecture and its materials are like for a listening student:

- **Two audio streams at once.** In class, the lecture is already audio. Following the slides means a second voice, often through one earbud, while the instructor talks. Materials available before class let a student hear them first, at their own pace.
- **Words that point at the screen don't land.** "As you can see here", "the red line", and "this box" carry nothing for a listener. Saying what is being pointed at helps everyone.
- **Every repetition costs time.** A chart repeated on six slides of a build is six chances to hear the same description ([P6](principles.md#p6)).
- **New notation is just sound until it is named.** A sighted student sees a symbol next to its definition; a listener needs the pairing spoken ([P9](principles.md#p9)).
- **Coordinating with classmates takes shared landmarks.** "Point 3 on slide 37" only works if the listener's format has slide numbers and points too ([P7](principles.md#p7)).
- **Everything takes longer,** which is part of why extended time is a common accommodation, and why materials that waste a listener's time matter.

None of this means a listening student learns less. It means the materials have to carry, in words and structure, what a sighted student gets from layout, color, and position.

## Try it yourself

Fifteen minutes with a screen reader changes how a description reads. A suggested first session:

1. **Turn one on.** On a Mac, VoiceOver: Command-F5. On Windows, Narrator: Windows logo key, Ctrl, and Enter; or install NVDA, which is free.
2. **Open a PDF of one of your own decks** and listen to a slide with a chart on it. What did you hear, in what order? What was missing?
3. **Turn the screen off.** VoiceOver and NVDA each have a screen curtain that blanks the display while the screen reader runs. Listen to the same slide again without looking.
4. **Open a Word document with headings** and jump between them (in NVDA, H; in VoiceOver, the rotor, VO-U). Then try a document whose headings are only bold text.
5. **Listen to an equation** in the PDF and in Word.

Two cautions:

- **A first session is not what an experienced user hears.** You will be slower and more lost than someone who uses a screen reader every day, so judge the content (what was said, in what order, what was left out), not how hard it was to get around.
- **Test before asking a student.** A student who uses a screen reader is the expert on their own setup and preferences, and their feedback is valuable, but they shouldn't be the first to find that a deck is silent. Additionally, without being able to compare the audio and visual, they may not be aware when content is not delivered as expected.

## What this means for your materials

| A listener… | So… | See |
|---|---|---|
| Hears only what is written into the file | Every figure that carries meaning gets a description, written from what students see | [P10](principles.md#p10), [Describing figures](describing-figures.md) |
| Hears it serially | Lead with the point; describe what changed, not everything again | [P4](principles.md#p4), [P6](principles.md#p6) |
| Skims by structure | Real headings, lists, and tables, with header rows marked | [P8](principles.md#p8) |
| Gets different results in different formats | Check how each posted file is heard; offer a format designed for listening | [P2](principles.md#p2), [The Word companion](word-companion.md) |
| Learns notation by ear | Name symbols and new terms before using them alone | [P9](principles.md#p9), [Equations](equations.md) |
