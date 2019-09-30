# synchronous API request demo

import requests
import time
import json


def tracklist():
    start = time.perf_counter()
    tracking_app_url = "https://httpbin.org/anything/"
    for i in range(25):
        print(i)
        r = requests.get(tracking_app_url + str(i))
        r = r.text
        r = json.loads(r)
        print(r["url"])

    elapsed = time.perf_counter() - start
    times.append(f"executed in {elapsed:0.2f} seconds.")


times = []
tracklist()
print(times)
