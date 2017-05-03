# Code listing #4

def fetch_url(url, ntries=3, timeout=30):
         " Fetch a given url and return its contents "

        # This loop performs a network fetch of the URL, retrying upto      
        # 3 times in case of errors. In case the URL cant be fetched,       
        # an error is returned.

        # Initialize all state
        count, result, error = 0, None, None
        while count < ntries:
            try:
                result = requests.get(url, timeout=timeout)
            except Exception as error:
                print('Caught exception', error, 'trying again after a while')
                # increment count
                count += 1
                # sleep 1 second every time
                time.sleep(1)
    
        if result == None:
            print("Error, could not fetch URL",url)
            # Return a tuple of (<return code>, <lasterror>)
            return (2, error)
    
        # Return data of URL
        return result.content
