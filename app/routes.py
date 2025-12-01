from flask import Flask, render_template
from app.models import db, Node, Device, Template, TemplateAction
import logging


logging.basicConfig(level=logging.INFO, filename="app.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    """Дашборд"""
    title='Home'
    data='NIS'
    return render_template("index.html", title=title, data=data)


@app.route('/nodes')
def get_nodes():
    """Получить все узлы"""
    title='Home'

    if db is None:
        return (f"Ошибка: нет подключения к базе данных")

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
        return render_template("index.html", title=title, data=node.name)

    except Exception as e:
        return (f"Ошибка: {str(e)}")