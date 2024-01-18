import os
from . import config
import redis
from rq import Worker, Queue, Connection

listen = ['test-rq-worker']

redis_conn = redis.from_url(config.REDIS_URL)

if __name__ == '__main__':
    with Connection(redis_conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
