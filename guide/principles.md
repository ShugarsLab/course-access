# Principles

*Start here.* This page summarizes the pedagogical principles behind everything in this guide, for instructors making content accessible for students using a screen reader.

The detailed rules that flow from these principles are in the [guide](README.md). Rules prefixed with F relate to [describing figures](describing-figures.md), and rules prefixed with E relate to [equations](equations.md). The course's own choices (spelling, terms, how symbols are written) go in a [house style](house-style-template.md).

Every principle here starts from one question: **what does a student who is listening, rather than looking, need in order to learn?**

<a id="p1"></a>

## P1. Keep the teaching decisions with the instructor

What a figure is for, what a slide should hold back, and what counts as decorative are teaching decisions: tools and AI assistants can find problems and draft text, but the instructor should make all decisions. Establish a house style to encode instructor norms and preferences.

Details: [House style template](house-style-template.md) and [worked example](house-style-example.md); [Working with an AI assistant](../ai-assistant/README.md)

<a id="p2"></a>

## P2. What is written isn't always what is heard

Alt text in a file is not necessarily read aloud: in our testing, a screen reader skipped descriptions on grouped figures, shapes, and equations in PowerPoint. Check how materials reach a listener, and offer a format designed for listening (a text-only Word companion with live equations) beside a PDF that is accessible for everyone.

Details: [Test results](../testing/README.md); [Where descriptions are read](describing-figures.md#where-descriptions-are-read); [Where an equation reaches a listener](equations.md#where-an-equation-reaches-a-listener), [E1](equations.md#e1), [E2](equations.md#e2); [The Word companion](word-companion.md)

<a id="p3"></a>

## P3. Figures are teaching materials

A description stands in for the figure and for what the instructor highlights while talking about it. Say what a student needs in order to learn from it, in the voice of the lecture, using articles and connecting words to make a picture clear. Clarity matters more than brevity.

Details: [F23](describing-figures.md#f23), [F25](describing-figures.md#f25), [F26](describing-figures.md#f26)

<a id="p4"></a>

## P4. Focus on the lesson

State a figure's key pedagogical takeaway first, and cut detail that doesn't serve the lesson. Where stating the point gives away something the slide asks students to work out, flag it and let the instructor decide. When the point is for students to find a pattern themselves, give them the material to find it with: the data as a real table, equations they can explore, the figure described without its conclusion.

Details: [F4](describing-figures.md#f4), [F5](describing-figures.md#f5), [F6](describing-figures.md#f6); [E1](equations.md#e1); tables of plotted data in [R Markdown worksheets](rmarkdown.md#1-describe-figures-in-the-source)

<a id="p5"></a>

## P5. Descriptions are developmental

The first time a type of figure appears, say what it is and how to read it: what the axes, boxes, or colors stand for. By the tenth of its kind, a sentence is enough. If the slide's own text already makes the point, the figure illustrates it; if the figure is the evidence, give the numbers.

Details: [F1](describing-figures.md#f1), [F2](describing-figures.md#f2), [F3](describing-figures.md#f3), [F27](describing-figures.md#f27)

<a id="p6"></a>

## P6. Listening is serial, so spare the listener repetition

A sighted student finds what changed on a slide at a glance; a listener hears everything again from the start. Across a build, say what changed and name it, and mark repeated content decorative. A figure that introduces a new idea still stands on its own, even when it grew out of the last one. This principle should be balanced with P7.

Details: [F7](describing-figures.md#f7), [F8](describing-figures.md#f8), [F9](describing-figures.md#f9), [F10](describing-figures.md#f10)

<a id="p7"></a>

## P7. Learning is social, so enable peer communication

While reducing repetition is generally better for a listener (P6), be thoughtful about enabling students to discuss materials with others. In the Word companion, keeping repeated titles, numbering slides to match the PDF, and using real bullets can help students cross-reference content with their peers ("point 3 on slide 37").

Details: [The Word companion](word-companion.md); [the companion document](house-style-example.md#the-companion-document) in the worked house style; [slide numbers and headings](house-style-template.md#slide-numbers-and-headings) in the template; repeated titles in the slides themselves, [F10](describing-figures.md#f10)

<a id="p8"></a>

## P8. Text should be text, and tables should be tables

A screenshot of code, a quotation, or a definition is carrying text: make it real text, which a screen reader can read, anyone can search, and magnification can enlarge without blurring. The exception is a screenshot kept to show a highlighted part in context, such as one line of R output; its description then says what is highlighted. A picture of a table becomes a real table with its header row marked, unless it is a repeat with selected cells highlighted or is illustrative rather than there to convey data. Table cells hidden under shapes in a build are emptied, or a listener hears the answers early.

Details: [F14](describing-figures.md#f14), [F15](describing-figures.md#f15); [Slides, stage 2](slides.md#2-plan)

<a id="p9"></a>

## P9. Describe new terms, notation, and symbols

A symbol read aloud before it has been named is just a sound. The first time a symbol or new term appears, say what it means (mu, the population mean; a mediator, which carries part of the effect). Pair the name and symbol for a while, then use the symbol alone. Write symbols out in words in descriptions (mu, not μ).

Details: [F19](describing-figures.md#f19), [F20](describing-figures.md#f20), [F21](describing-figures.md#f21), [F22](describing-figures.md#f22), [F24](describing-figures.md#f24); [E7](equations.md#e7), [E12](equations.md#e12)

<a id="p10"></a>

## P10. Describe what students see

The picture stored in a file isn't always what students see: crops, overlays, arrows, and labels are drawn on top of it on the slide. An AI tool reading the file can describe the stored picture rather than the slide, producing a description that doesn't match what students are meant to see. Work from the slide as it appears, not from the image file inside it. Name the axes before the marks, give each figure its own description, and say in words anything that color, line style, or marker shape shows.

Details: [F11](describing-figures.md#f11), [F12](describing-figures.md#f12), [F13](describing-figures.md#f13), [F16](describing-figures.md#f16), [F18](describing-figures.md#f18)
