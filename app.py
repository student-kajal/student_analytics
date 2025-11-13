# from flask import Flask
# from flask_cors import CORS
# from models import db
# from routes import api
# from config import Config

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
    
#     # Enable CORS
#     CORS(app)
    
#     # Initialize database
#     db.init_app(app)
    
#     # Register blueprints
#     app.register_blueprint(api)
    
#     return app

# if __name__ == '__main__':
#     app = create_app()
    
#     # Create tables
#     with app.app_context():
#         try:
#             db.create_all()
#             print("✅ Database tables created successfully!")
#             print(f"📊 Database: student_analytics")
#             print(f"📋 Tables: students, courses, grades")
#         except Exception as e:
#             print(f"❌ Error creating database: {e}")
#             print("Make sure PostgreSQL is running and database 'student_analytics' exists")
    
#     print(f"\n🚀 Server running on http://localhost:{Config.PORT}")
#     print(f"📝 Open http://localhost:{Config.PORT} in browser")
#     print(f"🔗 API endpoints available at /api/*")
#     print("\nPress CTRL+C to stop the server\n")
    
#     app.run(debug=Config.DEBUG, port=Config.PORT)
from flask import Flask
from flask_cors import CORS
from models import db
from routes import api
from config import Config

# --------------------------------------
# CREATE APP (Render requires top-level app)
# --------------------------------------
app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS
CORS(app)

# Initialize Database
db.init_app(app)

# Register Blueprints
app.register_blueprint(api)

# --------------------------------------
# Create tables (local + Render)
# --------------------------------------
with app.app_context():
    try:
        db.create_all()
        print("✅ Database tables created successfully!")
        print("📊 Tables: students, courses, grades")
    except Exception as e:
        print("❌ Error creating database:", e)
        print("Make sure PostgreSQL connection is correct.")


# --------------------------------------
# Local run
# --------------------------------------
if __name__ == '__main__':
    print(f"\n🚀 Server running at: http://localhost:{Config.PORT}")
    print(f"📝 API Docs: http://localhost:{Config.PORT}")
    print(f"📊 Dashboard: http://localhost:{Config.PORT}/dashboard\n")
    app.run(debug=Config.DEBUG, port=Config.PORT)
