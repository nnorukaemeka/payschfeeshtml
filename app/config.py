import os

SECRET_KEY = os.environ.get('SECRET_KEY') or "ajajajjsjsjajjajaaw333"

#connecting to database
MONGO_URI = os.environ.get('MONGO_URI') or "none"