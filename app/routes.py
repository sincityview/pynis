from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'PyNIS'.format(
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        os.getpid(),
        os.sys.version.split()[0],
        "develop" if app.debug else "production"
    )

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
        "author": "Alex Maas",
        "repository": "https://github.com/sincityview/pynis",
        "api_version": "v1",
        "endpoints": {
            "health": "/health"
        }
    })
