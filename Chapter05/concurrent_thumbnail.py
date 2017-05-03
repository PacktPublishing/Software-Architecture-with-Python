# Code Listing #16

"""

Processing of pictures into thumbnails using concurrent futures

"""

# NOTE: This requires presence of a local "thumbs" folder. Otherwise it fails silently.

import os
import sys
import mimetypes

from PIL import Image
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


def thumbnail_image(filename, size=(64,64), format='.png'):
    """ Convert image thumbnails, given a filename """

    try:
        im=Image.open(filename)         
        im.thumbnail(size, Image.ANTIALIAS)
        
        basename = os.path.basename(filename)
        thumb_filename = os.path.join('thumbs',
                                      basename.rsplit('.')[0] + '_thumb.png')
        im.save(thumb_filename)
        print('Saved',thumb_filename)
        return True
        
    except Exception as e:
        print('Error converting file',filename)
        raise
        return False

def directory_walker(start_dir):
    """ Walk a directory and generate list of valid images """
    
    for root,dirs,files in os.walk(os.path.expanduser(start_dir)):
        for f in files:
            filename = os.path.join(root,f)
            # Only process if its a type of image
            file_type = mimetypes.guess_type(filename.lower())[0]
            if file_type != None and file_type.startswith('image/'):
                yield filename
            
if __name__ == '__main__':
    root_dir = os.path.expanduser('~/Pictures/')
    if '--process' in sys.argv:
        executor = ProcessPoolExecutor(max_workers=10)
    else:
        executor = ThreadPoolExecutor(max_workers=10)
        
    with executor:
        future_map = {executor.submit(thumbnail_image, filename): filename for filename in directory_walker(root_dir)}
        for future in as_completed(future_map):
            num = future_map[future]
            status = future.result()
            if status:
                print('Thumbnail of',future_map[future],'saved')


        
        
