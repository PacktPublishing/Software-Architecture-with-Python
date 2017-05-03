# Code Listing #14

"""

Fetch URLs asynchronously and parse their responses - using aiohttp module

"""

# async_fetch_url2.py
import asyncio
import aiohttp
import async_timeout

@asyncio.coroutine
def fetch_page(session, url, timeout=60):
    """ Asynchronous URL fetcher """

    with async_timeout.timeout(timeout):
        response = session.get(url)
        return response
                
async def parse_response(futures):

    for future in futures:
        response = await future
        data = await response.text()            
        print('Response for URL',response.url,'=>', response.status, len(data))
        response.close()    
                
loop = asyncio.get_event_loop()
urls = ('http://www.google.com',
        'http://www.yahoo.com',
        'http://www.facebook.com',
        'http://www.reddit.com',
        'http://www.twitter.com')

session = aiohttp.ClientSession(loop=loop)
# Wait for futures

tasks = map(lambda x: fetch_page(session, x), urls)
done, pending = loop.run_until_complete(asyncio.wait(tasks, timeout=300))
loop.run_until_complete(parse_response(done))


session.close()
loop.close()

    


    
