# coding: utf-8

import multiprocessing

import os
import sys

pdir = os.path.abspath(os.path.dirname(__file__))
pdir = os.path.split(pdir)[0]
if pdir not in sys.path:
    sys.path.append(pdir)


chdir = pdir
bind = '0.0.0.0:5000'
workers = multiprocessing.cpu_count() * 2 + 1

worker_class = 'gevent'
# daemon = True
loglevel = 'info'
accesslog = '/Users/humin/Documents/project/ai_service/api.access'
errorlog = '/Users/humin/Documents/project/ai_service/api.error'

worker_connections = 1000
timeout = 60
max_requests = 3
graceful_timeout = 60
