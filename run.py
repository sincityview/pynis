#!/usr/bin/env python3
"""
PyNIS - Python Network Inventory Script
"""

# 1. Сначала импортируем app из routes
from app.routes import app

# 2. Потом конфиг и модели
from config import Config
from app.models import db

# 3. Конфигурируем
app.config.from_object(Config)

# 4. Инициализируем БД
db.init_app(app)

# 5. Создаем таблицы
with app.app_context():
    db.create_all()
    print("✅ Таблицы БД созданы/проверены")

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 PyNIS запущен: http://localhost:5000")
    print("="*50 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)