from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

# Colores corporativos
PRIMARY = colors.HexColor('#1a1a2e')
SECONDARY = colors.HexColor('#16213e')
ACCENT = colors.HexColor('#0f3460')
HIGHLIGHT = colors.HexColor('#e94560')
TEXT = colors.HexColor('#2d3e50')
TEXT_LIGHT = colors.HexColor('#5a6c7d')
WHITE = colors.white
BORDER = colors.HexColor('#e1e4e6')

# Configuración del documento
output_path = "David_Sanchez_Lavado_CV.pdf"
doc = SimpleDocTemplate(
    output_path,
    pagesize=A4,
    rightMargin=15*mm,
    leftMargin=15*mm,
    topMargin=15*mm,
    bottomMargin=15*mm
)

# Estilos personalizados
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name='NameStyle',
    parent=styles['Normal'],
    fontSize=22,
    textColor=PRIMARY,
    spaceAfter=3,
    fontName='Helvetica-Bold',
    leading=26
))

styles.add(ParagraphStyle(
    name='TitleStyle',
    parent=styles['Normal'],
    fontSize=11,
    textColor=TEXT_LIGHT,
    spaceAfter=10,
    fontName='Helvetica'
))

styles.add(ParagraphStyle(
    name='SectionTitleStyle',
    parent=styles['Normal'],
    fontSize=12,
    textColor=PRIMARY,
    spaceAfter=6,
    spaceBefore=6,
    fontName='Helvetica-Bold'
))

styles.add(ParagraphStyle(
    name='JobTitleStyle',
    parent=styles['Normal'],
    fontSize=10.5,
    textColor=PRIMARY,
    spaceAfter=2,
    fontName='Helvetica-Bold'
))

styles.add(ParagraphStyle(
    name='JobDateStyle',
    parent=styles['Normal'],
    fontSize=8.5,
    textColor=HIGHLIGHT,
    spaceAfter=2,
    fontName='Helvetica-Bold'
))

styles.add(ParagraphStyle(
    name='NormalStyle',
    fontSize=9,
    textColor=TEXT,
    leading=12,
    spaceAfter=4
))

styles.add(ParagraphStyle(
    name='SmallStyle',
    fontSize=8,
    textColor=TEXT_LIGHT,
    leading=10,
    spaceAfter=2
))

# Contenido del documento
story = []

# ===== HEADER =====
header_data = [
    [
        Paragraph('<font size=22><b>David Sánchez Lavado</b></font>', styles['NormalStyle']),
        ''
    ]
]
header_table = Table(header_data, colWidths=[200*mm, 40*mm])
header_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (0, 0), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 0),
    ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
]))
story.append(header_table)

# Título profesional
story.append(Paragraph('<font size=9.5 color="#5a6c7d">Técnico Superior en Desarrollo de Aplicaciones Multiplataforma</font>', styles['NormalStyle']))

# Contacto
contact_text = '<font size=8><b>Ubicación:</b> Alcalá de Henares, Madrid | <b>Tel:</b> +34 691 25 98 46 | <b>Email:</b> lavadosanchez.d@gmail.com</font>'
story.append(Paragraph(contact_text, styles['SmallStyle']))
story.append(Spacer(1, 3*mm))

# ===== PERFIL PROFESIONAL =====
story.append(Paragraph('PERFIL PROFESIONAL', styles['SectionTitleStyle']))
profile_text = ('Técnico especializado en desarrollo de aplicaciones con sólida formación en lenguajes '
                'multiplataforma. Orientado a resultados, proactivo y comprometido con la excelencia técnica. '
                'Experiencia práctica en administración de infraestructuras, gestión de redes y soporte técnico. '
                'Buscando contribuir en equipos innovadores que valoren el aprendizaje continuo.')
story.append(Paragraph(profile_text, styles['NormalStyle']))
story.append(Spacer(1, 3*mm))

# ===== EXPERIENCIA =====
story.append(Paragraph('EXPERIENCIA PROFESIONAL', styles['SectionTitleStyle']))

# Grupo Gestyde
story.append(Paragraph('Becario — Grupo Gestyde', styles['JobTitleStyle']))
story.append(Paragraph('Febrero 2026 — Presente', styles['JobDateStyle']))
gestyde_items = ['Soporte y mantenimiento de equipos informáticos en entorno corporativo',
                 'Administración de infraestructuras y gestión de redes',
                 'Participación activa en proyectos internos y mejora continua']
for item in gestyde_items:
    story.append(Paragraph(f'• {item}', styles['NormalStyle']))
story.append(Spacer(1, 2*mm))

# PRG Retail
story.append(Paragraph('Técnico Informático en Prácticas — PRG Retail Group', styles['JobTitleStyle']))
story.append(Paragraph('Marzo 2024 — Junio 2024', styles['JobDateStyle']))
prg_items = ['Montaje, configuración y mantenimiento de equipos informáticos',
             'Gestión de servidores Windows Server, clonaciones y discos duros',
             'Administración de redes locales y soporte técnico a usuarios']
for item in prg_items:
    story.append(Paragraph(f'• {item}', styles['NormalStyle']))
story.append(Spacer(1, 3*mm))

# ===== FORMACIÓN =====
story.append(Paragraph('FORMACIÓN ACADÉMICA', styles['SectionTitleStyle']))

# Técnico Superior
story.append(Paragraph('<b>Técnico Superior en Desarrollo de Aplicaciones Multiplataforma</b> <font color="#e94560"><b>[En curso]</b></font>', styles['NormalStyle']))
story.append(Paragraph('I.E.S. Alonso de Avellaneda — Alcalá de Henares', styles['SmallStyle']))
story.append(Paragraph('<b>Tecnologías:</b> Java · Python · C# · Kotlin · SQL/PL-SQL · GitHub · Android', styles['SmallStyle']))
story.append(Paragraph('<b>Proyecto:</b> Aplicación Java de gestión integral de series y películas', styles['SmallStyle']))
story.append(Spacer(1, 2*mm))

# Técnico Medio
story.append(Paragraph('<b>Técnico Medio en Sistemas Microinformáticos y Redes</b> <font color="#0f3460"><b>[2024]</b></font>', styles['NormalStyle']))
story.append(Paragraph('I.E.S. Alonso de Avellaneda — Alcalá de Henares', styles['SmallStyle']))
story.append(Paragraph('<b>Especialidades:</b> Ubuntu Linux, administración de servidores, redes locales, Windows Server', styles['SmallStyle']))
story.append(Paragraph('<b>Proyecto:</b> Infraestructura de múltiples servidores interconectados en Windows', styles['SmallStyle']))
story.append(Spacer(1, 3*mm))

# ===== COMPETENCIAS =====
story.append(Paragraph('COMPETENCIAS', styles['SectionTitleStyle']))

# Tabla de competencias técnicas y blandas
comp_data = [
    ['<b>Técnicas:</b> Java, Python, C#, Kotlin, SQL, GitHub,\nWindows Server, Linux, Redes TCP/IP, Android',
     '<b>Blandas:</b> Trabajo en equipo, Comunicación,\nResolución de problemas, Proactividad, Creatividad']
]
comp_table = Table(comp_data, colWidths=[90*mm, 90*mm])
comp_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f0f4f8')),
    ('FONT', (0, 0), (-1, -1), 'Helvetica', 8),
    ('LINEABOVE', (0, 0), (-1, -1), 0.5, ACCENT),
    ('LINEBELOW', (0, 0), (-1, -1), 0.5, ACCENT),
]))
story.append(comp_table)
story.append(Spacer(1, 3*mm))

# ===== IDIOMAS =====
story.append(Paragraph('IDIOMAS', styles['SectionTitleStyle']))
idiomas_data = [
    ['<b>Español</b> — Nativo', '<b>Inglés</b> — B2 (Comunicación profesional)']
]
idiomas_table = Table(idiomas_data, colWidths=[90*mm, 90*mm])
idiomas_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 0),
    ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ('FONT', (0, 0), (-1, -1), 'Helvetica', 9),
]))
story.append(idiomas_table)

# ===== FOOTER =====
story.append(Spacer(1, 6*mm))
footer_text = '<font size=7 color="#5a6c7d">LinkedIn: https://es.linkedin.com/in/david-sánchez-lavado-116332388 | © 2026 David Sánchez Lavado</font>'
story.append(Paragraph(footer_text, styles['SmallStyle']))

# Generar PDF
if __name__ == '__main__':
    doc.build(story)
    print(f'PDF profesional generado: {output_path}')
