import os

# class Config:
#     # PostgreSQL Database Configuration
#     # Format: postgresql://username:password@localhost:port/database_name
#     SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:your_password@localhost:5432/student_analytics'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SECRET_KEY = 'dev-secret-key-change-in-production'
    
#     # Application Configuration
#     DEBUG = True
#     PORT = 5000
# class Config:
#     SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Kajal%408010@localhost:5432/student_analytics'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SECRET_KEY = 'dev-secret-key-change-in-production'
#     DEBUG = True
#     PORT = 5000
import os

class Config:
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    
    SQLALCHEMY_DATABASE_URI = DATABASE_URL or 'postgresql://postgres:Kajal%408010@localhost:5432/student_analytics'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.environ.get('DEBUG', 'True') == 'True'
    PORT = int(os.environ.get('PORT', 5000))
