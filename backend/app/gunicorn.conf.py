import multiprocessing

bind = ':8000'
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 60 * 5

accesslog = '/app/logs/backend_access.log'
errorlog = '/app/logs/backend_error.log'
