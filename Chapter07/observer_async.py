# Code Listing #15

"""

Asynchronouse Observer Example

NOTE: This requires the package aiohttp.

"""

import weakref
import asyncio
import aiohttp

from collections import defaultdict, deque

class NewsPublisher(object):
    """ A news publisher class with asynchronous notifications """

    def __init__(self):
        # News channels
        self.channels = defaultdict(deque)
        self.subscribers = defaultdict(list)
        self.flag = True

    def add_news(self, channel, url):
        """ Add a news story """

        self.channels[channel].append(url)
        
    def register(self, subscriber, channel):
        """ Register a subscriber for a news channel """
        
        self.subscribers[channel].append(weakref.proxy(subscriber))

    def stop(self):
        """ Stop the publisher """

        self.flag = False
        
    async def notify(self):
        """ Notify subscribers """

        self.data_null_count = 0

        while self.flag:
            # Subscribers who were notified
            subs = []
            
            for channel in self.channels:
                try:
                    data = self.channels[channel].popleft()
                except IndexError:
                    self.data_null_count += 1
                    continue

                subscribers = self.subscribers[channel]
                for sub in subscribers:
                    print('Notifying',sub,'on channel',channel,'with data=>',data)
                    response = await sub.callback(channel, data)
                    print('Response from',sub,'for channel',channel,'=>',response)
                    subs.append(sub)

            await asyncio.sleep(2.0)

class NewsSubscriber(object):
    """ A news subscriber class with asynchronous callbacks """
    
    def __init__(self):
        self.stories = {}
        self.futures = []
        self.future_status = {}
        self.flag = True

    async def callback(self, channel, data):
        """ Callback method """

        # The data is a URL
        url = data
        # We return the response immediately
        print('Fetching URL',url,'...')
        future = aiohttp.request('GET', url)
        self.futures.append(future)
            
        return future
            
    async def fetch_urls(self):

        while self.flag:

            for future in self.futures:
                if self.future_status.get(future):
                    continue

                response = await future

                # Read data
                data = await response.read()

                print('\t',self,'Got data for URL',response.url,'length:',len(data))
                self.stories[response.url] = data
                # Mark as such
                self.future_status[future] = 1

            await asyncio.sleep(2.0)


if __name__ == "__main__":
    publisher = NewsPublisher()
    # Append some stories
    publisher.add_news('sports', 'http://www.cricbuzz.com/cricket-news/94018/collective-dd-show-hands-massive-loss-to-kings-xi-punjab')
    publisher.add_news('sports', 'https://sports.ndtv.com/indian-premier-league-2017/ipl-2017-this-is-how-virat-kohli-recovered-from-the-loss-against-mumbai-indians-1681955')
    publisher.add_news('india','http://www.business-standard.com/article/current-affairs/mumbai-chennai-and-hyderabad-airports-put-on-hijack-alert-report-117041600183_1.html')
    publisher.add_news('india','http://timesofindia.indiatimes.com/india/pakistan-to-submit-new-dossier-on-jadhav-to-un-report/articleshow/58204955.cms')

    subscriber1 = NewsSubscriber()
    subscriber2 = NewsSubscriber()  
    publisher.register(subscriber1, 'sports')
    publisher.register(subscriber2, 'india')    
    # subscriber.start()
    
    loop = asyncio.get_event_loop()

    tasks = map(lambda x: x.fetch_urls(), (subscriber1, subscriber2))
    loop.run_until_complete(asyncio.wait([publisher.notify(), *tasks], timeout=120))

    print('Ending loop')
    loop.close()
   
   
        
        
