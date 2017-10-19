#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)
#  @namespace logging_mv_integrations


from test import support
import unittest
import logging
import io
import os
from logging_mv_integrations import (
    LoggingOutput,
    get_logger,
    __version__
)

class LoggingTest(unittest.TestCase):

    def test_logging_output(self):
        self.assertTrue(LoggingOutput.validate(LoggingOutput.STDOUT))
        self.assertTrue(LoggingOutput.validate(LoggingOutput.STDOUT_COLOR))
        self.assertTrue(LoggingOutput.validate(LoggingOutput.FILE))
        self.assertFalse(LoggingOutput.validate("invalid"))

    def test_logging_file(self):
        logger_file = "test_log"
        logger = get_logger(
            logger_name=__name__,
            logger_version=__version__,
            logger_level=logging.DEBUG,
            logger_output=LoggingOutput.FILE,
            logger_file=logger_file
        )

        self.assertIsNotNone(logger)
        self.assertTrue(os.path.exists(logger.logging_file))

        logger.info("logging: info", extra={'test': __name__})
        logger.debug("logging: debug", extra={'test': __name__})
        logger.warning("logging: warning", extra={'test': __name__})
        logger.error("logging: error", extra={'test': __name__})
        logger.critical("logging: critical", extra={'test': __name__})
        logger.exception("logging: exception", extra={'test': __name__})

        self.assertIsNotNone(logger.logging_file)
        logger_fp = open(logger.logging_file, 'r')
        self.assertIsNotNone(logger_fp)
        self.assertIsNotNone(logger_fp.readlines())

    def test_logging_buffer(self):
        buffer = io.StringIO()
        logger_handler = logging.StreamHandler(buffer)

        logger = get_logger(
            logger_name=__name__,
            logger_version=__version__,
            logger_level=logging.DEBUG,
            logger_output=LoggingOutput.STDOUT,
            logger_handler=logger_handler
        )

        self.assertIsNotNone(logger)

        logger.info("logging: info", extra={'test': __name__})
        logger.debug("logging: debug", extra={'test': __name__})
        logger.warning("logging: warning", extra={'test': __name__})
        logger.error("logging: error", extra={'test': __name__})
        logger.critical("logging: critical", extra={'test': __name__})
        logger.exception("logging: exception", extra={'test': __name__})

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
