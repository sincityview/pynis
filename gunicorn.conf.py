import multiprocessing

# workers = multiprocessing.cpu_count() * 2 + 1
bind = "0.0.0.0:5000"
accesslog = "-"  # stdout
errorlog = "-"   # stdout
loglevel = "info"
reload = True
timeout = 120
keepalive = 5
wsgi_app = "run:app"