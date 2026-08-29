from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# ---------- Page margins ----------
for section in doc.sections:
    section.top_margin    = Inches(0.5)
    section.bottom_margin = Inches(0.5)
    section.left_margin   = Inches(0.75)
    section.right_margin  = Inches(0.75)

# ---------- Remove default paragraph spacing ----------
style = doc.styles['Normal']
style.font.name = 'Garamond'
style.font.size = Pt(10)
from docx.oxml.ns import qn
pPr = style.paragraph_format._element.get_or_add_pPr()
spacing = OxmlElement('w:spacing')
spacing.set(qn('w:before'), '0')
spacing.set(qn('w:after'),  '0')
pPr.append(spacing)

def set_spacing(para, before=0, after=0, line=None):
    pf = para.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after  = Pt(after)
    if line:
        from docx.shared import Pt as P
        pf.line_spacing = P(line)

def add_run(para, text, bold=False, italic=False, size=10, color=None):
    run = para.add_run(text)
    run.bold   = bold
    run.italic = italic
    run.font.size = Pt(size)
    run.font.name = 'Garamond'
    if color:
        run.font.color.rgb = RGBColor(*color)
    return run

def add_section_heading(doc, title):
    p = doc.add_paragraph()
    set_spacing(p, before=6, after=1)
    run = p.add_run(title.upper())
    run.bold = True
    run.font.size = Pt(11)
    run.font.name = 'Garamond'
    # Bottom border (rule line)
    pPr = p._element.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'),   'single')
    bottom.set(qn('w:sz'),    '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '000000')
    pBdr.append(bottom)
    pPr.append(pBdr)
    return p

def add_subheading(doc, left_bold, right, left_sub_italic, right_sub_italic):
    # Row 1: bold left, right aligned date
    p = doc.add_paragraph()
    set_spacing(p, before=3, after=0)
    tab_stops = p.paragraph_format.tab_stops
    tab_stops.add_tab_stop(Inches(6.5), 2)  # right align
    add_run(p, left_bold, bold=True)
    p.add_run('\t')
    add_run(p, right)
    # Row 2: italic sub
    p2 = doc.add_paragraph()
    set_spacing(p2, before=0, after=0)
    tab_stops2 = p2.paragraph_format.tab_stops
    tab_stops2.add_tab_stop(Inches(6.5), 2)
    add_run(p2, left_sub_italic, italic=True)
    p2.add_run('\t')
    add_run(p2, right_sub_italic, italic=True)

def add_bullet(doc, text):
    p = doc.add_paragraph(style='List Bullet')
    set_spacing(p, before=0, after=1)
    p.paragraph_format.left_indent  = Inches(0.25)
    p.paragraph_format.first_line_indent = Inches(-0.15)
    run = p.add_run(text)
    run.font.size = Pt(9.5)
    run.font.name = 'Garamond'
    return p

def add_skills_line(doc, label, value):
    p = doc.add_paragraph()
    set_spacing(p, before=1, after=1)
    add_run(p, label, bold=True, size=9.5)
    add_run(p, value, size=9.5)

# ============================================================
# HEADING
# ============================================================
name_p = doc.add_paragraph()
name_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
set_spacing(name_p, before=0, after=2)
name_run = name_p.add_run('RICHARD EFFAH YEBOAH')
name_run.bold = True
name_run.font.size = Pt(20)
name_run.font.name = 'Garamond'

contact_p = doc.add_paragraph()
contact_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
set_spacing(contact_p, before=0, after=4)
add_run(contact_p,
    '(614) 290-4260  |  kkras5050@gmail.com  |  github.com/t4thick  |  '
    'linkedin.com/in/richard-effah-yeboah  |  Portfolio',
    size=9.5)

# ============================================================
# EDUCATION
# ============================================================
add_section_heading(doc, 'Education')
add_subheading(doc,
    'Grambling State University', 'Expected May 2028',
    'B.S. Computer Science (Sophomore)  |  GPA: 4.0/4.0', 'Ruston, Louisiana')

p = doc.add_paragraph()
set_spacing(p, before=4, after=0)
add_run(p, 'Honors: ', bold=True, size=9.5)
add_run(p, "President's List; CodePath & IBM Alumnus", size=9.5)

p2 = doc.add_paragraph()
set_spacing(p2, before=1, after=0)
add_run(p2, 'Relevant Coursework: ', bold=True, size=9.5)
add_run(p2, 'Data Structures, Algorithms, Software Engineering, Web Development, Database Systems, Cybersecurity', size=9.5)

# ============================================================
# EXPERIENCE
# ============================================================
add_section_heading(doc, 'Experience')

add_subheading(doc, 'Lovely Queen Mart', 'Jan 2025 – Present',
               'E-Commerce Developer', 'Remote')
add_bullet(doc, 'Built a full-stack e-commerce platform (React, Node.js, PostgreSQL) managing 100+ SKUs with secure payment integration and order-fulfillment workflows')
add_bullet(doc, 'Redesigned ordering flow and site UX, improving customer retention by ~20% and engagement across the platform')

add_subheading(doc, 'New Life International School', 'Jan 2024 – Dec 2024',
               'ICT Instructor & Data Administrator', 'Kronum, Kumasi, Ghana')
add_bullet(doc, 'Designed and delivered ICT curriculum with hands-on labs (Excel, productivity tools), improving student proficiency in core computing concepts')
add_bullet(doc, 'Managed and validated student records in Excel, streamlining data accuracy and retrieval for administration workflows')

add_subheading(doc, 'God First Printing Press', 'May 2024 – Nov 2024',
               'Graphic Designer', 'Kumasi, Ghana (Part-Time)')
add_bullet(doc, 'Produced print and digital marketing assets (flyers, banners, logos) in Photoshop; delivered on deadline with consistent brand quality')

# ============================================================
# PROJECTS
# ============================================================
add_section_heading(doc, 'Projects')

p = doc.add_paragraph()
set_spacing(p, before=3, after=0)
tab_stops = p.paragraph_format.tab_stops
tab_stops.add_tab_stop(Inches(6.5), 2)
add_run(p, 'Item7 Food Truck Ordering System', bold=True)
p.add_run('\t')
add_run(p, 'Jan 2025 – Apr 2025')

p2 = doc.add_paragraph()
set_spacing(p2, before=0, after=0)
add_run(p2, 'Python, Flask, PostgreSQL, SQLAlchemy, REST API, Redis, Vercel, Stripe  |  Live Demo  |  GitHub', italic=True, size=9.5)

add_bullet(doc, 'Engineered a full-stack ordering platform (Python, Flask, PostgreSQL, SQLAlchemy) with a relational data model for 50+ menu items, carts, and orders; implemented CRUD flows and server-side validation via RESTful endpoints')
add_bullet(doc, 'Built a role-based staff portal (4 roles) for order and operations management; integrated Stripe checkout with robust error handling and order state consistency')
add_bullet(doc, 'Implemented Redis caching and serverless deployment (Vercel) to improve API performance and scalability')

p = doc.add_paragraph()
set_spacing(p, before=3, after=0)
tab_stops = p.paragraph_format.tab_stops
tab_stops.add_tab_stop(Inches(6.5), 2)
add_run(p, 'DevCanvas (Portfolio Site)', bold=True)
p.add_run('\t')
add_run(p, 'Side Project')

p2 = doc.add_paragraph()
set_spacing(p2, before=0, after=0)
add_run(p2, 'Next.js, TypeScript, Tailwind CSS  |  GitHub', italic=True, size=9.5)

add_bullet(doc, 'Developed a responsive portfolio (Next.js, TypeScript, Tailwind CSS) with component-driven architecture to showcase projects and experience in a recruiter-scannable format')
add_bullet(doc, 'Optimized page structure for SEO and fast navigation; maintained content through reusable sections and consistent formatting')

# ============================================================
# TECHNICAL SKILLS
# ============================================================
add_section_heading(doc, 'Technical Skills')
add_skills_line(doc, 'Languages: ',           'Python, TypeScript, JavaScript, SQL, HTML/CSS')
add_skills_line(doc, 'Technologies/Frameworks: ', 'React, Next.js, Flask, Node.js, REST APIs, SQLAlchemy, PostgreSQL, Redis')
add_skills_line(doc, 'Tools: ',               'Git/GitHub, Vercel, Stripe API, Excel')
add_skills_line(doc, 'Concepts: ',            'Full-Stack Development, RESTful APIs, Relational Databases, Role-Based Access Control')

# ============================================================
# ACTIVITIES / LEADERSHIP
# ============================================================
add_section_heading(doc, 'Activities / Leadership')

add_subheading(doc, 'IBM SkillsBuild', 'May 2025 – Jun 2025',
               'IBM Scholar – Data Science Track', 'Virtual')
add_bullet(doc, 'Completed end-to-end data workflows in Python (Jupyter Notebook, Watson Studio); applied data wrangling and statistical analysis across multiple datasets to derive actionable insights')

add_subheading(doc, 'ColorStack', 'Sept 2024 – Present',
               'Member', 'Grambling State University')
add_bullet(doc, 'Active member in technical community; CodePath & IBM Alumnus; certifications in Web Development, AI, Cybersecurity, Data, and IBM Enterprise Design Thinking')

p = doc.add_paragraph()
set_spacing(p, before=3, after=0)
add_run(p, 'Clubs: ', bold=True, size=9.5)
add_run(p, 'Advocacy for Climate Change Education  |  ISSUP  |  SECURE+  |  African Student Association', size=9.5)

# ============================================================
out = r"c:\Users\tfott\OneDrive\Desktop\jakes template resume\resume.docx"
doc.save(out)
print(f"Saved: {out}")
