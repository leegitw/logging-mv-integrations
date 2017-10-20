#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)
#  @namespace logging_mv_integrations

import os
import logging
import logging.config
import time
import math

from .logging_json_formatter import LoggingJsonFormatter
from .logger_adapter_custom import LoggerAdapterCustom

from .logging_format import LoggingFormat
from .logging_output import LoggingOutput


def get_logger(
    logger_name,
    logger_version=None,
    logger_level=logging.INFO,
    logger_format=LoggingFormat.JSON,
    logger_output=LoggingOutput.STDOUT_COLOR,
    logger_handler=None
):
    """
        logger_name      Return a logger with the specified logger_name, creating it if necessary.
        logger_level     Set the root logger level to the specified level.
        logger_format    LoggerFormat.
        logger_output    LoggerOutput.
        logger_handler   Provide custom logging handler.
    """
    if logger_format == LoggingFormat.STANDARD:
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    else:
        formatter = LoggingJsonFormatter(
            logger_name,
            logger_version,
            logger_output=logger_output,
            fmt='%(asctime)s %(levelname)s %(name)s %(version)s %(message)s'
        )

    logging_file = None
    if logger_handler is None:
        if logger_output == LoggingOutput.FILE:

            logging_dir = "./tmp"
            if not os.path.isdir(logging_dir):
                os.makedirs(logging_dir)

            # Log name combines logger_format and epoch time in seconds
            # rounded-up to the nearest 10 seconds
            epoch_time_sec = int(time.time())
            epoch_time_sec_ceil = int(math.ceil((epoch_time_sec + 10) / 10.0)) * 10
            logging_file = f"{logging_dir}/log_{logger_format}_{epoch_time_sec_ceil}.json"

            open(logging_file, "w+")
            logger_handler = logging.FileHandler(logging_file, encoding='utf-8')
        else:
            logger_handler = logging.StreamHandler()

    logger_handler.setFormatter(formatter)

    log = logging.getLogger(logger_name)
    log.setLevel(logger_level)

    if not len(log.handlers):
        log.addHandler(logger_handler)

    return LoggerAdapterCustom(logger_output, logging_file, log, {'version': logger_version})
