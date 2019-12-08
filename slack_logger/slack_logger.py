import json
import logging
import platform

import requests


class HostnameFilter(logging.Filter):
    hostname = platform.node()

    def filter(self, record):
        record.hostname = HostnameFilter.hostname
        return True


class SlackHandler(logging.Handler):
    def __init__(self, url: str) -> None:
        super().__init__()
        self._url = url
        self.addFilter(HostnameFilter())
        self.setFormatter(logging.Formatter(
            '%(hostname)s: %(message)s',
        ))

    def emit(self, record: logging.LogRecord) -> None:
        requests.post(
            url=self._url,
            headers={
                'Content-Type': 'application/json',
            },
            data=json.dumps({
                'text': self.format(record),
            }),
        )
