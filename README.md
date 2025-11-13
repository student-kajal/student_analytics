# 🎓 Student Performance Analytics System

A comprehensive full-stack REST API application for managing student academic performance with real-time analytics and automated PDF report generation.

## ✨ Features

- ✅ **Complete CRUD Operations** - Students, Courses, and Grades management
- ✅ **Automated Grade Calculation** - Automatic letter grade assignment based on marks
- ✅ **Real-time Analytics** - Student-wise, course-wise, and overall performance metrics
- ✅ **PDF Report Generation** - Professional performance reports with ReportLab
- ✅ **RESTful API Design** - Clean, standardized API endpoints
- ✅ **PostgreSQL Database** - Relational data with proper foreign key relationships
- ✅ **Data Validation** - Input validation and error handling

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python Flask |
| **Database** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **PDF Generation** | ReportLab |
| **API Style** | RESTful |

## 📊 Database Schema

### Students Table
- id (Primary Key)
- name, email, enrollment_no
- branch, semester
- created_at

### Courses Table
- id (Primary Key)
- code, name, credits
- semester

### Grades Table
- id (Primary Key)
- student_id (Foreign Key → students)
- course_id (Foreign Key → courses)
- marks, grade, semester
- academic_year, created_at

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- PostgreSQL (with pgAdmin)

### Step 1: Clone Repository
git clone https://github.com/student-kajal/student_analytics.git
cd student_analytics
Step 2: Create Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
Step 3: Install Dependencies
pip install -r requirements.txt
Step 4: Configure Database
Create PostgreSQL Database:
-- Open pgAdmin or psql
CREATE DATABASE student_analytics;
Update config.py with your credentials:
DATABASE_URI = 'postgresql://username:password@localhost:5432/student_analytics'
SECRET_KEY = 'your-secret-key-here'
DEBUG = True
Step 5: Initialize Database
python app.py
Database tables will be created automatically on first run.
Step 6: Access Application
Dashboard (with data tables):
http://localhost:5000/dashboard
API Documentation:
http://localhost:5000
📋 API Endpoints
Student Management
| Method | Endpoint          | Description        | Request Body                             |
| ------ | ----------------- | ------------------ | ---------------------------------------- |
| GET    | /api/students     | Get all students   | -                                        |
| POST   | /api/students     | Create new student | name,email,enrollment_no,branch,semester |
| GET    | /api/students/:id | Get student by ID  | -                                        |
| DELETE | /api/students/:id | Delete student     | -                                        |
Example Request (POST):

text
{
  "name": "Kajal Kumari",
  "email": "kajal@nsut.ac.in",
  "enrollment_no": "2021ECE001",
  "branch": "ECE",
  "semester": 7
}
Course Management
Method	Endpoint	Description	Request Body
GET	/api/courses	Get all courses	-
POST	/api/courses	Create new course	code, name, credits, semester
Example Request (POST):

json
{
  "code": "CS301",
  "name": "Database Management Systems",
  "credits": 4,
  "semester": 5
}
Grade Management
Method	Endpoint	Description	Request Body
POST	/api/grades	Add grade	student_id, course_id, marks, semester, academic_year
GET	/api/grades/student/:id	Get student grades	-
Example Request (POST):

text
{
  "student_id": 1,
  "course_id": 1,
  "marks": 88.5,
  "semester": 5,
  "academic_year": "2024-25"
}
Analytics
| Method | Endpoint                   | Description         | Response Data                                    |
| ------ | -------------------------- | ------------------- | ------------------------------------------------ |
| GET    | /api/analytics/overall     | Overall statistics  | Total students, courses, grades, average         |
| GET    | /api/analytics/student/:id | Student performance | Average marks, grade distribution, course count  |
| GET    | /api/analytics/course/:id  | Course statistics   | Average, highest, lowest marks, enrollment count |
Reports
| Method | Endpoint                 | Description         | Response      |
| ------ | ------------------------ | ------------------- | ------------- |
| GET    | /api/reports/student/:id | Generate PDF report | PDF file path |
🎯 Key Features Explained
Automated Grade Calculation
The system automatically calculates letter grades based on marks:

python
if marks >= 90:
    grade = 'A+'  # 90-100
elif marks >= 80:
    grade = 'A'   # 80-89
elif marks >= 70:
    grade = 'B+'  # 70-79
elif marks >= 60:
    grade = 'B'   # 60-69
elif marks >= 50:
    grade = 'C'   # 50-59
else:
    grade = 'F'   # Below 50
Real-time Analytics
Student Analytics includes:

Average marks across all courses

Total courses completed

Grade distribution (count of A+, A, B+, etc.)

Individual course performance

Course Analytics includes:

Class average for the course

Total students enrolled

Highest and lowest scores

Performance distribution

Overall Analytics includes:

Total students in system

Total courses offered

Total grades recorded

System-wide average performance

PDF Report Generation
Professional PDF reports are generated with:

Student information header

Formatted table of all grades

Course-wise performance breakdown

Overall average calculation

Performance rating

🧪 Testing
Using Postman
Import the API collection

Set base URL: http://localhost:5000

Test endpoints one by one

Sample Test Flow
Create Student → POST /api/students

Create Course → POST /api/courses

Add Grade → POST /api/grades

View Analytics → GET /api/analytics/student/1

Generate Report → GET /api/reports/student/1

🔧 Configuration
Environment Variables (Optional)
Create .env file in project root:

text
DATABASE_URI=postgresql://user:password@localhost:5432/student_analytics
SECRET_KEY=your-secret-key-here
DEBUG=True
PORT=5000
Grade Calculation Customization
Modify grade thresholds in routes.py:

python
# Custom grading scale
if marks >= 85:
    grade_letter = 'A+'
elif marks >= 75:
    grade_letter = 'A'
# ... customize as needed
📈 Future Enhancements
 JWT-based authentication

 Role-based access control (Admin, Faculty, Student)

 Email notifications for grade updates

 Excel export functionality

 Data visualization with Chart.js

 Attendance tracking module

 Assignment submission system

 Mobile responsive design improvements

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Kajal Kumari

GitHub: @student-kajal

Institution: NSUT Delhi - B.Tech ECE

LinkedIn: Your LinkedIn Profile

🙏 Acknowledgments
Flask documentation and community

PostgreSQL documentation

ReportLab for PDF generation

SQLAlchemy ORM

NSUT Delhi

📞 Support
For issues, questions, or suggestions:

Open an issue on GitHub

Email: kajal971126@gmail.com

Create a pull request

⭐ Show Your Support
Give a ⭐ if this project helped you learn or build something cool!
Built with ❤️ by Kajal Kumari | NSUT Delhi
