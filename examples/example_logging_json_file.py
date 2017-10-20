#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)
#  @namespace logging_mv_integrations

import logging
from logging_mv_integrations import (
    LoggingFormat,
    LoggingOutput,
    get_logger,
    __version__
)
from pprintpp import pprint

logger = get_logger(
    logger_name=__name__,
    logger_version=__version__,
    logger_level=logging.NOTE,
    logger_format=LoggingFormat.JSON,
    logger_output=LoggingOutput.FILE
)

logger.info("logging: info", extra={'test': __name__})
logger.note("logging: note", extra={'test': __name__})
logger.debug("logging: debug", extra={'test': __name__})
logger.warning("logging: warning", extra={'test': __name__})
logger.error("logging: error", extra={'test': __name__})
logger.critical("logging: critical", extra={'test': __name__})
logger.exception("logging: exception", extra={'test': __name__})

pprint(f"Logger file path: {logger.logging_file}")

logger_fp = open(logger.logging_file, 'r')
pprint(logger_fp.readlines())

pprint(logger.getLevelName())
