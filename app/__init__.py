from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)
    
    db.init_app(app)
    
    from . import routes
    app.register_blueprint(routes.bp)
    
    return app