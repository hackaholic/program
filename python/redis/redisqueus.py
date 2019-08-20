from redis import Redis
from rq import Queue
from url_word_count import count_word
import time

url = "http://www.google.com"
conn = Redis(host='172.17.0.2', port=6379)
q = Queue('test' ,connection=conn)
job = q.enqueue(count_word, args=(url,))

while not job.result:
    pass

print(job.result)
