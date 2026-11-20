import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

def create_resume(output_path):
    # Page setup - 0.45 in margins (32.4pt) for clean 1-page layout
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=32
    )

    styles = getSampleStyleSheet()

    # Color Palette - Professional Tech Aesthetic
    C_PRIMARY = colors.HexColor('#0f172a')     # Slate 900
    C_SECONDARY = colors.HexColor('#2563eb')   # Blue 600
    C_TEXT = colors.HexColor('#1e293b')        # Slate 800
    C_MUTED = colors.HexColor('#475569')       # Slate 600
    C_LINE = colors.HexColor('#cbd5e1')        # Slate 300

    # Custom Typography Styles
    style_name = ParagraphStyle(
        'Name',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=22,
        alignment=TA_CENTER,
        textColor=C_PRIMARY,
        spaceAfter=4
    )

    style_contact = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        alignment=TA_CENTER,
        textColor=C_MUTED,
        spaceAfter=8
    )

    style_section_title = ParagraphStyle(
        'SectionTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=C_SECONDARY,
        spaceBefore=7,
        spaceAfter=2,
        textTransform='uppercase'
    )

    style_bold_left = ParagraphStyle(
        'BoldLeft',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11.5,
        textColor=C_PRIMARY
    )

    style_right = ParagraphStyle(
        'RightText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        alignment=TA_RIGHT,
        textColor=C_MUTED
    )

    style_right_bold = ParagraphStyle(
        'RightTextBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        alignment=TA_RIGHT,
        textColor=C_PRIMARY
    )

    style_sub = ParagraphStyle(
        'SubText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        textColor=C_MUTED
    )

    style_bullet = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=10.8,
        textColor=C_TEXT,
        leftIndent=10,
        firstLineIndent=-6,
        spaceAfter=2
    )

    style_skill_label = ParagraphStyle(
        'SkillLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=C_PRIMARY
    )

    style_skill_val = ParagraphStyle(
        'SkillVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=C_TEXT
    )

    story = []

    # 1. HEADER
    story.append(Paragraph("RAJVIR SINGH SANDHU", style_name))
    contact_line1 = (
        "Bengaluru, Karnataka, India &bull; "
        "<b>Email:</b> rajvirssandhu007@gmail.com &bull; "
        "<b>College:</b> 1ms25ci099@msrit.edu"
    )
    contact_line2 = (
        "<b>Portfolio:</b> rajvirsinghsandhu07.github.io &bull; "
        "<b>GitHub:</b> github.com/RajvirSinghSandhu07 &bull; "
        "<b>LinkedIn:</b> in/rajvir-singh-sandhu-5b324b2a5"
    )
    story.append(Paragraph(f"{contact_line1}<br/>{contact_line2}", style_contact))
    story.append(HRFlowable(width="100%", thickness=1, color=C_LINE, spaceBefore=0, spaceAfter=4))

    # 2. EDUCATION
    story.append(Paragraph("Education", style_section_title))
    story.append(HRFlowable(width="100%", thickness=0.5, color=C_SECONDARY, spaceBefore=0, spaceAfter=4))

    edu_table_data = [
        [
            Paragraph("<b>Ramaiah Institute of Technology (MSRIT)</b> — Bengaluru, India", style_bold_left),
            Paragraph("Sept 2025 – Present (3rd Semester)", style_right)
        ],
        [
            Paragraph("<i>B.E. in Computer Science and Engineering (Artificial Intelligence & Machine Learning)</i>", style_sub),
            Paragraph("<b>Cumulative 1st Year CGPA: 9.72 / 10.0</b>", style_right_bold)
        ]
    ]
    t_edu = Table(edu_table_data, colWidths=[380, 160])
    t_edu.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_edu)
    story.append(Paragraph("&bull; <b>Relevant Coursework:</b> Data Structures &amp; Algorithms (C++), Object-Oriented Programming (Java/C++), AI &amp; Machine Learning Foundations, Web Technologies, Database Concepts.", style_bullet))
    story.append(Spacer(1, 4))

    # 3. TECHNICAL SKILLS
    story.append(Paragraph("Technical Skills", style_section_title))
    story.append(HRFlowable(width="100%", thickness=0.5, color=C_SECONDARY, spaceBefore=0, spaceAfter=4))

    skills_data = [
        [Paragraph("<b>Programming Languages:</b>", style_skill_label), Paragraph("C++ (Primary DSA), Python (AI/ML &amp; Automation), Java, JavaScript (ES6+), HTML5, CSS3", style_skill_val)],
        [Paragraph("<b>Frameworks &amp; Tools:</b>", style_skill_label), Paragraph("FastAPI, React, Next.js 14, Tailwind CSS, Bootstrap, Google OR-Tools CP-SAT, Leaflet GIS, Framer Motion", style_skill_val)],
        [Paragraph("<b>Developer Tooling:</b>", style_skill_label), Paragraph("Git, GitHub (Version Control &amp; Actions), VS Code, Vercel, RESTful APIs, Linux/Bash", style_skill_val)],
        [Paragraph("<b>Core CS Competencies:</b>", style_skill_label), Paragraph("Data Structures &amp; Algorithms, Constraint Optimization, Modular Frontend Architecture, Rapid Prototyping", style_skill_val)]
    ]
    t_skills = Table(skills_data, colWidths=[135, 405])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_skills)
    story.append(Spacer(1, 4))

    # 4. FEATURED PROJECTS & HACKATHONS
    story.append(Paragraph("Featured Projects &amp; Hackathon Prototypes", style_section_title))
    story.append(HRFlowable(width="100%", thickness=0.5, color=C_SECONDARY, spaceBefore=0, spaceAfter=4))

    # Project 1: Raksha-Block
    p1_head = [
        [Paragraph("<b>Raksha-Block: AI-Powered Railway Maintenance Planning</b> | <i>FastAPI, CP-SAT, Leaflet GIS, Python</i>", style_bold_left),
         Paragraph("<b>SIH 2026 — Screening Cleared</b>", style_right_bold)]
    ]
    t_p1 = Table(p1_head, colWidths=[370, 170])
    t_p1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p1)
    story.append(Paragraph("&bull; Tackled Indian Railways problem statement SIH26027 to eliminate track possession conflicts across Engineering, S&amp;T, and TRD.", style_bullet))
    story.append(Paragraph("&bull; Built an automated block-bundling engine using Google OR-Tools CP-SAT constraint optimization with a 2D GIS Leaflet map across the Delhi-Howrah corridor; cleared institutional screening at MSRIT.", style_bullet))
    story.append(Spacer(1, 3))

    # Project 2: Omni Link
    p2_head = [
        [Paragraph("<b>Omni Link: Autonomous Humanitarian Logistics Platform</b> | <i>Next.js 14, Tailwind, Framer Motion, Recharts</i>", style_bold_left),
         Paragraph("<b>Google Hackathon (MSRIT) — Top 10</b>", style_right_bold)]
    ]
    t_p2 = Table(p2_head, colWidths=[370, 170])
    t_p2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p2)
    story.append(Paragraph("&bull; Architected an autonomous emergency aid operations dashboard for Team AlgoRythms in MSRIT's intra-college Google Hackathon, advancing to Round 2.", style_bullet))
    story.append(Paragraph("&bull; Implemented an Autonomous Dispatch HUD with prompt parsing, proximity routing, Bengaluru crisis hotspot overlay, and interactive partner network graphs.", style_bullet))
    story.append(Spacer(1, 3))

    # Project 3: Elevate
    p3_head = [
        [Paragraph("<b>Elevate: AI-Powered Academic Companion Platform</b> | <i>React, TypeScript, Tailwind CSS, Vercel</i>", style_bold_left),
         Paragraph("<b>Deployed: elevate-weld-eight.vercel.app</b>", style_right)]
    ]
    t_p3 = Table(p3_head, colWidths=[370, 170])
    t_p3.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p3)
    story.append(Paragraph("&bull; Engineered a student productivity ecosystem aligned with UN SDG 4 (Quality Education) to reduce exam anxiety and syllabus fragmentation.", style_bullet))
    story.append(Paragraph("&bull; Developed proprietary 'CGPA Fixer / Planner' score projection tool, smart task management, syllabus tracking, and focus timers.", style_bullet))
    story.append(Spacer(1, 3))

    # Project 4: Commercial Web Enablement (GOAT & Gym)
    p4_head = [
        [Paragraph("<b>Commercial Web Systems: GOAT Gaming Cafe &amp; Gym Web</b> | <i>HTML5, CSS3, JavaScript, WhatsApp API</i>", style_bold_left),
         Paragraph("<b>Client &amp; Production Deployments</b>", style_right)]
    ]
    t_p4 = Table(p4_head, colWidths=[370, 170])
    t_p4.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p4)
    story.append(Paragraph("&bull; <b>GOAT Gaming Cafe:</b> Developed a responsive multi-branch web portal for an esports gaming center featuring live console availability grids, WhatsApp VIP slot booking funnel, and an interactive 'Hall of Legends' competitive leaderboard.", style_bullet))
    story.append(Paragraph("&bull; <b>Gym-Web Platform:</b> Created a modern 5-page fitness platform with interactive membership plans, student discount calculator, integrated BMI health assessment, and WhatsApp trial scheduling funnel.", style_bullet))
    story.append(Spacer(1, 3))

    # Project 5: FinMate
    p5_head = [
        [Paragraph("<b>FinMate: Smart Student Personal Finance App</b> | <i>React, Next.js, Interactive State, Vercel</i>", style_bold_left),
         Paragraph("<b>Deployed: fin-mate-two.vercel.app</b>", style_right)]
    ]
    t_p5 = Table(p5_head, colWidths=[370, 170])
    t_p5.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
    story.append(t_p5)
    story.append(Paragraph("&bull; Designed a modern budgeting application featuring customizable spending 'Pockets' (Food, Travel, Bills), peer expense splitting, and gamified saving milestones with badge rewards.", style_bullet))
    story.append(Spacer(1, 4))

    # 5. HONORS & LEADERSHIP
    story.append(Paragraph("Honors, Achievements &amp; Extracurricular Leadership", style_section_title))
    story.append(HRFlowable(width="100%", thickness=0.5, color=C_SECONDARY, spaceBefore=0, spaceAfter=4))

    story.append(Paragraph("&bull; <b>Google Hackathon Finalist (MSRIT):</b> Cleared Round 1 and advanced to Round 2 (Top 10 finish) in the intra-college Google Hackathon at MSRIT.", style_bullet))
    story.append(Paragraph("&bull; <b>Smart India Hackathon (SIH 2026):</b> Cleared intra-college screening with project Raksha-Block at Ramaiah Institute of Technology.", style_bullet))
    story.append(Paragraph("&bull; <b>Academic Distinction:</b> Achieved a 9.72 cumulative first-year CGPA at MSRIT across foundational engineering coursework.", style_bullet))
    story.append(Paragraph("&bull; <b>Indian Music Team (IMT) — MSRIT:</b> Selected through rigorous college auditions as an official member, actively performing in musical compositions and ensemble events.", style_bullet))
    story.append(Paragraph("&bull; <b>Sports &amp; Athletic Discipline:</b> Dedicated regular sports and fitness practitioner; cultivates physical stamina, mental focus, and persistence.", style_bullet))

    doc.build(story)
    print(f"Resume generated successfully at: {output_path}")

if __name__ == "__main__":
    out_file = os.path.abspath("assets/resume.pdf")
    create_resume(out_file)
