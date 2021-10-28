
from stem import Signal
from stem.control import Controller

import urllib
import socket
import socks



#controller = Controller.from_port(port=9051)
#
#def connectTor():
#    socks.setdefaultproxy(
#        socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True
#    )
#    socket.socket = socks.socksocket
#
#
#def renewTor():
#    controller.authenticate("abc123")
#    controller.signal(Signal.NEWNYM)
#
#
#def request_page(address, php=False):
#    print("LOG: {}".format(address))
#
#    if php:
#        req = urllib.request.Request(
#            address, headers={'User-Agent' : "Magic Browser"}
#        ) 
#    else:
#        req = urllib.request.Request(address) 
#
#    try:
#        response = urllib.request.urlopen(req)
#    except urllib.error.URLError as e:
#        print("ERROR URL: {}".format(e.reason))
#        response = ""
#
#    return response
#
#
#def setup_connection(renew=False):
#    if renew:
#        #renewTor()
#        pass
#    
#    #renewTor()
#    connectTor()
#