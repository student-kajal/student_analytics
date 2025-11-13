# from flask import Blueprint, request, jsonify, render_template
# from models import db, Student, Course, Grade
# from sqlalchemy import func
# from utils.pdf_generator import generate_student_report

# api = Blueprint('api', __name__)

# # Home route
# @api.route('/')
# def home():
#     return render_template('index.html')

# # Student Routes
# @api.route('/api/students', methods=['GET'])
# def get_students():
#     try:
#         students = Student.query.all()
#         return jsonify({
#             'success': True,
#             'data': [student.to_dict() for student in students],
#             'count': len(students)
#         }), 200
#     except Exception as e:
#         return jsonify({'success': False, 'error': str(e)}), 500

# @api.route('/api/students', methods=['POST'])
# def create_student():
#     try:
#         data = request.get_json()
        
#         # Validation
#         required_fields = ['name', 'email', 'enrollment_no', 'branch', 'semester']
#         if not all(k in data for k in required_fields):
#             return jsonify({'success': False, 'error': 'Missing required fields'}), 400
        
#         # Check if student already exists
#         existing = Student.query.filter_by(email=data['email']).first()
#         if existing:
#             return jsonify({'success': False, 'error': 'Student with this email already exists'}), 400
        
#         student = Student(
#             name=data['name'],
#             email=data['email'],
#             enrollment_no=data['enrollment_no'],
#             branch=data['branch'],
#             semester=data['semester']
#         )
        
#         db.session.add(student)
#         db.session.commit()
        
#         return jsonify({
#             'success': True,
#             'message': 'Student created successfully',
#             'data': student.to_dict()
#         }), 201
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'success': False, 'error': str(e)}), 500

# @api.route('/api/students/<int:id>', methods=['GET'])
# def get_student(id):
#     try:
#         student = Student.query.get(id)
#         if not student:
#             return jsonify({'success': False, 'error': 'Student not found'}), 404
        
#         return jsonify({
#             'success': True,
#             'data': student.to_dict()
#         }), 200
#     except Exception as e:
#         return jsonify({'success': False, 'error': str(e)}), 500

# @api.route('/api/students/<int:id>', methods=['DELETE'])
# def delete_student(id):
#     try:
#         student = Student.query.get(id)
#         if not student:
#             return jsonify({'success': False, 'error': 'Student not found'}), 404
        
#         db.session.delete(student)
#         db.session.commit()
        
#         return jsonify({
#             'success': True,
#             'message': 'Student deleted successfully'
#         }), 200
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'success': False, 'error': str(e)}), 500

# # Course Routes
# @api.route('/api/courses', methods=['GET'])
# def get_courses():
#     try:
#         courses = Course.query.all()
#         return jsonify({
#             'success': True,
#             'data': [course.to_dict() for course in courses],
#             'count': len(courses)
#         }), 200
#     except Exception as e:
#         return jsonify({'success': False, 'error': str(e)}), 500

# @api.route('/api/courses', methods=['POST'])
# def create_course():
#     try:
#         data = request.get_json()
        
#         required_fields = ['code', 'name', 'credits', 'semester']
#         if not all(k in data for k in required_fields):
#             return jsonify({'success': False, 'error': 'Missing required fields'}), 400
        
#         # Check if course already exists
#         existing = Course.query.filter_by(code=data['code']).first()
#         if existing:
#             return jsonify({'success': False, 'error': 'Course with this code already exists'}), 400
        
#         course = Course(
#             code=data['code'],
#             name=data['name'],
#             credits=data['credits'],
#             semester=data['semester']
#         )
        
#         db.session.add(course)
#         db.session.commit()
        
#         return jsonify({
#             'success': True,
#             'message': 'Course created successfully',
#             'data': course.to_dict()
#         }), 201
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'success': False, 'error': str(e)}), 500

# # Grade Routes
# @api.route('/api/grades', methods=['POST'])
# def add_grade():
#     try:
#         data = request.get_json()
        
#         required_fields = ['student_id', 'course_id', 'marks', 'semester', 'academic_year']
#         if not all(k in data for k in required_fields):
#             return jsonify({'success': False, 'error': 'Missing required fields'}), 400
        
#         # Verify student and course exist
#         student = Student.query.get(data['student_id'])
#         course = Course.query.get(data['course_id'])
        
#         if not student:
#             return jsonify({'success': False, 'error': 'Student not found'}), 404
#         if not course:
#             return jsonify({'success': False, 'error': 'Course not found'}), 404
        
#         # Calculate grade based on marks
#         marks = float(data['marks'])
#         if marks >= 90:
#             grade_letter = 'A+'
#         elif marks >= 80:
#             grade_letter = 'A'
#         elif marks >= 70:
#             grade_letter = 'B+'
#         elif marks >= 60:
#             grade_letter = 'B'
#         elif marks >= 50:
#             grade_letter = 'C'
#         else:
#             grade_letter = 'F'
        
#         grade = Grade(
#             student_id=data['student_id'],
#             course_id=data['course_id'],
#             marks=marks,
#             grade=grade_letter,
#             semester=data['semester'],
#             academic_year=data['academic_year']
#         )
        
#         db.session.add(grade)
#         db.session.commit()
        
#         return jsonify({
#             'success': True,
#             'message': 'Grade added successfully',
#             'data': grade.to_dict()
#         }), 201
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'success': False, 'error': str(e)}), 500

# @api.route('/api/grades/student/<int:student_id>', methods=['GET'])
# def get_student_grades(student_id):
#     try:
#         student = Student.query.get(student_id)
#         if not student:
#             return jsonify({'success': False, 'error': 'Student not found'}), 404
        
#         grades = Grade.query.filter_by(student_id=student_id).all()
        
#         result = []
#         for grade in grades:
#             course = Course.query.get(grade.course_id)
#             result.append({
#                 **grade.to_dict(),
#                 'course_name': course.name,
#                 'course_code': course.code
#             })
        
#         return jsonify({
#             'success': True,
#             'data': result,
#             'count': len(result)
#         }), 200
#     except Exception as e:
#         return jsonify({'success': False, 'error': str(e)}), 500

# # Analytics Routes
# @api.route('/api/analytics/student/<int:student_id>', methods=['GET'])
# def get_student_analytics(student_id):
#     try:
#         student = Student.query.get(student_id)
#         if not student:
#             return jsonify({'success': False, 'error': 'Student not found'}), 404
        
#         # Calculate average marks
#         avg_marks = db.session.query(func.avg(Grade.marks)).filter_by(student_id=student_id).scalar()
        
#         # Get all grades
#         grades = Grade.query.filter_by(student_id=student_id).all()
        
#         # Grade distribution
#         grade_distribution = {}
#         for grade in grades:
#             grade_distribution[grade.grade] = grade_distribution.get(grade.grade, 0) + 1
        
#         return jsonify({
#             'success': True,
#             'data': {
#                 'student': student.to_dict(),
#                 'average_marks': round(float(avg_marks), 2) if avg_marks else 0,
#                 'total_courses': len(grades),
#                 'grade_distribution': grade_distribution,
#                 'grades': [grade.to_dict() for grade in grades]
#             }
#         }), 200
#     except Exception as e:
#         return jsonify({'success': False, 'error': str(e)}), 500

# @api.route('/api/analytics/course/<int:course_id>', methods=['GET'])
# def get_course_analytics(course_id):
#     try:
#         course = Course.query.get(course_id)
#         if not course:
#             return jsonify({'success': False, 'error': 'Course not found'}), 404
        
#         # Calculate average marks for course
#         avg_marks = db.session.query(func.avg(Grade.marks)).filter_by(course_id=course_id).scalar()
        
#         # Count students enrolled
#         student_count = db.session.query(func.count(Grade.id)).filter_by(course_id=course_id).scalar()
        
#         # Highest and lowest marks
#         max_marks = db.session.query(func.max(Grade.marks)).filter_by(course_id=course_id).scalar()
#         min_marks = db.session.query(func.min(Grade.marks)).filter_by(course_id=course_id).scalar()
        
#         return jsonify({
#             'success': True,
#             'data': {
#                 'course': course.to_dict(),
#                 'average_marks': round(float(avg_marks), 2) if avg_marks else 0,
#                 'total_students': student_count,
#                 'highest_marks': float(max_marks) if max_marks else 0,
#                 'lowest_marks': float(min_marks) if min_marks else 0
#             }
#         }), 200
#     except Exception as e:
#         return jsonify({'success': False, 'error': str(e)}), 500

# # PDF Report Route
# @api.route('/api/reports/student/<int:student_id>', methods=['GET'])
# def generate_report(student_id):
#     try:
#         student = Student.query.get(student_id)
#         if not student:
#             return jsonify({'success': False, 'error': 'Student not found'}), 404
        
#         grades = Grade.query.filter_by(student_id=student_id).all()
        
#         if not grades:
#             return jsonify({'success': False, 'error': 'No grades found for this student'}), 404
        
#         # Generate PDF
#         pdf_path = generate_student_report(student, grades)
        
#         return jsonify({
#             'success': True,
#             'message': 'Report generated successfully',
#             'pdf_path': pdf_path
#         }), 200
#     except Exception as e:
#         return jsonify({'success': False, 'error': str(e)}), 500
# @api.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')
# # Overall Analytics
# @api.route('/api/analytics/overall', methods=['GET'])
# def get_overall_analytics():
#     try:
#         total_students = Student.query.count()
#         total_courses = Course.query.count()
#         total_grades = Grade.query.count()
        
#         overall_avg = db.session.query(func.avg(Grade.marks)).scalar()
        
#         return jsonify({
#             'success': True,
#             'data': {
#                 'total_students': total_students,
#                 'total_courses': total_courses,
#                 'total_grades': total_grades,
#                 'overall_average': round(float(overall_avg), 2) if overall_avg else 0
#             }
#         }), 200
#     except Exception as e:
#         return jsonify({'success': False, 'error': str(e)}), 500
from flask import Blueprint, request, jsonify, render_template
from models import db, Student, Course, Grade
from sqlalchemy import func
# from utils.pdf_generator import generate_student_report
from utils.pdf_generator import generate_student_report_buffer
from flask import Blueprint, request, jsonify, render_template, send_file

api = Blueprint('api', __name__)


# -----------------------------------------
# Home Route
# -----------------------------------------
@api.route('/')
def home():
    return render_template('index.html')


# -----------------------------------------
# Student Routes
# -----------------------------------------
@api.route('/api/students', methods=['GET'])
def get_students():
    try:
        students = Student.query.all()
        return jsonify({
            'success': True,
            'data': [student.to_dict() for student in students],
            'count': len(students)
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@api.route('/api/students', methods=['POST'])
def create_student():
    try:
        data = request.get_json()

        required_fields = ['name', 'email', 'enrollment_no', 'branch', 'semester']
        if not all(k in data for k in required_fields):
            return jsonify({'success': False, 'error': 'Missing required fields'}), 400

        # Check if email already exists
        if Student.query.filter_by(email=data['email']).first():
            return jsonify({'success': False, 'error': 'Student with this email already exists'}), 400

        student = Student(
            name=data['name'],
            email=data['email'],
            enrollment_no=data['enrollment_no'],
            branch=data['branch'],
            semester=data['semester']
        )

        db.session.add(student)
        db.session.commit()

        return jsonify({
            'success': True,
            'message': 'Student created successfully',
            'data': student.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


@api.route('/api/students/<int:id>', methods=['GET'])
def get_student(id):
    try:
        student = Student.query.get(id)
        if not student:
            return jsonify({'success': False, 'error': 'Student not found'}), 404

        return jsonify({'success': True, 'data': student.to_dict()}), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@api.route('/api/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    try:
        student = Student.query.get(id)
        if not student:
            return jsonify({'success': False, 'error': 'Student not found'}), 404

        db.session.delete(student)
        db.session.commit()

        return jsonify({'success': True, 'message': 'Student deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


# -----------------------------------------
# Course Routes
# -----------------------------------------
@api.route('/api/courses', methods=['GET'])
def get_courses():
    try:
        courses = Course.query.all()
        return jsonify({
            'success': True,
            'data': [course.to_dict() for course in courses],
            'count': len(courses)
        }), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@api.route('/api/courses', methods=['POST'])
def create_course():
    try:
        data = request.get_json()

        required_fields = ['code', 'name', 'credits', 'semester']
        if not all(k in data for k in required_fields):
            return jsonify({'success': False, 'error': 'Missing required fields'}), 400

        if Course.query.filter_by(code=data['code']).first():
            return jsonify({'success': False, 'error': 'Course with this code already exists'}), 400

        course = Course(
            code=data['code'],
            name=data['name'],
            credits=data['credits'],
            semester=data['semester']
        )

        db.session.add(course)
        db.session.commit()

        return jsonify({
            'success': True,
            'message': 'Course created successfully',
            'data': course.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


# -----------------------------------------
# Grade Routes
# -----------------------------------------
@api.route('/api/grades', methods=['POST'])
def add_grade():
    try:
        data = request.get_json()

        required_fields = ['student_id', 'course_id', 'marks', 'semester', 'academic_year']
        if not all(k in data for k in required_fields):
            return jsonify({'success': False, 'error': 'Missing required fields'}), 400

        student = Student.query.get(data['student_id'])
        course = Course.query.get(data['course_id'])

        if not student:
            return jsonify({'success': False, 'error': 'Student not found'}), 404
        if not course:
            return jsonify({'success': False, 'error': 'Course not found'}), 404

        marks = float(data['marks'])

        # Grade calculation
        if marks >= 90:
            grade_letter = 'A+'
        elif marks >= 80:
            grade_letter = 'A'
        elif marks >= 70:
            grade_letter = 'B+'
        elif marks >= 60:
            grade_letter = 'B'
        elif marks >= 50:
            grade_letter = 'C'
        else:
            grade_letter = 'F'

        grade = Grade(
            student_id=data['student_id'],
            course_id=data['course_id'],
            marks=marks,
            grade=grade_letter,
            semester=data['semester'],
            academic_year=data['academic_year']
        )

        db.session.add(grade)
        db.session.commit()

        return jsonify({
            'success': True,
            'message': 'Grade added successfully',
            'data': grade.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


@api.route('/api/grades/student/<int:student_id>', methods=['GET'])
def get_student_grades(student_id):
    try:
        student = Student.query.get(student_id)
        if not student:
            return jsonify({'success': False, 'error': 'Student not found'}), 404

        grades = Grade.query.filter_by(student_id=student_id).all()

        result = []
        for grade in grades:
            course = Course.query.get(grade.course_id)
            result.append({
                **grade.to_dict(),
                'course_name': course.name,
                'course_code': course.code
            })

        return jsonify({
            'success': True,
            'data': result,
            'count': len(result)
        }), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# -----------------------------------------
# Analytics Routes
# -----------------------------------------
@api.route('/api/analytics/student/<int:student_id>', methods=['GET'])
def get_student_analytics(student_id):
    try:
        student = Student.query.get(student_id)
        if not student:
            return jsonify({'success': False, 'error': 'Student not found'}), 404

        avg_marks = db.session.query(func.avg(Grade.marks)).filter_by(student_id=student_id).scalar()
        grades = Grade.query.filter_by(student_id=student_id).all()

        grade_distribution = {}
        for g in grades:
            grade_distribution[g.grade] = grade_distribution.get(g.grade, 0) + 1

        return jsonify({
            'success': True,
            'data': {
                'student': student.to_dict(),
                'average_marks': round(float(avg_marks), 2) if avg_marks else 0,
                'total_courses': len(grades),
                'grade_distribution': grade_distribution,
                'grades': [g.to_dict() for g in grades]
            }
        }), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@api.route('/api/analytics/course/<int:course_id>', methods=['GET'])
def get_course_analytics(course_id):
    try:
        course = Course.query.get(course_id)
        if not course:
            return jsonify({'success': False, 'error': 'Course not found'}), 404

        avg_marks = db.session.query(func.avg(Grade.marks)).filter_by(course_id=course_id).scalar()
        student_count = db.session.query(func.count(Grade.id)).filter_by(course_id=course_id).scalar()
        max_marks = db.session.query(func.max(Grade.marks)).filter_by(course_id=course_id).scalar()
        min_marks = db.session.query(func.min(Grade.marks)).filter_by(course_id=course_id).scalar()

        return jsonify({
            'success': True,
            'data': {
                'course': course.to_dict(),
                'average_marks': round(float(avg_marks), 2) if avg_marks else 0,
                'total_students': student_count,
                'highest_marks': float(max_marks) if max_marks else 0,
                'lowest_marks': float(min_marks) if min_marks else 0,
            }
        }), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


# -----------------------------------------
# PDF Report Route
# -----------------------------------------
# @api.route('/api/reports/student/<int:student_id>', methods=['GET'])
# def generate_report(student_id):
#     try:
#         student = Student.query.get(student_id)
#         if not student:
#             return jsonify({'success': False, 'error': 'Student not found'}), 404

#         grades = Grade.query.filter_by(student_id=student_id).all()
#         if not grades:
#             return jsonify({'success': False, 'error': 'No grades found'}), 404

#         pdf_path = generate_student_report(student, grades)

#         return jsonify({
#             'success': True,
#             'message': 'Report generated successfully',
#             'pdf_path': pdf_path
#         }), 200

#     except Exception as e:
#         return jsonify({'success': False, 'error': str(e)}), 500

@api.route('/api/reports/student/<int:student_id>', methods=['GET'])
def generate_report(student_id):
    try:
        student = Student.query.get(student_id)
        if not student:
            return jsonify({'success': False, 'error': 'Student not found'}), 404

        grades = Grade.query.filter_by(student_id=student_id).all()
        if not grades:
            return jsonify({'success': False, 'error': 'No grades found'}), 404

        from flask import send_file
        pdf_buffer = generate_student_report_buffer(student, grades)

        return send_file(
            pdf_buffer,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=f'student_report_{student.enrollment_no}.pdf'
        )
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
# -----------------------------------------
# Dashboard
# -----------------------------------------
@api.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# -----------------------------------------
# Overall Analytics
# -----------------------------------------
@api.route('/api/analytics/overall', methods=['GET'])
def get_overall_analytics():
    try:
        total_students = Student.query.count()
        total_courses = Course.query.count()
        total_grades = Grade.query.count()

        overall_avg = db.session.query(func.avg(Grade.marks)).scalar()

        return jsonify({
            'success': True,
            'data': {
                'total_students': total_students,
                'total_courses': total_courses,
                'total_grades': total_grades,
                'overall_average': round(float(overall_avg), 2) if overall_avg else 0
            }
        }), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
