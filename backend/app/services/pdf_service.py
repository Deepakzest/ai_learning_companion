from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    KeepTogether,
)


def generate_exam_notes_pdf(notes, output_path):

    document = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontSize=24,
        leading=30,
        alignment=TA_CENTER,
        spaceAfter=8,
    )

    subtitle_style = ParagraphStyle(
        "SubtitleStyle",
        parent=styles["Normal"],
        fontSize=12,
        leading=18,
        alignment=TA_CENTER,
        spaceAfter=20,
    )

    section_style = ParagraphStyle(
        "SectionStyle",
        parent=styles["Heading1"],
        fontSize=16,
        leading=20,
        spaceBefore=14,
        spaceAfter=8,
    )

    subsection_style = ParagraphStyle(
        "SubsectionStyle",
        parent=styles["Heading2"],
        fontSize=12,
        leading=16,
        spaceBefore=8,
        spaceAfter=5,
    )

    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["BodyText"],
        fontSize=10,
        leading=15,
        spaceAfter=6,
    )

    bullet_style = ParagraphStyle(
        "BulletStyle",
        parent=body_style,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=4,
    )

    question_style = ParagraphStyle(
        "QuestionStyle",
        parent=body_style,
        fontSize=10.5,
        leading=15,
        spaceBefore=6,
        spaceAfter=5,
    )

    answer_style = ParagraphStyle(
        "AnswerStyle",
        parent=body_style,
        leftIndent=12,
        spaceAfter=3,
    )

    story = []

    # --------------------------------------------------
    # TITLE
    # --------------------------------------------------

    title = notes.get("title", "Exam-Oriented Study Notes")

    story.append(Spacer(1, 25 * mm))

    story.append(
        Paragraph(
            "AI LEARNING COMPANION",
            subtitle_style,
        )
    )

    story.append(
        Paragraph(
            title,
            title_style,
        )
    )

    story.append(
        Paragraph(
            "Exam-Oriented Study Notes",
            subtitle_style,
        )
    )

    story.append(Spacer(1, 10 * mm))

    story.append(
        Paragraph(
            "Generated from the lecture transcript",
            body_style,
        )
    )

    story.append(PageBreak())

    # --------------------------------------------------
    # 1. OVERVIEW
    # --------------------------------------------------

    story.append(
        Paragraph(
            "1. Overview",
            section_style,
        )
    )

    overview = notes.get("overview", "")

    if overview:
        story.append(
            Paragraph(
                overview,
                body_style,
            )
        )

    # --------------------------------------------------
    # 2. IMPORTANT DEFINITIONS
    # --------------------------------------------------

    definitions = notes.get("important_definitions", [])

    if definitions:

        story.append(
            Paragraph(
                "2. Important Definitions",
                section_style,
            )
        )

        for index, item in enumerate(definitions, start=1):

            term = item.get("term", "")
            definition = item.get("definition", "")

            story.append(
                Paragraph(
                    f"<b>{index}. {term}</b>",
                    subsection_style,
                )
            )

            story.append(
                Paragraph(
                    definition,
                    body_style,
                )
            )

    # --------------------------------------------------
    # 3. KEY CONCEPTS
    # --------------------------------------------------

    concepts = notes.get("key_concepts", [])

    if concepts:

        story.append(
            Paragraph(
                "3. Key Concepts",
                section_style,
            )
        )

        for index, item in enumerate(concepts, start=1):

            concept = item.get("concept", "")
            explanation = item.get("explanation", "")

            story.append(
                Paragraph(
                    f"<b>{index}. {concept}</b>",
                    subsection_style,
                )
            )

            story.append(
                Paragraph(
                    explanation,
                    body_style,
                )
            )

    # --------------------------------------------------
    # 4. IMPORTANT POINTS
    # --------------------------------------------------

    important_points = notes.get("important_points", [])

    if important_points:

        story.append(
            Paragraph(
                "4. Important Exam Points",
                section_style,
            )
        )

        for point in important_points:

            story.append(
                Paragraph(
                    f"• {point}",
                    bullet_style,
                )
            )

    # --------------------------------------------------
    # 5. COMPARISONS
    # --------------------------------------------------

    comparisons = notes.get("comparisons", [])

    if comparisons:

        story.append(
            Paragraph(
                "5. Important Comparisons",
                section_style,
            )
        )

        for comparison in comparisons:

            topic = comparison.get("topic", "")
            points = comparison.get("points", [])

            story.append(
                Paragraph(
                    topic,
                    subsection_style,
                )
            )

            table_data = [
                [
                    Paragraph("<b>Aspect</b>", body_style),
                    Paragraph("<b>First</b>", body_style),
                    Paragraph("<b>Second</b>", body_style),
                ]
            ]

            for point in points:

                table_data.append(
                    [
                        Paragraph(
                            point.get("aspect", ""),
                            body_style,
                        ),
                        Paragraph(
                            point.get("first", ""),
                            body_style,
                        ),
                        Paragraph(
                            point.get("second", ""),
                            body_style,
                        ),
                    ]
                )

            table = Table(
                table_data,
                colWidths=[
                    40 * mm,
                    60 * mm,
                    60 * mm,
                ],
                repeatRows=1,
            )

            table.setStyle(
                TableStyle(
                    [
                        (
                            "GRID",
                            (0, 0),
                            (-1, -1),
                            0.5,
                            colors.grey,
                        ),
                        (
                            "BACKGROUND",
                            (0, 0),
                            (-1, 0),
                            colors.lightgrey,
                        ),
                        (
                            "VALIGN",
                            (0, 0),
                            (-1, -1),
                            "TOP",
                        ),
                        (
                            "LEFTPADDING",
                            (0, 0),
                            (-1, -1),
                            6,
                        ),
                        (
                            "RIGHTPADDING",
                            (0, 0),
                            (-1, -1),
                            6,
                        ),
                        (
                            "TOPPADDING",
                            (0, 0),
                            (-1, -1),
                            6,
                        ),
                        (
                            "BOTTOMPADDING",
                            (0, 0),
                            (-1, -1),
                            6,
                        ),
                    ]
                )
            )

            story.append(table)
            story.append(Spacer(1, 8))

    # --------------------------------------------------
    # 6. EXAM QUESTIONS
    # --------------------------------------------------

    questions = notes.get("exam_questions", [])

    if questions:

        story.append(
            Paragraph(
                "6. Likely Exam Questions",
                section_style,
            )
        )

        for index, question in enumerate(questions, start=1):

            q = question.get("question", "")
            answer_points = question.get("answer_points", [])

            question_block = []

            question_block.append(
                Paragraph(
                    f"<b>Q{index}. {q}</b>",
                    question_style,
                )
            )

            if answer_points:

                question_block.append(
                    Paragraph(
                        "<b>Answer Points:</b>",
                        answer_style,
                    )
                )

                for point in answer_points:

                    question_block.append(
                        Paragraph(
                            f"• {point}",
                            answer_style,
                        )
                    )

            story.append(
                KeepTogether(question_block)
            )

    # --------------------------------------------------
    # 7. QUICK REVISION
    # --------------------------------------------------

    revision = notes.get("quick_revision", [])

    if revision:

        story.append(
            Paragraph(
                "7. Quick Revision",
                section_style,
            )
        )

        for point in revision:

            story.append(
                Paragraph(
                    f"✓ {point}",
                    bullet_style,
                )
            )

    # --------------------------------------------------
    # PAGE NUMBER
    # --------------------------------------------------

    def add_page_number(canvas, document):

        canvas.saveState()

        canvas.setFont("Helvetica", 8)

        canvas.drawCentredString(
            A4[0] / 2,
            10 * mm,
            f"AI Learning Companion • Page {document.page}",
        )

        canvas.restoreState()

    document.build(
        story,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number,
    )