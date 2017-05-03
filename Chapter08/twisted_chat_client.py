# Code Listing #7

"""

Multiuser chat client using Twisted

"""

# twisted_chat_client.py

import sys
import socket
from twisted.internet import stdio, reactor, protocol


class ChatProtocol(protocol.Protocol):
    """ Base protocol for chat """
    
    def __init__(self, client):
        self.output = None
        # Client name: E.g: andy
        self.client = client
        self.prompt='[' + '@'.join((self.client, socket.gethostname().split('.')[0])) + ']> '             

    def input_prompt(self):
        """ The input prefix for client """
        sys.stdout.write(self.prompt)
        sys.stdout.flush()
        
    def dataReceived(self, data):
        self.processData(data)
        
class ChatClientProtocol(ChatProtocol):
    """ Chat client protocol """

    def connectionMade(self):
        print 'Connection made'
        self.output.write(self.client + ":<handshake>")
        
    def processData(self, data):
        """ Process data received """
        
        if not len(data.strip()):
            return

        self.input_prompt()
        
        if self.output:
            # Send data in this form to server
            self.output.write(self.client + ":" + data)
            

class StdioClientProtocol(ChatProtocol):
    """ Protocol which reads data from input and echoes
    data to standard output """
    
    def connectionMade(self):
        # Create chat client protocol
        chat = ChatClientProtocol(client=sys.argv[1])
        chat.output = self.transport

        # Create stdio wrapper
        stdio_wrapper = stdio.StandardIO(chat)
        # Connect to output
        self.output = stdio_wrapper
        print "Connected to server"
        self.input_prompt()

    def input_prompt(self):
        # Since the output is directly connected
        # to stdout, use that to write.
        self.output.write(self.prompt)

    def processData(self, data):
        """ Process data received """
        
        if self.output:
            self.output.write('\n' + data)
            self.input_prompt()
            
            
class StdioClientFactory(protocol.ClientFactory):

    def buildProtocol(self, addr):
        return StdioClientProtocol(sys.argv[1])


def main():
    reactor.connectTCP("localhost", 3490, StdioClientFactory())
    reactor.run()


if __name__ == '__main__':
    main()
