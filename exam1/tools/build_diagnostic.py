"""Build accessible Word copies from the two diagnostic Markdown sources.

Run from any directory with Python 3 and python-docx installed.
The Markdown files are the source of truth. PDF export is a separate step.
"""
from pathlib import Path
import re

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT

ROOT = Path(__file__).resolve().parents[1]


def inline(paragraph, text):
    for piece in re.split(r'(\[[^\]]+\]\([^)]+\))', text):
        match = re.fullmatch(r'\[([^\]]+)\]\(([^)]+)\)', piece)
        if not match:
            paragraph.add_run(piece.replace('`', ''))
            continue
        link = OxmlElement('w:hyperlink')
        link.set(qn('r:id'), paragraph.part.relate_to(match[2], RT.HYPERLINK, is_external=True))
        run = OxmlElement('w:r')
        props = OxmlElement('w:rPr')
        underline = OxmlElement('w:u')
        underline.set(qn('w:val'), 'single')
        props.append(underline)
        run.append(props)
        value = OxmlElement('w:t')
        value.text = match[1]
        run.append(value)
        link.append(run)
        paragraph._p.append(link)


def build(stem):
    doc = Document()
    section = doc.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = section.bottom_margin = Inches(0.65)
    section.left_margin = section.right_margin = Inches(0.75)
    normal = doc.styles['Normal']
    normal.font.name = 'Arial'
    normal.font.size = Pt(12)
    normal.font.color.rgb = RGBColor(0, 0, 0)
    normal.paragraph_format.space_after = Pt(5)
    normal.paragraph_format.line_spacing = 1.0
    for name, size in [('Title', 22), ('Heading 1', 16), ('Heading 2', 12)]:
        style = doc.styles[name]
        style.font.name = 'Arial'
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.font.bold = True
        style.paragraph_format.space_before = Pt(8 if name != 'Title' else 0)
        style.paragraph_format.space_after = Pt(5)
        style.paragraph_format.keep_with_next = True
    lang = OxmlElement('w:lang')
    lang.set(qn('w:val'), 'en-US')
    normal.element.get_or_add_rPr().append(lang)
    doc.core_properties.title = ('Exam 1 foundation check' if stem == 'questions'
                                 else 'Exam 1 foundation check answer guide')
    doc.core_properties.subject = 'CSC225 student practice and review routing'
    doc.core_properties.author = 'CSC225 TA resources'
    footer = section.footer.paragraphs[0]
    footer.add_run('CSC225  |  ' + ('Foundation check' if stem == 'questions' else 'Answer guide') + '  |  Page ')
    field = OxmlElement('w:fldSimple')
    field.set(qn('w:instr'), 'PAGE')
    footer._p.append(field)
    for run in footer.runs:
        run.font.size = Pt(9)
    lines = (ROOT / 'diagnostic' / (stem + '.md')).read_text(encoding='utf-8').splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        i += 1
        if not line:
            continue
        if line == '<!-- pagebreak -->':
            doc.add_page_break()
        elif line.startswith('```'):
            code = []
            while i < len(lines) and not lines[i].startswith('```'):
                code.append(lines[i])
                i += 1
            i += 1
            p = doc.add_paragraph()
            p.paragraph_format.keep_together = True
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.space_after = Pt(5)
            run = p.add_run('\n'.join(code))
            run.font.name = 'Consolas'
            run.font.size = Pt(11)
        elif line.startswith('# '):
            doc.add_paragraph(line[2:], 'Title')
        elif line.startswith('## '):
            doc.add_paragraph(line[3:], 'Heading 1')
        elif line.startswith('### '):
            doc.add_paragraph(line[4:], 'Heading 2')
        elif line.startswith('- '):
            inline(doc.add_paragraph(style='List Bullet'), line[2:])
        else:
            block = [line]
            while i < len(lines) and lines[i] and not lines[i].startswith(('#', '```', '<!--', '- ')):
                block.append(lines[i])
                i += 1
            p = doc.add_paragraph()
            inline(p, '\n'.join(block))
            p.paragraph_format.keep_together = True
            if stem == 'questions' and not line.startswith(('Answer:', 'Reason', 'Output:', 'Values of', 'Next:')):
                p.paragraph_format.keep_with_next = True
    target = ROOT / 'diagnostic' / (stem + '.docx')
    doc.save(target)
    print(target)


if __name__ == '__main__':
    build('questions')
    build('answers')
