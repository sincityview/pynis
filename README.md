### Структура

```
nis/
├── app/
│   ├── models.py           # Модели БД
│   ├── routes.py           # Роуты Flask
│   └── templates/
│       └── index.html
├── config.py               # Конфигурация приложения
├── gunicorn.conf.py        # Конфигурация Gunicorn
├── run.py                  # Точка входа
├── requirements.txt        # Зависимости
├── env.example             # Шаблон .env
└── README.md               # Документация
```


### Запуск

git clone git@github.com:sincityview/nis.git

cd nis

python3 -m venv .venv

.venv/bin/pip install -r requirements.txt

.venv/bin/gunicorn run:app

