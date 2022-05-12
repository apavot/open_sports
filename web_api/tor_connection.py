
from tornado            import gen
from tornado.concurrent import run_on_executor
from tornado.ioloop     import IOLoop 
from tornado.web        import Application, RequestHandler
 
from concurrent.futures import ThreadPoolExecutor 

from base_parser import BaseParsing
from parser_livetv import LiveTv

import ast
import json

MAX_WORKERS = 2 


class TornadoTest(RequestHandler):
    
    def get(self):
        self.write("Hello world!")


class TornadoServer(RequestHandler):
    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    
    def set_default_headers(self):
        self.set_header('Accept', 'application/json')
        self.set_header("Content-type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "http://localhost:3000")
        self.set_header("Access-Control-Allow-Headers", "Origin, Content-Type,  X-Requested-With, Accept, Authorization")
        self.set_header("Access-Control-Allow-Methods", "POST, OPTIONS")

    @run_on_executor
    def get_page(self, body):
        return BaseParsing("//livetv.sx").dispatch_request(body)
    
    @gen.coroutine
    def post(self):
        body = ast.literal_eval(self.request.body.decode("utf-8"))
        print("LOG: {}".format(body))
        data = yield self.get_page(body)
        self.write(json.dumps({'message': data}))
        self.finish()


def make_app():
    urls = [
      ("/", TornadoTest),
      ("/api/item", TornadoServer)
    ]
    print("Tornado ready")
    return Application(urls, debug=True)


if __name__ == '__main__':
    app = make_app()
    app.listen(3001)
    IOLoop.instance().start()
