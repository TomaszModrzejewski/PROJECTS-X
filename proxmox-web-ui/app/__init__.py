from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a_very_secret_key'

from app import routes