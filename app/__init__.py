#####################################################################################
########################   LIBRARIES  ################################################
#######################################################################################
from flask import Flask
from flask_pymongo import PyMongo
import os
from app.config import MONGO_URI, SECRET_KEY


#####################################################################################
########################   INITIALIZATION  ################################################
#######################################################################################
# Initializing Flask
app = Flask (__name__)

#app configuration
app_settings = os.environ.get(
    'APP_SETTINGS'
    'app.config'
) 
app.config.from_object(app_settings)

#initializing PyMongo
mongo = PyMongo(app, MONGO_URI)

from app import view