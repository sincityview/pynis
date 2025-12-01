from flask import Flask, jsonify, render_template
from sqlalchemy import text
import datetime
import os

try:
    from app.models import db, Node, Device, Template, TemplateAction
except ImportError:
    # Если импорт не удался (например, в тестах)
    Node = Device = Template = TemplateAction = None


# Создаем app здесь
app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "service": "pyni"
    })

@app.route('/about')
def about():
    return jsonify({
        "project": "PyNIS",
        "version": "0.1.0",
        "description": "Python Network Inventory Script",
        "author": "Alex Mass",
        "repository": "https://github.com/sincityview/pynis",
        "api_version": "v1",
        "endpoints": {
            "health": "/health"
        }
    })

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
        title='Home',
        data='PyNIS')

@app.route('/db')
def db_status():
    # Проверяем, инициализирована ли db
    if db is None:
        return "❌ DB not initialized", 500
    
    try:
        db.session.execute(text('SELECT 1'))
        status = '✅ connected'
    except Exception as e:
        status = f'❌ error: {str(e)}'
    
    return render_template("index.html",
        title='Database Status',
        data=status)


@app.route('/nodes')
def get_nodes():
    """Получить все узлы"""
    if db is None:
        return jsonify({"error": "Database not initialized"}), 500
    
    try:
        nodes = Node.query.all()
        result = []
        for node in nodes:
            result.append({
                'id': node.id,
                'name': node.name,
                'address': node.address,
                'device_count': len(node.devices)
            })
        return jsonify({"nodes": result, "count": len(nodes)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500