import tornado.web
import asyncio
import json
from pywebpush import webpush
from py_vapid import Vapid
import base64
from cryptography.hazmat.primitives import serialization


subscriptions = []
subscription = None
key = None

def base64UrlEncode(data: bytes) -> str:
    """Base64Url Encode data."""
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')


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
        keys = Vapid()
        keys.generate_keys()
        keys.save_key('private_key.pem')
        pub_key = base64.urlsafe_b64encode(keys.public_key.public_bytes(
            serialization.Encoding.X962,
            serialization.PublicFormat.UncompressedPoint
        )).rstrip(b'=').decode('utf-8')
        self.write(pub_key)



async def make_app():
    app = tornado.web.Application([
        (r'/send-sub', PushHandler),
        (r'/send-push', SendPushHandler),
        (r'/get-vapid', PushCertHandler),
        (r'/(.*)', tornado.web.StaticFileHandler, {"path":".", "default_filename": "index.html"}),
    ])
    app.listen(9998)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(make_app())