import multiprocessing

bind = "127.0.0.1:9002"
workers = multiprocessing.cpu_count()
loglevel = "info"
proc_name = "curlbin"
timeout = 1200
