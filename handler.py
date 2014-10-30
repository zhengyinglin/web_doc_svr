#coding=utf-8
import tornado.web
import os

_HTMLPath = None

def set_path(path):
    global _HTMLPath
    _HTMLPath = path 


_HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
%s
</body></html>"""


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("""<html><title>hmldoc</title><body>
<h1>Hello, world tornado simple hmldoc</h1>
<a href="/dochtml">some html doc</a>
</body></html>""")



class HtmIndexHandler(tornado.web.RequestHandler):
    def get_files(self):
        link = ""
        for item in os.walk(_HTMLPath):
            for filename in item[2]:
                filename = self.to_utf8(filename)
                link += '<p><a href=\"/static/%s" /a>%s</p>' %(filename, filename)
        return  _HTML %  link 

    def to_utf8(self, filename):
        try:
           return unicode(filename, 'gbk').encode('utf-8')
        except:
            return filename

    def get(self):
        self.write(self.get_files())