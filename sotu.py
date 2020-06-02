import os

# from app import create_app

from .app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
