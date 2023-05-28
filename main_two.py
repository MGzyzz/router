import socketserver

from controllers.pages import PagesController
from controllers.click import ClickerController
from router import Router
from request import Request
from response import Response
from static_responder import StaticResponder
import errors

HOST, PORT = '127.0.0.1', 1025


router = Router()
router.get('/', ClickerController, 'get')
router.get('/click', ClickerController, 'click')


class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self) -> None:
        request = Request(file=self.rfile)
        response = Response(file=self.wfile)

        static_responder = StaticResponder(request, response, 'static')

        router.run(request, response)
        
        print(
            f'Method: {request.method}\n'
            f'URI: {request.uri}\n'
            f'Protocol: {request.protocol}\n'
        )
        
        response.send()


socketserver.TCPServer.allow_reuse_address = True

with socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) as server:
    server.serve_forever()