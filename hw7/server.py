import tornado.web
import asyncio
import json
from pywebpush import webpush


subscriptions = []
subscription = None


class PushHandler(tornado.web.RequestHandler):
    def post(self):
        subscription = json.loads(self.request.body)
        subscriptions.append(subscription)
    get = post


class SendPushHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.dumps({
                'title': 'Hello there',
                'body': 'General Kenobi!',
            })
        for subscription in subscriptions:
            webpush(
                subscription_info=subscription,
                data=data,
                vapid_private_key='./private_key.pem',
                vapid_claims={"sub": "mailto:anpilov2611@gmail.com"}
            )
    get=post
        


class PushCertHandler(tornado.web.RequestHandler):
    def get(self):
        with open('app_key.txt', 'r') as f:
            self.write(f.read())


async def make_app():
    app = tornado.web.Application([
        (r'/send-sub', PushHandler),
        (r'/send-push', SendPushHandler),
        (r'/get-vapid', PushCertHandler),
        (r'/(.*)', tornado.web.StaticFileHandler, {"path":".", "default_filename": "index.html"}),
    ])
    app.listen(8000)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(make_app())