from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.db_config import DataSourceConfig

app = Flask(__name__)
app.config.from_object(DataSourceConfig)

db = SQLAlchemy(app)

from app.controllers import lessor_controller

