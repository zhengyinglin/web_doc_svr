#coding=utf-8
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import options
import os
import handler

tornado.options.define('port', default=8080, type=int, help=("Server port"))

local_path = os.path.dirname(__file__)

settings = {
       "debug": True , 
       #"template_path": os.path.join(local_path, "templates"),
       "static_path":   os.path.join(local_path, "static"),
}


handler.set_path( settings['static_path'] )

application = tornado.web.Application([
    (r"/", handler.MainHandler),
    (r'/(favicon.ico)', tornado.web.StaticFileHandler, {"path": ""}),
    (r'/dochtml', handler.HtmIndexHandler), 
] ,  **settings )


if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
