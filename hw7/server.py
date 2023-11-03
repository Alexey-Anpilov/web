import tornado.web
import asyncio


class SendVapidHandler(tornado.web.RequestHandler):
    def get(self):
        vapid_key = 'BDcOOWtidN65AtFOqAsE1W6613r4bZg1aPGtHSQe5up3GplKjtbLLHYJNx5-Nak8HEgwAi5HxKUhmsPkOqqd41I'
        self.write(vapid_key)       

class GetPushSubsciptionHandler(tornado.web.RequestHandler):
    def post(self):
        pass


async def make_app():
    app = tornado.web.Application([
        (r"/send_vapid", SendVapidHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path":".", "default_filename": "index.html"})

    ])
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(make_app())