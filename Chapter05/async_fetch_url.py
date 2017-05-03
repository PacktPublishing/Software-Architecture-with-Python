# Code Listing #13

"""

Fetch URLs asynchronously - using aiohttp and print response.

"""

# async_fetch_url.py
import asyncio
import aiohttp
import async_timeout

@asyncio.coroutine
def fetch_page(session, url, timeout=60):
    """ Asynchronous URL fetcher """

    with async_timeout.timeout(timeout):
        response = session.get(url)
        return response

loop = asyncio.get_event_loop()
urls = ('http://www.google.com',
        'http://www.yahoo.com',
        'http://www.facebook.com',
        'http://www.reddit.com',
        'http://www.twitter.com')


session = aiohttp.ClientSession(loop=loop)
tasks = map(lambda x: fetch_page(session, x), urls)
# Wait for tasks
done, pending = loop.run_until_complete(asyncio.wait(tasks, timeout=120))

for future in done:
    response = future.result()
    print(response)
    response.close()

session.close()
loop.close()

    
    


    
