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
