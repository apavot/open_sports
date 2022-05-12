from audioop import add
import datetime
import re
import urllib

import utils


class BaseParsing:
    _instance = {}
    _register_class = {}

    URL = ""
    REGEX_SUB_PATTERN_URL = ""
    REGEX_REPL_PATTERN_URL = ""
    MAIN_LINK = ""

    def __init_subclass__(cls):
        """Register Class."""
        cls._register_class[cls.URL] = cls

    def __new__(cls, url):
        """Return instance of the class.

        Args:
            url (str): Type of the instance to get.

        Returns:
            BaseParsing: Instance.
        """
        if url not in cls._instance:
            cls._instance[url] = super().__new__(cls._register_class[url])        
        return cls._instance[url]

    def __init__(self, url):
        utils.setup_connection()

    def request_page(self, address, php=False):
        """

        Args:
            address (_type_): _description_
            php (bool, optional): _description_. Defaults to False.

        Returns:
            _type_: _description_
        """
        print("Address:", address)

        if php:
           req = urllib.request.Request(
               address, headers={'User-Agent' : "Magic Browser"}
           ) 
        else:
            req = urllib.request.Request(address) 

        try:
            response = urllib.request.urlopen(req)
        except urllib.error.URLError as e:
            #response = request_page(address, php=php) 
            print("ERROR URL: {}".format(e.reason))
            response = ""

        return response

    def _check_ip(self):
        print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        address = "http://checkip.dyndns.org"
        print("IP ADDERSS: {}".format(self.request_page(address)))

    def _build_url(self, link):
        """Build URL.

        Args:
            link (str): Part of the url.

        Returns:
            str: Url to query.
        """
        address = "{}{}".format(
            self.URL_PREFIX,
            re.sub(
                self.REGEX_SUB_PATTERN_URL,
                self.REGEX_REPL_PATTERN_URL,
                link,
            )
        )
        return address

    def dispatch_request(self, body):
        """Dispatch request.

        Args:
            body (dict): Information received.

        Returns:
            dict: Data parsed.
        """
        _type = body.get("type")
        print(f"TEST {body}")
        info = body.get(_type, {})
        link = info.get("link") or self.MAIN_LINK
        address = self._build_url(link)
        
        if _type == "main":
            return self.get_first_page_data(address)
        elif _type == "game":
            return self.get_game_link(address)
        elif _type == "stream":
            return self.get_game_stream(address)
        elif _type == "test_ip":
            self._check_ip()
        
        return {}

