import tornado.ioloop
import tornado.web
import tornado.websocket
import asyncio

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print('WebSocket opened')

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        print("WebSocket closed")

    def check_origin(self, origin):
        return True

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/websocket", EchoWebSocket),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8080, 'localhost')
    tornado.ioloop.IOLoop.current().start()