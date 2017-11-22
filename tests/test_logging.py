#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)
#  @namespace logging_mv_integrations

import logging
import io
import os
from logging_mv_integrations import (
    LoggingFormat,
    LoggingOutput,
    get_logger,
    __version__
)

class TestLoggingMvIntegration():

    def test_logging_format(self):
        assert(LoggingFormat.validate(LoggingFormat.JSON) is True)
        assert(LoggingFormat.validate(LoggingFormat.STANDARD) is True)
        assert(LoggingFormat.validate("invalid") is False)

    def test_logging_output(self):
        assert(LoggingOutput.validate(LoggingOutput.STDOUT) is True)
        assert(LoggingOutput.validate(LoggingOutput.STDOUT_COLOR) is True)
        assert(LoggingOutput.validate(LoggingOutput.FILE) is True)
        assert(LoggingOutput.validate("invalid") is False)

    def test_logging_file(self):
        log = get_logger(
            logger_name=__name__,
            logger_version=__version__,
            logger_level=logging.DEBUG,
            logger_output=LoggingOutput.FILE
        )

        assert(log is not None)
        assert(os.path.exists(log.logger_path) is True)

        log.info("logging: info", extra={'test': __name__})
        log.debug("logging: debug", extra={'test': __name__})
        log.warning("logging: warning", extra={'test': __name__})
        log.error("logging: error", extra={'test': __name__})
        log.critical("logging: critical", extra={'test': __name__})
        log.exception("logging: exception", extra={'test': __name__})

        assert(log.logger_path)
        logger_fp = open(log.logger_path, 'r')
        assert(logger_fp)
        assert(logger_fp.readlines())

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

        assert(log is not None)

        log.info("logging: info", extra={'test': __name__})
        log.debug("logging: debug", extra={'test': __name__})
        log.warning("logging: warning", extra={'test': __name__})
        log.error("logging: error", extra={'test': __name__})
        log.critical("logging: critical", extra={'test': __name__})
        log.exception("logging: exception", extra={'test': __name__})

        assert(buffer.getvalue() is not None)
        buffer.close()

