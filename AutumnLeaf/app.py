import time
import os
import requests

is_completed = False
my_count =0

while (my_count < os.environ.get['times']):
    start = time.perf_counter()
    response = requests.get(os.environ.get['site'])
    my_count =+1
    print(time.perf_counter() - start)

