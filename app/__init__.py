from flask import Flask

app = Flask(__name__) # variable

from app import routes # Refers to the app package
