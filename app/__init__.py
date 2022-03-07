from flask import Flask
from config import DevConfig

# import flask
news_app = Flask(__name__)
news_app.config.from_object(DevConfig)
news_app.config.from_pyfile('../instance/config.py')


from .main import views
from .main import errors




