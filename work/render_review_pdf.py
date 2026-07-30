from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    PageBreak,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "drafts" / "review-integrated.md"
FINAL_OUTPUT = ROOT / "output" / "pdf" / "succinct-filters-review-final.pdf"

font_path = Path("C:/Windows/Fonts/NotoSerifSC-VF.ttf")
pdfmetrics.registerFont(TTFont("ReviewCJK", str(font_path)))

styles = getSampleStyleSheet()
body = ParagraphStyle(
    "BodyCJK",
    parent=styles["BodyText"],
    fontName="ReviewCJK",
    fontSize=9.6,
    leading=14.6,
    spaceAfter=4.5,
    firstLineIndent=18,
    alignment=TA_LEFT,
)
heading = {
    1: ParagraphStyle("H1CJK", parent=body, fontSize=19, leading=25, spaceBefore=4, spaceAfter=12, textColor=colors.HexColor("#263746")),
    2: ParagraphStyle("H2CJK", parent=body, fontSize=14, leading=19, spaceBefore=12, spaceAfter=7, textColor=colors.HexColor("#314f67"), keepWithNext=True),
    3: ParagraphStyle("H3CJK", parent=body, fontSize=11.5, leading=16, spaceBefore=8, spaceAfter=5, textColor=colors.HexColor("#3f5f76"), keepWithNext=True),
}
code_style = ParagraphStyle("CodeCJK", parent=body, fontName="ReviewCJK", fontSize=7.8, leading=11, leftIndent=6, borderColor=colors.HexColor("#78909c"), borderWidth=0.6, borderPadding=5, backColor=colors.HexColor("#f5f7f8"))
table_cell = ParagraphStyle("TableCJK", parent=body, fontSize=6.6, leading=8.6, spaceAfter=0)
list_style = ParagraphStyle("ListCJK", parent=body, firstLineIndent=0, leftIndent=14, bulletIndent=2, spaceAfter=2.5)
cover_title = ParagraphStyle("CoverTitle", parent=body, fontSize=23, leading=34, alignment=TA_CENTER, textColor=colors.HexColor("#20384a"), firstLineIndent=0, spaceAfter=15)
cover_subtitle = ParagraphStyle("CoverSubtitle", parent=body, fontSize=14, leading=22, alignment=TA_CENTER, textColor=colors.HexColor("#496777"), firstLineIndent=0)
cover_meta = ParagraphStyle("CoverMeta", parent=body, fontSize=11, leading=20, alignment=TA_CENTER, firstLineIndent=0)


def inline(text: str) -> str:
    text = escape(text.strip())
    text = text.replace("**", "").replace("*", "").replace("`", "")
    symbol_replacements = {
        "⌈": "ceil(", "⌉": ")", "★": "*", "₀": "_0", "₁": "_1",
        "₂": "_2", "₃": "_3", "₄": "_4", "∘": "·",
        "Pătraşcu": "Patrascu", "Pătrașcu": "Patrascu",
    }
    for old, new in symbol_replacements.items():
        text = text.replace(old, new)
    citation_numbers = {
        "liu2020succinct": 1, "bloom1970space": 2, "carter1978membership": 3,
        "almeida2007scalable": 4, "guo2006dynamic": 5, "arbitman2010backyard": 6,
        "demaine2006dictionary": 7, "pagh2005optimal": 8, "pagh2013unknown": 9,
        "raman2003succinct": 10, "bender2012quotient": 11, "fan2014cuckoo": 12,
        "dayan2024aleph": 13, "kuszmaul2024dynamicfilters": 14,
        "kuszmaul2026resizable": 15,
    }
    for key, number in citation_numbers.items():
        text = text.replace(f"[{key}]", f"[{number}]")
    text = re.sub(r"(?:见|对应|依赖图：)?\s*(?:drafts|references|figures|notes|discussions)/[^\s，。；）]+\.md", "", text)
    text = text.replace("issue-stage-index", "阶段下标核查项")
    text = re.sub(r"\s+", " ", text)
    return text


def table_flowable(rows):
    width = 170 * mm
    columns = max(len(row) for row in rows)
    normalized = [row + [""] * (columns - len(row)) for row in rows]
    data = [[Paragraph(inline(cell), table_cell) for cell in row] for row in normalized]
    table = Table(data, colWidths=[width / columns] * columns, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "ReviewCJK"),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e9eef2")),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#8998a3")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return table


def parse_markdown(text: str):
    lines = text.splitlines()
    story = []
    paragraph = []
    code = []
    in_code = False

    def flush_paragraph():
        if paragraph:
            value = " ".join(item.strip() for item in paragraph)
            story.append(Paragraph(inline(value), body))
            paragraph.clear()

    # 首页标题和紧随其后的过程状态属于仓库工作记录；正式 PDF 使用独立封面。
    i = 0
    if lines and lines[0].startswith("# "):
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        if i < len(lines):
            i += 1
    while i < len(lines):
        line = lines[i]
        if line.startswith("## 附录 A"):
            flush_paragraph()
            break
        if line.startswith("完整 BibTeX 元数据见"):
            flush_paragraph()
            i += 1
            continue
        if line.startswith(("体系结构见", "完整状态机见", "同步图：", "操作流程图：", "对应 `notes/", "依赖图：")):
            flush_paragraph()
            i += 1
            continue
        if line.startswith("```"):
            flush_paragraph()
            if in_code:
                story.append(Preformatted("\n".join(code), code_style))
                code.clear()
            in_code = not in_code
            i += 1
            continue
        if in_code:
            code.append(line)
            i += 1
            continue
        if line.startswith("|") and i + 1 < len(lines) and lines[i + 1].startswith("|") and "---" in lines[i + 1]:
            flush_paragraph()
            rows = []
            rows.append([cell.strip() for cell in line.strip("|").split("|")])
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([cell.strip() for cell in lines[i].strip("|").split("|")])
                i += 1
            story.append(table_flowable(rows))
            story.append(Spacer(1, 4))
            continue
        if line.startswith("### "):
            flush_paragraph(); story.append(Paragraph(inline(line[4:]), heading[3])); i += 1; continue
        if line.startswith("## "):
            flush_paragraph(); story.append(Paragraph(inline(line[3:]), heading[2])); i += 1; continue
        if line.startswith("# "):
            flush_paragraph(); story.append(Paragraph(inline(line[2:]), heading[1])); i += 1; continue
        if line.strip() == "---":
            flush_paragraph(); story.append(Spacer(1, 5)); i += 1; continue
        if not line.strip():
            flush_paragraph(); i += 1; continue
        stripped = line.lstrip()
        is_numbered = len(stripped.split(".", 1)) == 2 and stripped.split(".", 1)[0].isdigit()
        if line.startswith("- ") or is_numbered:
            flush_paragraph()
            if is_numbered:
                number, content = stripped.split(".", 1)
                story.append(Paragraph(inline(content), list_style, bulletText=f"{number}."))
            else:
                story.append(Paragraph(inline(line[2:]), list_style, bulletText="•"))
            i += 1
            continue
        paragraph.append(line)
        i += 1
    flush_paragraph()
    return story


def cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#20384a"))
    canvas.rect(0, A4[1] - 8 * mm, A4[0], 8 * mm, fill=1, stroke=0)
    canvas.restoreState()


def body_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("ReviewCJK", 8)
    canvas.setFillColor(colors.HexColor("#667782"))
    canvas.drawString(20 * mm, A4[1] - 11 * mm, "Succinct Filters for Sets of Unknown Sizes：论文 Review")
    canvas.setStrokeColor(colors.HexColor("#b8c3ca"))
    canvas.setLineWidth(0.4)
    canvas.line(20 * mm, A4[1] - 13 * mm, A4[0] - 20 * mm, A4[1] - 13 * mm)
    canvas.drawCentredString(A4[0] / 2, 9 * mm, f"{doc.page - 1}")
    canvas.restoreState()


FINAL_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
doc = BaseDocTemplate(
    str(FINAL_OUTPUT),
    pagesize=A4,
    leftMargin=20 * mm,
    rightMargin=20 * mm,
    topMargin=20 * mm,
    bottomMargin=18 * mm,
    title="Succinct Filters for Sets of Unknown Sizes：论文 Review",
    author="刘威、张书铖、陈戚",
    subject="Liu, Yin and Yu, ICALP 2020 paper review",
)
cover_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="cover")
body_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body")
doc.addPageTemplates([
    PageTemplate(id="cover", frames=[cover_frame], onPage=cover_page, autoNextPageTemplate="body"),
    PageTemplate(id="body", frames=[body_frame], onPage=body_page),
])

story = [
    Spacer(1, 42 * mm),
    Paragraph("Succinct Filters for Sets of Unknown Sizes", cover_title),
    Paragraph("论文 Review", cover_subtitle),
    Spacer(1, 27 * mm),
    Paragraph("刘威（A）　张书铖（B）　陈戚（C）", cover_meta),
    Spacer(1, 10 * mm),
    Paragraph("评述论文：Liu, Yin and Yu, ICALP 2020", cover_meta),
    Paragraph("最终提交版 · 2026 年 7 月", cover_meta),
    PageBreak(),
]
story.extend(parse_markdown(SOURCE.read_text(encoding="utf-8")))
doc.build(story)
print(FINAL_OUTPUT)
