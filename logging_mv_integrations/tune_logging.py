#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)
#  @namespace logging_mv_integrations

import copy
import logging
import logging.config
from .logging_json_formatter import LoggingJsonFormatter
from .logging_format import TuneLoggingFormat


class CustomAdapter(logging.LoggerAdapter):

    def process(self, msg, kwargs):
        kwargs_clone = copy.deepcopy(kwargs)
        extra = kwargs_clone.get('extra')
        if extra:
            kwargs_clone['extra'].update({'version': self.extra['version']})
        else:
            kwargs_clone['extra'] = {'version': self.extra['version']}
        return msg, kwargs_clone


def get_logging_level(str_logging_level):

    assert str_logging_level
    str_logging_level = str_logging_level.upper()

    return {
        'NOTSET': logging.NOTSET,
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }.get(str_logging_level, logging.INFO)


def get_logger(logger_name, logger_version=None, logger_level=logging.INFO, logger_format=None):

    if logger_format == TuneLoggingFormat.STANDARD:
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    else:
        formatter = LoggingJsonFormatter(
            logger_name,
            logger_version,
            fmt='%(asctime)s %(levelname)s %(name)s %(version)s %(message)s'
        )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logger_level)
    if not len(logger.handlers):
        logger.addHandler(handler)

    adapter = CustomAdapter(logger, {'version': logger_version})

    return adapter





