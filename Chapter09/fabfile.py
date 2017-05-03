# Code Listing #2

from fabric.api import run

def remote_install(application):
    
    print ('Installing',application)
    run('sudo pip install ' + application)
