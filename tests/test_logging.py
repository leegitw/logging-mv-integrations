#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)
#  @namespace logging_mv_integrations

from test import support
import unittest
import logging
import io
import os
from logging_mv_integrations import (
    LoggingFormat,
    LoggingOutput,
    get_logger,
    __version__
)

class LoggingTest(unittest.TestCase):

    def test_logging_format(self):
        self.assertTrue(LoggingFormat.validate(LoggingFormat.JSON))
        self.assertTrue(LoggingFormat.validate(LoggingFormat.STANDARD))
        self.assertFalse(LoggingFormat.validate("invalid"))

    def test_logging_output(self):
        self.assertTrue(LoggingOutput.validate(LoggingOutput.STDOUT))
        self.assertTrue(LoggingOutput.validate(LoggingOutput.STDOUT_COLOR))
        self.assertTrue(LoggingOutput.validate(LoggingOutput.FILE))
        self.assertFalse(LoggingOutput.validate("invalid"))

    def test_logging_file(self):
        log = get_logger(
            logger_name=__name__,
            logger_version=__version__,
            logger_level=logging.DEBUG,
            logger_output=LoggingOutput.FILE
        )

        self.assertIsNotNone(log)
        self.assertTrue(os.path.exists(log.logger_path))

        log.info("logging: info", extra={'test': __name__})
        log.debug("logging: debug", extra={'test': __name__})
        log.warning("logging: warning", extra={'test': __name__})
        log.error("logging: error", extra={'test': __name__})
        log.critical("logging: critical", extra={'test': __name__})
        log.exception("logging: exception", extra={'test': __name__})

        self.assertIsNotNone(log.logger_path)
        logger_fp = open(log.logger_path, 'r')
        self.assertIsNotNone(logger_fp)
        self.assertIsNotNone(logger_fp.readlines())

    def test_logging_buffer(self):
        buffer = io.StringIO()
        logger_handler = logging.StreamHandler(buffer)

        log = get_logger(
            logger_name=__name__,
            logger_version=__version__,
            logger_level=logging.DEBUG,
            logger_output=LoggingOutput.STDOUT,
            logger_handler=logger_handler
        )

        self.assertIsNotNone(log)

        log.info("logging: info", extra={'test': __name__})
        log.debug("logging: debug", extra={'test': __name__})
        log.warning("logging: warning", extra={'test': __name__})
        log.error("logging: error", extra={'test': __name__})
        log.critical("logging: critical", extra={'test': __name__})
        log.exception("logging: exception", extra={'test': __name__})

        self.assertIsNotNone(buffer.getvalue())
        buffer.close()


# Set the locale to the platform-dependent default.  I have no idea
# why the test does this, but in any case we save the current locale
# first and restore it at the end.
@support.run_with_locale('LC_ALL', '')
def test_main():
    tests = [LoggingTest]
    support.run_unittest(*tests)

if __name__ == "__main__":
    test_main()
