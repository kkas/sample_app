# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado import gen
from tornado.httpclient import AsyncHTTPClient, HTTPError
from tornado.options import define, options

import json

from pyquery import PyQuery

""" Options used in this applicaitons. """
define("port", default=5555, help="port for this server")


class AsyncHandler(tornado.web.RequestHandler):

    url = "http://search.hatena.ne.jp/asinsearch?word=%A5%B9%A5%DE%A5%DB&type=All"
    # url = "http://www.google.co.jp"

    @gen.coroutine
    def get(self):
        http_client = AsyncHTTPClient()
        try:
            response = yield http_client.fetch(self.url)
            # raise gen.Return(response.body)
            res = self.__handle_response(response)
            self.set_header('content-type', 'application/json; charset=UTF-8')
            print type(res)
            self.write(str(res))
            self.finish()
        # self.write(response.body)
        # self.finish()
        finally:
            http_client.close()

        # try:
        #     response = yield http_client.fetch(self.url)
        #     # print 'response.body: {}'.format(response.body)
        #     # raise gen.Return(response.body)
        #     print 'aaaa'
        #     raise gen.Return('OK!')
        # except HTTPError as e:
        #     # HTTPError is raised for non-200 responses; the response
        #     # can be found in e.response.
        #     print("Error: " + str(e))
        # # except Exception as e:
        # #     # Other errors are possible, such as IOError.
        # #     print("Error: " + str(e))
        # finally:
        #     http_client.close()

    def extract_items(self, html):
        items = []

        dom = PyQuery(html)
        dom('div.hatena-search-result div.asin-item').each(lambda i, node: items.append(PyQuery(node).html()))

        return items

    def __handle_response(self, response):
        items = self.extract_items(response.body)
        print 'items[0]: {}'.format(items[0])
        items_json = json.dumps(items)
        print 'items_json: {}'.format(items_json)
        return items_json

    def _to_json(self, items_list):
        ret = []
        for item in items_list:
            dom = PyQuery(item)
            dict(

            )

        # if response.error:
        #   response.rethrow()
        # self.set_header('content-type', 'application/atom+xml; charset=UTF-8')
        # self.write(response.body)
        # self.finish()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", AsyncHandler)
        ]

        settings = dict(
            debug=True,
            autoreload=True,
        )

        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    app = Application()

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print("Server running on {}...".format(options.port))
    tornado.ioloop.IOLoop.current().start()
  
if __name__ == "__main__":
    main()
