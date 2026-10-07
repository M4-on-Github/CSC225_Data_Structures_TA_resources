"""Create print PDFs from the diagnostic Word paragraphs using ReportLab.

This is a portable print layout, not a native Word pagination check.
Requires python-docx and reportlab. Rebuild DOCX files first.
"""
from pathlib import Path
from html import escape
from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph as WordParagraph
from docx.table import Table as WordTable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Table, TableStyle
from reportlab.lib import colors

ROOT = Path(__file__).resolve().parents[1]
FONTS = Path('C:/Windows/Fonts')
if (FONTS / 'arial.ttf').exists():
    for name, file in [('Body', 'arial.ttf'), ('Bold', 'arialbd.ttf'), ('Code', 'consola.ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(FONTS / file)))
    BODY, BOLD, CODE = 'Body', 'Bold', 'Code'
else:
    BODY, BOLD, CODE = 'Helvetica', 'Helvetica-Bold', 'Courier'


def build(stem):
    source = Document(ROOT / 'diagnostic' / (stem + '.docx'))
    flow = []
    for element in source.element.body:
        if element.tag == qn('w:tbl'):
            word_table = WordTable(element, source)
            rows = []
            for r, row in enumerate(word_table.rows):
                cells = []
                for c, cell in enumerate(row.cells):
                    style = ParagraphStyle('cell', fontName=BOLD if r == 0 else BODY,
                                           fontSize=12, leading=13, alignment=0 if c == 0 else 1)
                    cells.append(Paragraph(escape(cell.text), style))
                rows.append(cells)
            table = Table(rows, colWidths=[col.width.pt for col in word_table.columns],
                          repeatRows=1, hAlign='LEFT', spaceAfter=5)
            table.setStyle(TableStyle([
                ('GRID', (0, 0), (-1, -1), 0.6, colors.HexColor('#D9D9D9')),
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#E8E8E8')),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('LEFTPADDING', (0, 0), (-1, -1), 5),
                ('RIGHTPADDING', (0, 0), (-1, -1), 5),
                ('TOPPADDING', (0, 0), (-1, -1), 6),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ]))
            flow.append(table)
            continue
        if element.tag != qn('w:p'):
            continue
        p = WordParagraph(element, source)
        if any(b.get(qn('w:type')) == 'page' for b in p._p.iter(qn('w:br'))):
            flow.append(PageBreak())
            continue
        if not p.text:
            continue
        name = p.style.name
        is_code = bool(p.runs and p.runs[0].font.name == 'Consolas')
        size = {'Title': 22, 'Heading 1': 16, 'Heading 2': 12}.get(name, 11 if is_code else 12)
        font = CODE if is_code else BOLD if name in ('Title', 'Heading 1', 'Heading 2') else BODY
        style = ParagraphStyle(name, fontName=font, fontSize=size, leading=size * 1.08,
                               spaceBefore=8 if name.startswith('Heading') else 0,
                               spaceAfter=5, keepWithNext=bool(p.paragraph_format.keep_with_next),
                               allowWidows=0, allowOrphans=0)
        body = escape(p.text).replace('\n', '<br/>')
        if is_code:
            body = body.replace(' ', '&#160;')
        if name == 'List Bullet':
            body = '- ' + body
        flow.append(Paragraph(body, style))
    target = ROOT / 'diagnostic' / (stem + '.pdf')
    title = source.core_properties.title
    pdf = SimpleDocTemplate(str(target), pagesize=(612, 792), leftMargin=54, rightMargin=54,
                            topMargin=46.8, bottomMargin=46.8, title=title,
                            author='CSC225 TA resources', pageCompression=1)
    def footer(canvas, document):
        canvas.setFont(BODY, 9)
        canvas.drawString(54, 25, 'CSC225  |  ' + ('Foundation check' if stem == 'questions' else 'Answer guide'))
        canvas.drawRightString(558, 25, 'Page ' + str(document.page))
    pdf.build(flow, onFirstPage=footer, onLaterPages=footer)
    print(target)


if __name__ == '__main__':
    build('questions')
    build('answers')
