# asynchronous API request demo

import aiohttp
import asyncio
import time
import json


testing_app_url = "https://httpbin.org/anything/"


async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(_get_response(session, i) for i in range(25)))


async def _get_response(session: "ClientSession", i):
    print(i)
    async with session.get(testing_app_url + str(i)) as resp:
        r = await resp.text()
        r = json.loads(r)
        print(r["url"])


times = []


loop = asyncio.get_event_loop()

start = time.perf_counter()
loop.run_until_complete(main())
elapsed = time.perf_counter() - start
times.append(f"executed in {elapsed:0.2f} seconds.")
print(times)
