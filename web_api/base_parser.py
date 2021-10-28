import datetime
from enum import IntFlag
import re

from bs4 import BeautifulSoup

from utils import request_page


class BaseParser:

    URL = "http://livetv.sx"
    #URL = "http://livetv464.me"


    def get_game_stream(self, html):
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

    def get_game_link(self, html):
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

    def get_first_page_data(self, html):
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
       
    def dispatch_request(self, body):
        _type = body.get("type")

        info = body.get("info", {})
        if not info:
            return {}

        link = info.get("link")
        if _type == "main":
            address = "{}{}".format(self.URL, link)
            html = request_page(address)
            return self.get_first_page_data(html)
        
        elif _type == "game":
            address = "{}{}".format(self.URL, link)
            html = request_page(address)
            return self.get_game_link(html)
        
        elif _type == "stream":
            address = "http:{}".format(link)
            html = request_page(address, php=True)
            return self.get_game_stream(html)
        
        elif _type == "test_ip":
            self.check_ip()
            return ()
        else:
            return {}