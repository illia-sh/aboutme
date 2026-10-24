from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'illia-shpak-cv.pdf'
INK = colors.HexColor('#18202c')
MUTED = colors.HexColor('#495465')
ACCENT = colors.HexColor('#165879')
styles = {
    'name': ParagraphStyle('Name', fontName='Helvetica-Bold', fontSize=27, leading=31, textColor=INK, spaceAfter=4),
    'role': ParagraphStyle('Role', fontName='Helvetica', fontSize=12, leading=16, textColor=ACCENT, spaceAfter=6),
    'links': ParagraphStyle('Links', fontName='Helvetica', fontSize=8, leading=12, textColor=MUTED, spaceAfter=10),
    'body': ParagraphStyle('Body', fontName='Helvetica', fontSize=9.1, leading=12.7, textColor=INK, spaceAfter=7),
    'section': ParagraphStyle('Section', fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=ACCENT, spaceBefore=9, spaceAfter=7),
    'job': ParagraphStyle('Job', fontName='Helvetica-Bold', fontSize=9.6, leading=13, textColor=INK, spaceAfter=2),
    'meta': ParagraphStyle('Meta', fontName='Helvetica', fontSize=8.1, leading=11, textColor=MUTED, spaceAfter=4),
    'bullet': ParagraphStyle('Bullet', fontName='Helvetica', fontSize=8.9, leading=12.2, textColor=INK, leftIndent=10, firstLineIndent=-8, spaceAfter=3),
    'small': ParagraphStyle('Small', fontName='Helvetica', fontSize=8.5, leading=12, textColor=INK, spaceAfter=5),
}

def p(text, style='body'):
    return Paragraph(text, styles[style])

story = [
    p('ILLIA SHPAK', 'name'),
    p('Engineering Leader | Platform, Reliability &amp; Security', 'role'),
    p('London / Dubai | Working globally<br/><link href="https://www.linkedin.com/in/illiash/" color="#165879">linkedin.com/in/illiash</link>  |  <link href="https://github.com/illia-sh" color="#165879">github.com/illia-sh</link>  |  <link href="https://illia-sh.github.io/aboutme/" color="#165879">illia-sh.github.io/aboutme</link>', 'links'),
    HRFlowable(width='100%', thickness=.7, color=colors.HexColor('#ccd5df'), spaceAfter=10),
    p('Hands-on engineering leader with 15+ years across fintech, banking, fashion, and travel. Builds distributed teams and connects platform engineering, security, developer experience, and cloud strategy with business growth. Open to CTO, VP Engineering, and Head of Platform opportunities.'),
    p('SELECTED IMPACT', 'section'),
    p('<b>Lean:</b> grew DevOps &amp; SRE from 2 to 8 across four regions; reduced infrastructure spend by 50%; supported the business from seed through Series B.<br/><b>DREST:</b> saved $500K through re-architecture; moved deployments from weekly to multiple times per hour.', 'small'),
    p('EXPERIENCE', 'section'),
]

jobs = [
    ('Head of DevOps &amp; SRE', 'Lean Technologies | London / Dubai / Riyadh | 2022-Present', [
        'Led multi-cloud infrastructure, FinOps governance, developer self-service, and infrastructure controls supporting regulated operations and SAMA licensing.',
        'Designed business continuity and disaster recovery across OCI, GCP, and AWS. Supported a platform serving 250+ clients and processing $2B+ in transactions.'
    ]),
    ('VP Cloud / Systems Architect', 'JPMorgan Chase | London | 2021-2022', [
        'Contributed to a global digital call center platform: real-time data integration, WebRTC quality metrics, and intelligent call routing.',
        'The solution was presented at AWS re:Invent 2022 as reference architecture.'
    ]),
    ('Head of DevOps &amp; Security', 'DREST | London | 2019-2021', [
        'Reported to the CEO/CTO. Identified infrastructure inefficiencies and led a full-stack migration, saving $500K and increasing deployment frequency.'
    ]),
    ('Lead DevOps Engineer', 'Burberry, via EPAM | London | 2017-2019', [
        'Reduced infrastructure costs by 40%; managed GitLab for 150+ engineers; completed AWS security remediation in 3 weeks against a 2-month plan.'
    ]),
    ('Senior DevOps / SRE Engineer', 'Thomas Cook, via EPAM | Minsk / London | 2011-2017', [
        'Led 12 engineers. Migrated EU data centers covering 400+ instances with minimal downtime, and deployed monitoring for 500+ instances.'
    ]),
]
for title, meta, bullets in jobs:
    block = [p(title, 'job'), p(meta, 'meta')]
    block += [p('- ' + text, 'bullet') for text in bullets]
    block.append(Spacer(1, 7))
    story.append(KeepTogether(block))

story += [
    p('PRODUCTS &amp; EXPERTISE', 'section'),
    p('<b>DzeTruck:</b> B2B construction logistics marketplace with paying clients; Firebase, React, Flutter.<br/><b>Menu Scanner:</b> AI-powered dietary analysis; Next.js, Cloud Run, Google Cloud Vision.', 'small'),
    p('Team building, hiring, OKRs, executive collaboration, cloud contract negotiation, AWS, GCP, OCI, Kubernetes, Terraform, GitOps, FinOps, observability, security, and disaster recovery.', 'small'),
    p('CREDENTIALS &amp; CONTINUED LEARNING', 'section'),
    p('AWS Solutions Architect - Associate | GCP Professional Cloud Architect | Chef Certified Developer<br/>Additional training: Google Project Management; Y Combinator Startup School; SRE: Measuring &amp; Managing Reliability; ELK Machine Learning.', 'small'),
]

def footer(canvas, doc):
    canvas.setFont('Helvetica', 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(40, 23, 'Illia Shpak | Engineering Leader')
    canvas.drawRightString(A4[0]-40, 23, str(doc.page))

doc = SimpleDocTemplate(str(DEST), pagesize=A4, rightMargin=40, leftMargin=40, topMargin=33, bottomMargin=36, title='Illia Shpak - Engineering Leader', author='Illia Shpak')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
reader = PdfReader(str(DEST))
print('CV:', len(reader.pages), 'page(s),', DEST.stat().st_size, 'bytes')
assert len(reader.pages) == 1, 'CV should fit one page'
assert all(s in reader.pages[0].extract_text() for s in ['ILLIA SHPAK','Lean Technologies','JPMorgan Chase','DREST','Burberry','Thomas Cook','CREDENTIALS'])
