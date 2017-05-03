# Code Listing #1

"""

Thumbnail converter using URLs

"""

import threading
import urllib.request
# Install PILL via Pillow
from PIL import Image

def thumbnail_image(url, size=(64, 64), format='.png'):
    """ Convert image to a specific format """

    im = Image.open(urllib.request.urlopen(url))
    # filename is last part of URL minus extension + '.format'
    pieces = url.split('/')
    filename = ''.join((pieces[-2],'_',pieces[-1].split('.')[0],'_thumb',format))
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(filename)   
    print('Saved',filename)

if __name__ == "__main__":
    
    img_urls = ['https://dummyimage.com/256x256/000/fff.jpg',
                'https://dummyimage.com/320x240/fff/00.jpg',
                'https://dummyimage.com/640x480/ccc/aaa.jpg',
                'https://dummyimage.com/128x128/ddd/eee.jpg',
                'https://dummyimage.com/720x720/111/222.jpg']
            
    for url in img_urls:
        # For making the program serial, comment out the next two
        # lines and uncomment the last line.
        t = threading.Thread(target=thumbnail_image,args=(url,))
        t.start()
        # thumbnail_image(url)

