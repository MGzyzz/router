from .base import BaseController


class PagesController(BaseController):

    def http_request(self, set_body):
        self.response.add_header('Content-Type:', 'text/html')
        self.response.add_header('Connection:', 'close')
        self.response.set_body(set_body)

    def list_page(self):
        self.http_request("""
        <a href="/one">First page</a><br/>

        <a href="/two">Second page</a><br/>

        <a href="/three">Third page</a><br/>
        """)

    def home(self):
        self.http_request('<h1>This is homepage</h1>')

    def about_us(self):
        self.http_request('<h1>This is about us page</h1>')

    def first_page(self):
        self.http_request("<h1>This is first page!</h1>")

    def second_page(self):
        self.http_request("<h1>This is second page!</h1>")

    def third_page(self):
        self.http_request("<h1>This is third page!</h1>")