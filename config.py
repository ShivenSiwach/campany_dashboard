import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-secret-123'
    DEBUG = True