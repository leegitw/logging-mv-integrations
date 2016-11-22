#!/usr/bin/env python3

import logging
import json
import sys
import traceback

import sys
import gc

import logging
import json
import sys
import traceback

try:
    import xmlrunner
except ImportError:
    pass

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from pythonjsonlogger import jsonlogger
import json_log_formatter

from logging_mv_integrations.errors import (print_traceback)


class ExampleJsonLogger(object):

    _INTEGRATION_NAME = "Example: JsonLogger"
    LOGGER_NAME = 'example-json-logger'

    # Initialize Job
    #
    def __init__(self):
        pass

    def runJsonFormatter(self):
        print('jsonlogger.JsonFormatter')
        logger = logging.getLogger(self.LOGGER_NAME)
        logger.setLevel(logging.DEBUG)

        logHandler = logging.StreamHandler()
        logger.addHandler(logHandler)

        formatter = jsonlogger.JsonFormatter()
        logHandler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)

        msg = {"text": "testing logging", "num": 1, 5: "9", "nested": {"more": "data"}}

        logger.info(msg)

        extra = {"text": "testing logging", "num": 1, 5: "9", "nested": {"more": "data"}}

        logger.info("hello", extra=extra)

        SUPPORTED_KEYS = [
            'asctime', 'created', 'filename', 'funcName', 'levelname', 'levelno', 'lineno', 'module', 'msecs',
            'message', 'name', 'pathname', 'process', 'processName', 'relativeCreated', 'thread', 'threadName'
        ]

        log_format = lambda x: ['%({0:s})'.format(i) for i in x]
        custom_format = ' '.join(log_format(SUPPORTED_KEYS))

        formatter = jsonlogger.JsonFormatter(custom_format)
        logHandler.setFormatter(formatter)

        msg = "A testing logging format"
        logger.info(msg)

        msg = {"text": "B testing logging", "num": 1, 5: "9", "nested": {"more": "data"}}

        logger.info(msg)

        extra = {"text": "C testing logging", "num": 1, 5: "9", "nested": {"more": "data"}}

        logger.info("hello", extra=extra)

    def runJsonLogFormatter(self):
        print('json_log_formatter.JSONFormatter')
        logger = logging.getLogger(self.LOGGER_NAME)
        logger.setLevel(logging.DEBUG)

        logHandler = logging.StreamHandler()
        logger.addHandler(logHandler)

        formatter = json_log_formatter.JSONFormatter()
        logHandler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)

        msg = {"text": "testing logging", "num": 1, 5: "9", "nested": {"more": "data"}}

        logger.info(msg=msg)

        extra = {"text": "testing logging", "num": 1, 5: "9", "nested": {"more": "data"}}

        logger.info("hello", extra=extra)

        FORMAT_KEYS = {}

        SUPPORTED_KEYS = {
            'args',
            'asctime',
            'created',
            'exc_info',
            'exc_text',
            'filename',
            'funcName',
            'levelname',
            'levelno',
            'lineno',
            'module',
            'msecs',
            'message',
            'msg',
            'name',
            'pathname',
            'process',
            'processName',
            'relativeCreated',
            'stack_info',
            'thread',
            'threadName',
        }

        log_format = lambda x: ['%({0:s})'.format(i) for i in x]
        custom_format = ' '.join(log_format(SUPPORTED_KEYS))

        formatter = json_log_formatter.JSONFormatter(custom_format)
        logHandler.setFormatter(formatter)

        msg = "testing logging format"
        logger.info(msg=msg)

        msg = {"text": "testing logging", "num": 1, 5: "9", "nested": {"more": "data"}}

        logger.info(msg=msg)

        extra = {"text": "testing logging", "num": 1, 5: "9", "nested": {"more": "data"}}

        logger.info("hello", extra=extra)


def main():
    """Main
    """

    job = ExampleJsonLogger()

    try:
        job.runJsonFormatter()
        job.runJsonLogFormatter()

    except Exception as ex:
        print_traceback(ex)


if __name__ == '__main__':
    sys.exit(main())
