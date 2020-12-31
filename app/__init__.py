from flask import Flask
from config import  Config

app = Flask(__name__) # variable
app.config.from_object(Config)

from app import routes # Refers to the app package
