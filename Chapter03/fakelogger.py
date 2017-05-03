# Code Listing #2
import logging

class FakeLogger(object):
    """ A class that fakes the interface of the 
    logging.Logger object in a minimalistic fashion """

    def __init__(self):
        self.lvl = logging.INFO

    def setLevel(self, level):
        """ Set the logging level """
        self.lvl = level

    def _log(self, msg, *args):
        """ Perform the actual logging """

        # Since this is a fake object - no actual logging is done.
        # Instead the message is simply printed to standard output.
        print (msg, end=' ')
        for arg in args:
            print(arg, end=' ')
        print()
                
    def info(self, msg, *args):
        """ Log at info level """
        if self.lvl<=logging.INFO: return self._log(msg, *args)

    def debug(self, msg, *args):
        """ Log at debug level """
        if self.lvl<=logging.DEBUG: return self._log(msg, *args)

    def warning(self, msg, *args):
        """ Log at warning level """
        if self.lvl<=logging.WARNING: return self._log(msg, *args)          

    def error(self, msg, *args):
        """ Log at error level """
        if self.lvl<=logging.ERROR: return self._log(msg, *args)    

    def critical(self, msg, *args):
        """ Log at critical level """
        if self.lvl<=logging.CRITICAL: return self._log(msg, *args)         
