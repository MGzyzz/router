from .base import BaseController


class ClickerController(BaseController):
    clicks = 0


    def get(self):
        self.response.add_header('Content-Type:', 'text/html')
        self.response.add_header('Connection:', 'close')
        self.response.set_body(f"""
        <p><b>{ClickerController.clicks}</b></p>
            <a href="/click">Click</a>
        """)


    def click(self):
        ClickerController.clicks += 1
        self.get()