import logging

import slack_logger


def test_slack_logger():
    handler = slack_logger.SlackHandler('https://example.com')
    _logger = logging.getLogger('test_logger')
    _logger.addHandler(handler)
    _logger.warning('example message')
