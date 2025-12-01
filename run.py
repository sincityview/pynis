#!/usr/bin/env python3
"""
Network Inventory Script
"""

from config import Config
from app.routes import app
from app.models import db


app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()
