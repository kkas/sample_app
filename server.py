# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.escape
from tornado.options import define, options

import os
from pymongo import MongoClient
from bson.objectid import ObjectId

""" Options used in this applicaitons. """
define("port", default=9999, help="port for this server")
define("mongo_host", default="127.0.0.1", help="Main mongoDB host")
define("mongo_port", default=27017, type=int, help="Main mongoDB port")
define("mongo_dbname", default="my_test_db", help="mongoDB dbname")


class Application(tornado.web.Application):
    def __init__(self):
        client = MongoClient(options.mongo_host, options.mongo_port)
        db = client[options.mongo_dbname]

        handlers = [
            (r"/", MainHandler),
            (r"/user", UserHandler, dict(db=db)),
            (r"/order", OrderHandler, dict(db=db)),
        ]

        settings = dict(
            debug=True,
            autoreload=True,
        )

        tornado.web.Application.__init__(self, handlers, **settings)


class UserHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.database = db

    def get(self):
        # リクエストのクエリストリングから user_id を取得する.
        query_args = self.request.query_arguments
        print(u'args: {}'.format(query_args))
        user_id = query_args['user_id'][0]
        print(u'user_id: {}'.format(user_id))

        # user_id で users コレクションを検索し user 情報を取得する.
        users = self.database.users
        user = users.find_one({'_id': ObjectId(user_id)})

        # 取得した user 情報でレスポンスを生成する.
        self.write(u'あなたのuser_idは{}ですね。\n'.format(user_id))
        self.write(u'こんにちは、{name}さん。あなたのメアドは{email}です。\n'.format(
                name=user['name'], email=user['email']))

    def post(self):
        body = self.request.body

        json = tornado.escape.json_decode(body)
        print("json data: {}".format(json))
        print("json type: {}".format(type(json)))

        # 取得したパラメタをDBに保存
        users = self.database.users
        user_id = users.insert_one(json).inserted_id

        self.write(u"Hi, Mr.{}\n".format(json['name']))
        self.write(u"あなたの user_id は{}です.".format(user_id))


class OrderHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.database = db

    def get(self):
        # orders = self.database.orders
        # order_id = orders.insert_one(order).inserted_id
        # self.write("order number: {}".format(order_id))
        pass

    def post(self):
        # # print("type of self: {}".format(type(self)))
        # body = self.request.body
        # print("body: {}".format(body))
        #
        # json = tornado.escape.json_decode(body)
        # print("json data: {}".format(json))
        # print("json type: {}".format(type(json)))
        #
        # # 取得したパラメタをDBに保存
        # users = self.database.users
        # user_id = users.insert_one(json).inserted_id
        #
        # self.write(u"Hi, Mr.{}\n".format(json['name']))
        # self.write(u"あなたの UserID は{}です.".format(user_id))
        pass

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")


def main():
    tornado.options.parse_config_file('server.conf')
    app = Application()

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print("Server running on {}...".format(options.port))
    tornado.ioloop.IOLoop.current().start()
  
if __name__ == "__main__":
    main()
