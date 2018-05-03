import multiprocessing

bind = "127.0.0.1:{{cookiecutter.port}}"
workers = multiprocessing.cpu_count()
loglevel = "info"
proc_name = "{{cookiecutter.project_name}}"
timeout = 1200
