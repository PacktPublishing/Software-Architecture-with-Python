# Code Listing #6

"""

Multiuser chat server using Twisted

"""

# twisted_chat_server.py
        
from twisted.internet import protocol, reactor


class Chat(protocol.Protocol):
    """ Chat protocol """

    transports = {}
    peers = {}
    
    def connectionMade(self):
        self._peer = self.transport.getPeer()
        print 'Connected',self._peer
        
    def connectionLost(self, reason):
        self._peer = self.transport.getPeer()
        # Find out and inform other clients
        user = self.peers.get((self._peer.host, self._peer.port))
        if user != None:
            self.broadcast('(User %s disconnected)\n' % user, user)
            print 'User %s disconnected from %s' % (user, self._peer)

    def broadcast(self, msg, user):
        """ Broadcast chat message to all connected users except 'user' """

        for key in self.transports.keys():
            if key != user:
                if msg != "<handshake>":
                    self.transports[key].write('#[' + user + "]>>> " + msg)
                else:
                    # Inform other clients of connection
                    self.transports[key].write('(User %s connected from %s)\n' % (user, self._peer))                
        
    def dataReceived(self, data):
        """ Callback when data is ready to be read from the socket """
        
        user, msg = data.split(":")
        print "Got data=>",msg,"from",user
        self.transports[user] = self.transport
        # Make an entry in the peers dictionary
        self.peers[(self._peer.host, self._peer.port)] = user
        self.broadcast(msg, user)

class ChatFactory(protocol.Factory):
    """ Chat protocol factory """
    
    def buildProtocol(self, addr):
        return Chat()

if __name__ == "__main__":
    reactor.listenTCP(3490, ChatFactory())
    reactor.run()
