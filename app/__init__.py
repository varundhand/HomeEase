from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from redis import Redis
from celery import Celery

app = Flask(__name__)
# app.config.from_object('config.Config')

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///household.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'

# Initialize Database
db = SQLAlchemy(app)

# Initialize Caching
cache = Cache(app)

# Initialize Celery
def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CACHE_REDIS_URL'],
        broker=app.config['CACHE_REDIS_URL']
    )
    celery.conf.update(app.config)
    return celery

celery = make_celery(app)

from app import routes, models
