"""Regenerate the two-page CV from experience on the original public page."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether, PageBreak
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'illia-shpak-cv.pdf'
INK = colors.HexColor('#18202c')
MUTED = colors.HexColor('#495465')
ACCENT = colors.HexColor('#165879')
styles = {
    'name': ParagraphStyle('Name', fontName='Helvetica-Bold', fontSize=27, leading=31, textColor=INK, spaceAfter=5),
    'role': ParagraphStyle('Role', fontName='Helvetica', fontSize=12, leading=17, textColor=ACCENT, spaceAfter=7),
    'links': ParagraphStyle('Links', fontName='Helvetica', fontSize=8.5, leading=12.5, textColor=MUTED, spaceAfter=11),
    'body': ParagraphStyle('Body', fontName='Helvetica', fontSize=10, leading=14, textColor=INK, spaceAfter=8),
    'section': ParagraphStyle('Section', fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=ACCENT, spaceBefore=12, spaceAfter=8, keepWithNext=True),
    'job': ParagraphStyle('Job', fontName='Helvetica-Bold', fontSize=11.5, leading=15.5, textColor=INK, spaceAfter=3, keepWithNext=True),
    'meta': ParagraphStyle('Meta', fontName='Helvetica', fontSize=9, leading=12.5, textColor=MUTED, spaceAfter=7, keepWithNext=True),
    'bullet': ParagraphStyle('Bullet', fontName='Helvetica', fontSize=9.7, leading=13.6, textColor=INK, leftIndent=10, firstLineIndent=-9, spaceAfter=5),
    'small': ParagraphStyle('Small', fontName='Helvetica', fontSize=9.1, leading=13, textColor=INK, spaceAfter=6),
    'continued': ParagraphStyle('Continued', fontName='Helvetica', fontSize=9, leading=13, textColor=MUTED, spaceAfter=12),
}

def p(text, style='body'):
    return Paragraph(text, styles[style])

def job(title, meta, bullets, stack):
    return [
        p(title, 'job'), p(meta, 'meta'),
        *[p('- ' + text, 'bullet') for text in bullets],
        p('<b>Environment:</b> ' + stack, 'small'), Spacer(1, 5),
    ]

story = [
    p('ILLIA SHPAK', 'name'),
    p('Engineering Leader | Platform, Reliability &amp; Security', 'role'),
    p('London / Dubai | Working globally<br/><link href="https://www.linkedin.com/in/illiash/" color="#165879">linkedin.com/in/illiash</link>  |  <link href="https://github.com/illia-sh" color="#165879">github.com/illia-sh</link>  |  <link href="https://illia-sh.github.io/aboutme/" color="#165879">illia-sh.github.io/aboutme</link>', 'links'),
    HRFlowable(width='100%', thickness=.7, color=colors.HexColor('#ccd5df'), spaceAfter=11),
    p('Engineering leader with 15+ years building platforms, security foundations, and delivery capabilities across fintech, banking, fashion, and travel. Combines hands-on architecture with distributed team leadership, executive collaboration, and multi-million dollar cloud contract negotiation. Focused on making growth reliable, secure, and economically sustainable.'),
    p('SELECTED BUSINESS IMPACT', 'section'),
    p('<b>50% lower infrastructure spend at Lean</b> through FinOps governance and cloud optimization.<br/><b>$500K saved at DREST</b> while moving deployments from weekly to multiple times per hour.<br/><b>Seed through Series B at Lean:</b> infrastructure supporting a platform serving 250+ clients and processing $2B+ in transactions.', 'small'),
    p('PROFESSIONAL EXPERIENCE', 'section'),
]

story += job('Head of DevOps &amp; SRE', 'Lean Technologies | London / Dubai / Riyadh | 2022-Present', [
    'Led platform infrastructure for a regulated MENA fintech from seed stage through a $33M Series A (Sequoia) and a $67.5M Series B (General Catalyst).',
    'Implemented FinOps governance, infrastructure optimization, and cloud contract negotiation, reducing infrastructure spend by 50%.',
    'Led infrastructure and security work supporting SAMA fintech licensing in Saudi Arabia, with CIS-hardened Kubernetes and cloud infrastructure.',
    'Designed and executed business continuity and disaster recovery across OCI, GCP, and AWS, with RPO=0 and RTO at or below 2 hours.',
    'Built golden paths and developer self-service platforms; achieved DORA Elite metrics and applied AI-assisted workflows to engineering operations.',
    'Built a distributed DevOps &amp; SRE function across four regions, growing from 2 to 8 engineers while supporting a platform serving 250+ clients, including Binance and Tabby.',
], 'GCP, OCI, AWS, Kubernetes, Terraform, Argo CD, Vault, FinOps, SAMA, CIS, BCP/DR')

story += job('VP Cloud / Systems Architect', 'JPMorgan Chase | London | 2021-2022', [
    'Contributed to the architecture of a global digital call center platform, with real-time data integration microservices and intelligent call routing.',
    'Built WebRTC quality-metrics pipelines. The solution was presented at AWS re:Invent 2022 as reference architecture.',
], 'AWS, Python, Kafka, Kinesis, Spinnaker, Terraform')

story += [PageBreak(), p('ILLIA SHPAK / EXPERIENCE &amp; CAPABILITIES', 'continued')]

story += job('Head of DevOps &amp; Security', 'DREST | London | 2019-2021', [
    'Reported to the CEO/CTO and led infrastructure and security work for the business.',
    'Identified inefficiencies and led a full-stack migration and re-architecture, saving $500K.',
    'Transformed deployments from weekly to multiple times per hour and implemented the AWS Well-Architected Framework.',
], 'AWS, EKS, CircleCI, Neptune, GraphQL, GDPR')

story += job('Lead DevOps Engineer', 'Burberry, via EPAM | London | 2017-2019', [
    'Reduced infrastructure costs by 40% and managed GitLab supporting 150+ engineers.',
    'Led AWS security hardening and completed remediation in 3 weeks against a 2-month plan.',
    'Worked across enterprise-scale ELK, Akamai CDN, and Kubernetes orchestration.',
], 'AWS, Kubernetes, Chef, ELK, Akamai')

story += job('Senior DevOps / SRE Engineer', 'Thomas Cook, via EPAM | Minsk / London | 2011-2017', [
    'Led a team of 12 engineers and migrated EU data centers covering 400+ instances with minimal downtime.',
    'Deployed monitoring for 500+ instances and delivered performance testing, database optimization, and automation at enterprise scale.',
], 'Linux, Puppet, Chef, Oracle, MySQL, Zabbix')

story += [
    p('LEADERSHIP &amp; TECHNICAL CAPABILITIES', 'section'),
    p('<b>Leadership:</b> distributed team building, 200+ technical interviews, OKRs/KPIs, executive collaboration, vendor negotiation, and engineering culture.<br/><b>Platform &amp; reliability:</b> multi-cloud architecture, GKE/EKS/OKE, GitOps, developer self-service, SLO/SLI frameworks, incident response, and validated failover runbooks.<br/><b>Security:</b> zero-trust networks, privileged access management, SOC/SIEM capability, CIS Level 1 hardening, and work across SAMA, CBUAE, ISO 27001, GDPR, and NIST.<br/><b>Operations:</b> FinOps, Prometheus, Grafana, OpenTelemetry, ELK, AI-assisted observability, LLM toolchains, and infrastructure automation.', 'small'),
    p('PRODUCTS BUILT', 'section'),
    p('<b><link href="https://landing.dzetruck.com" color="#165879">DzeTruck</link>:</b> B2B construction logistics marketplace connecting contractors with transport providers. Acquired paying B2B clients. Firebase, React, Flutter, and automated App Store / Google Play releases.<br/><b><link href="https://menu-scanner.com" color="#165879">Menu Scanner</link>:</b> AI-powered dietary analysis using computer vision and NLP. Next.js, GCP Cloud Run, Google Cloud Vision, and Vercel edge delivery.', 'small'),
    p('CREDENTIALS &amp; CONTINUED LEARNING', 'section'),
    p('AWS Solutions Architect - Associate | GCP Professional Cloud Architect | Chef Certified Developer<br/>Additional training: Google Project Management; Y Combinator Startup School; SRE: Measuring &amp; Managing Reliability; ELK Machine Learning.', 'small'),
]

def footer(canvas, doc):
    canvas.setFont('Helvetica', 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(40, 22, 'Illia Shpak | Engineering Leader')
    canvas.drawRightString(A4[0]-40, 22, f'{doc.page} / 2')

doc = SimpleDocTemplate(str(DEST), pagesize=A4, rightMargin=40, leftMargin=40, topMargin=34, bottomMargin=36, title='Illia Shpak - Engineering Leadership CV', author='Illia Shpak')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
reader = PdfReader(str(DEST))
texts = [page.extract_text() for page in reader.pages]
print('CV:', len(reader.pages), 'pages,', sum(len(t.split()) for t in texts), 'words,', DEST.stat().st_size, 'bytes')
assert len(reader.pages) == 2, 'CV must have two balanced pages'
assert all(s in texts[0] for s in ['ILLIA SHPAK', 'Lean Technologies', 'JPMorgan Chase'])
assert all(s in texts[1] for s in ['DREST', 'Burberry', 'Thomas Cook', 'PRODUCTS BUILT', 'CREDENTIALS'])
