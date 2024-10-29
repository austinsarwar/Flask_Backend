import os
import secrets

class Config:
    # Use an environment variable for the secret key or generate one if not set
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(16)  # Generates a random key
    # Use an environment variable for the database URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
