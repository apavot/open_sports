
from stem import Signal
from stem.control import Controller

import socket
import socks


ADDRESS = "proxy-tor"
#ADDRESS = "127.0.0.1"


#controller = Controller.from_port(port=9051)
def renewTor():
    #controller.authenticate("abc123")
    #controller.signal(Signal.NEWNYM)
    pass


def connectTor():
    socks.setdefaultproxy(
        socks.PROXY_TYPE_SOCKS5, ADDRESS, 9050, True
    )
    socket.socket = socks.socksocket


def setup_connection(renew=False):
    if renew:
        renewTor()
        pass
    
    #renewTor()
    connectTor()
