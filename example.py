import logging
import os

import slack_logger

if __name__ == '__main__':
    handler = slack_logger.SlackLogger(os.environ['HOOK_URL'])
    handler.setLevel(logging.INFO)

    _logger = logging.getLogger()
    _logger.setLevel(logging.INFO)
    _logger.addHandler(handler)

    _logger.info('hello slack')
