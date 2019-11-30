import json
import logging

import requests


class SlackLogger(logging.Handler):
    def __init__(self, url):
        super().__init__()
        self._url = url

    def emit(self, record):
        requests.post(
            url=self._url,
            headers={
                'Content-Type': 'application/json',
            },
            data=json.dumps({
                'text': self.format(record),
            }),
        )
