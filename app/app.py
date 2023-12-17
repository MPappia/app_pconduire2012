from flask import Flask, request, render_template
from .config import Config
from flask_bootstrap import Bootstrap
import pandas as pd 

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)

bootstrap= Bootstrap(app)

from .routes import generales