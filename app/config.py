import os

SECRET_KEY = os.environ.get('SECRET_KEY') or "ajajajjsjsjajjajaaw333"

#connecting to database
MONGO_URI = os.environ.get('MONGO_URI') or "mongodb+srv://nnorukaemeka:oluchukwu@cluster0-k3hbu.mongodb.net/testkiara?retryWrites=true&w=majority"