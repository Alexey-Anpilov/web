import tornado.web
import asyncio

class RequestCounterHandler(tornado.web.RequestHandler):
    request_count = 0
    
    def get(self):
        RequestCounterHandler.request_count += 1
        self.write(f"Порядковый номер запроса: {self.request_count}")


async def make_app():
    app = tornado.web.Application([
        (r"/request_number", RequestCounterHandler),
        (r"/hw/(.*)", tornado.web.StaticFileHandler, {"path":"../hw1-2/", "default_filename": "index.html"}),
    ])
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(make_app())