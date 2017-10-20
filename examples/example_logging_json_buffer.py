#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)
#  @namespace logging_mv_integrations

import io
import logging
import json
from logging_mv_integrations import (
    LoggingFormat,
    LoggingOutput,
    get_logger,
    __version__
)
from pprintpp import pprint

buffer = io.StringIO()
logger_handler = logging.StreamHandler(buffer)

logger = get_logger(
    logger_name=__name__,
    logger_version=__version__,
    logger_level=logging.NOTE,
    logger_format=LoggingFormat.JSON,
    logger_output=LoggingOutput.STDOUT,
    logger_handler=logger_handler
)

logger.info("logging: info", extra={'test': __name__})
logger.note("logging: note", extra={'test': __name__})
logger.debug("logging: debug", extra={'test': __name__})
logger.warning("logging: warning", extra={'test': __name__})
logger.error("logging: error", extra={'test': __name__})
logger.critical("logging: critical", extra={'test': __name__})
logger.exception("logging: exception", extra={'test': __name__})

buffer_str = buffer.getvalue()
buffer_str = buffer_str.replace('\n',',')
buffer_str = buffer_str[:-1]
buffer_str = '[' + buffer_str + ']'

logJson = json.loads(buffer_str)
pprint(logJson)
buffer.close()

pprint(logger.getLevelName())

