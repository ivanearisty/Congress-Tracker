import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the JWT secret key and other configurations from the environment
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")
