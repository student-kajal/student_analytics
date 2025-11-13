from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from models import Course
from datetime import datetime
import os

def generate_student_report(student, grades):
    """Generate comprehensive PDF report for student performance"""
    
    # Create reports directory if not exists
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    filename = f"reports/student_{student.enrollment_no}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    
    # Container for elements
    elements = []
    styles = getSampleStyleSheet()
    
    # Title
    title = Paragraph(f"<b>Student Performance Report</b>", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 0.3*inch))
    
    # Report generated date
    date_para = Paragraph(f"<i>Generated on: {datetime.now().strftime('%B %d, %Y')}</i>", styles['Normal'])
    elements.append(date_para)
    elements.append(Spacer(1, 0.3*inch))
    
    # Student Info Section
    info_heading = Paragraph("<b>Student Information</b>", styles['Heading2'])
    elements.append(info_heading)
    elements.append(Spacer(1, 0.1*inch))
    
    student_info = [
        ['Name:', student.name],
        ['Enrollment No:', student.enrollment_no],
        ['Email:', student.email],
        ['Branch:', student.branch],
        ['Current Semester:', str(student.semester)]
    ]
    
    info_table = Table(student_info, colWidths=[2*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#667eea')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
    ]))
    
    elements.append(info_table)
    elements.append(Spacer(1, 0.5*inch))
    
    # Grades Table Section
    grade_heading = Paragraph("<b>Academic Performance</b>", styles['Heading2'])
    elements.append(grade_heading)
    elements.append(Spacer(1, 0.15*inch))
    
    grade_data = [['S.No', 'Course Code', 'Course Name', 'Marks', 'Grade', 'Semester']]
    
    total_marks = 0
    for idx, grade in enumerate(grades, 1):
        course = Course.query.get(grade.course_id)
        grade_data.append([
            str(idx),
            course.code,
            course.name,
            f"{grade.marks:.1f}",
            grade.grade,
            str(grade.semester)
        ])
        total_marks += grade.marks
    
    avg_marks = total_marks / len(grades) if grades else 0
    
    # Performance summary
    if avg_marks >= 80:
        performance = "Excellent"
    elif avg_marks >= 60:
        performance = "Good"
    elif avg_marks >= 40:
        performance = "Average"
    else:
        performance = "Needs Improvement"
    
    grade_data.append(['', '', 'Average Marks', f'{avg_marks:.2f}', '', ''])
    grade_data.append(['', '', 'Performance', performance, '', ''])
    
    grade_table = Table(grade_data, colWidths=[0.5*inch, 1.2*inch, 2.3*inch, 1*inch, 0.8*inch, 1*inch])
    grade_table.setStyle(TableStyle([
        # Header styling
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        
        # Data rows styling
        ('BACKGROUND', (0, 1), (-1, -3), colors.beige),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -3), 1, colors.black),
        ('TOPPADDING', (0, 1), (-1, -3), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -3), 8),
        
        # Summary rows styling
        ('FONTNAME', (0, -2), (-1, -1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, -2), (-1, -2), colors.HexColor('#e3f2fd')),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#c8e6c9')),
        ('SPAN', (1, -2), (2, -2)),
        ('SPAN', (1, -1), (2, -1)),
        ('GRID', (0, -2), (-1, -1), 1, colors.black),
        ('TOPPADDING', (0, -2), (-1, -1), 10),
        ('BOTTOMPADDING', (0, -2), (-1, -1), 10),
    ]))
    
    elements.append(grade_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Footer
    footer = Paragraph(
        "<i>This is a computer-generated report. For queries, contact academic office.</i>",
        styles['Normal']
    )
    elements.append(Spacer(1, 0.5*inch))
    elements.append(footer)
    
    # Build PDF
    doc.build(elements)
    
    return filename
