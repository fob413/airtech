import os

from app.app import create_app
from app.task.celery import make_celery


env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)
celery = make_celery(app)
