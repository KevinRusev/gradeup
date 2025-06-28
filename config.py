import os
import platform
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'hard-to-guess-string')

    # Email verification toggle
    DISABLE_EMAIL_VERIFICATION = os.environ.get('DISABLE_EMAIL_VERIFICATION', 'false').lower() in ['true', 'on', '1', 'yes']
    
    # Database configuration - supports both PostgreSQL (for production) and SQLite (for development)
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    if DATABASE_URL:
        # Production: Use PostgreSQL from Render
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
        # Fix for SQLAlchemy 1.4+ compatibility with Render's postgres:// URLs
        if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
            SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    else:
        # Development: Use SQLite
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = '[School Recommendation]'
    MAIL_SENDER = os.environ.get('MAIL_USERNAME')  # Use the authenticated Gmail account as sender
