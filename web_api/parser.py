import re
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup

import urllib
import socket
import socks

import datetime


URL = "http://livetv.sx"
#URL = "http://livetv464.me"

ADDRESS = "proxy-tor"
#ADDRESS = "127.0.0.1"

#controller = Controller.from_port(
#    address=ADDRESS, port=9051
#)

def connectTor():
    socks.setdefaultproxy(
        socks.PROXY_TYPE_SOCKS5, ADDRESS, 9050, True
    )
    socket.socket = socks.socksocket


def renewTor():
    #controller.authenticate("abc123")
    controller.signal(Signal.NEWNYM)


def request_page(address, php=False):
    print(address)

    #if php:
    req = urllib.request.Request(
        address, headers={'User-Agent' : "Magic Browser"}
    ) 
    #else:
    #    req = urllib.request.Request(address) 

    #response = urlopen(req)
    #print("RESPONSE:\n{}".format(response))
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        #response = request_page(address, php=php) 
        print("ERROR URL: {}".format(e.reason))
        response = ""

    return response


def setup_connection(renew=False):
    if renew:
        #renewTor()
        pass
    
    #renewTor()
    connectTor()


def format_template(string_in, tokens):
    for key, value in tokens.items():
        string_in = string_in.replace(key, str(value))
    
    return string_in


def save_file(string_in):
    path = "/mnt/c/Users/apavo/dev_code/test/html/test_lvplayer.html"
    try:
        with open(path, 'w') as file:
            file.write(string_in)
        
        print("Success to save '{}'".format(path))
    except:
        print("Failed to save '{}'".format(path))


def get_game_stream(html):
    streams = []

    soup = BeautifulSoup(html, "html.parser")

    iframes = soup.find_all("iframe", allowfullscreen=True)
    if not iframes:
        return streams

    for iframe in iframes:
        link = iframe.attrs.get("src")
        if link:
            streams.append(link)

    #print(streams) 
    return streams


def get_game_link(html):
    links = []
    soup = BeautifulSoup(html, "html.parser")

    _a = soup.find_all("a", title="Îòêðûòü â íîâîì îêíå")
    index = 1 
    for a in _a:
        link = a.attrs.get("href")
        if not link:
            continue
        
        languages = [
            i.attrs.get("title")
            for i in a.parent.parent.find_all("img") 
            if "title" in i.attrs
        ]
        language = "{:02}-{}".format(index,  languages[0] or "Unknown")

        links.append(
            {"link": link, "value": language, "label": language}
        )
        index += 1

    #print(links)
    return links


def get_first_page_data(html):
    data = {"categories": {}, "games": []}

    soup = BeautifulSoup(html, "html.parser")

    d = soup.select(".main b")
    cats = []
    for t in d:
        attrs = t.parent.attrs
        if "main" in attrs.get("class", []):
            name = t.contents[0]
            link = attrs.get("href")
            cats.append(
                {"link": link, "value": name, "label": name}
            )     

    data["categories"] = sorted(cats, key=lambda k:k["label"])

    d = soup.find_all("table", width="100%", cellpadding=12, cellspacing=0)
    live_class = d[0].select(".live") if d else []
    games = {}
    for t in live_class:
        name = t.contents[0]
        a = t.parent.select(".evdesc")[0].contents
        date = a[0].replace("\t", "").replace("\n", "")
        championship = a[-1].replace("\t", "").replace("\n", "")
        link = t.attrs.get("href")

        key = "{}_{}_{}".format(
            date, name, championship
        ).replace(" ", "")
        try:
            time_format = re.findall(" ([0-9]+):([0-9]+)", date)[0]
            date = "{:02}:{} - {}".format(
                int(time_format[0]), time_format[1], date.split(" at")[0]
            )
        except:
            date = date

        games[key] = {
            "value": name,
            "label": name,
            "date": date,
            "championship": championship,
            "link": link,
            }

    data["games"] = [value for (k,value) in sorted(games.items())]

    return data


def check_ip():
    print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    address = "http://checkip.dyndns.org"
    print("IP ADDERSS: {}".format(request_page(address)))


def main_page(info):
    link="/enx/allupcomingsports/1/"
    if info:
        link = info.get("link", link)
    
    print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    address = "{}{}".format(URL, link)
    html = request_page(address)
    data = get_first_page_data(html)
    print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    return data


def link_page(game):
    if not game:
        return []

    print("\n{}".format(game))
    address = "{}{}".format(URL, game.get("link"))
    html = request_page(address)
    links = get_game_link(html)
    print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    return links


def stream_page(link):
    streams = []    
    if not link:
        return streams

    print("\n{} {}".format(link.get("language", "-"), link.get("link")))
    address = "http:{}".format(link.get("link"))
    html = request_page(address, php=True)
    streams = get_game_stream(html)
    print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

    return streams


def dispatch_request(body):
    _type = body.get("type")

    if _type == "main":
        info = body.get("info", {})
        return main_page(info)
    elif _type == "game":
        game = body.get("info", {})
        return link_page(game)
    elif _type == "stream":
        stream = body.get("info", {})
        return stream_page(stream)
    elif _type == "test_ip":
        check_ip()
        return ()
    else:
        return {}