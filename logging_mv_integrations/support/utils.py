#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)
#  @namespace logging_mv_integrations

import logging
# from pprintpp import pprint

from logging_mv_integrations.logging_format import (
    TuneLoggingFormat
)
from logging_mv_integrations.tune_logging_handler import (
    TuneLoggingHandler
)

def safe_cast(val, to_type, default=None):
    """Safely cast value to type, and if failed, returned default.
    Args:
        val:
        to_type:
        default:
    Returns:
    """
    if val is None:
        return default

    try:
        return to_type(val)
    except ValueError:
        return default


def safe_str(val):
    """Safely cast value to str
    Args:
        val:
    Returns:
    """
    return safe_cast(val, str, "")


def safe_float(val, ndigits=2):
    """Safely cast value to float
    Args:
        val:
    Returns:
    """
    return round(safe_cast(val, float, 0.0), ndigits)


def safe_int(val):
    """Safely cast value to int
    Args:
        val:
    Returns:
    """
    return safe_cast(safe_float(val, 0), int, 0)


def safe_dict(val):
    """Safely cast value to dict
    Args:
        val:
    Returns:
    """
    return safe_cast(val, dict, {})

def get_tune_logger_with_handler(
    logger_name,
    logger_version,
    logger_format,
    logger_level=logging.NOTSET,
    logger=None
):
    if not logger_name:
        raise ValueError(
            "Undefined 'logger_name'"
        )
    if not logger_version:
        raise ValueError(
            "Undefined 'logger_version'"
        )
    if not logger_format:
        raise ValueError(
            "Undefined 'logger_format'"
        )

    if not TuneLoggingFormat.validate(logger_format):
        raise ValueError(
            "Invalid 'logger_format': {}".format(
                logger_format
            )
        )

    tune_loggin_handler = TuneLoggingHandler(
        logger_format=logger_format
    )

    tune_loggin_handler.add_logger_version(
        logger_name,
        logger_version
    )

    if logger_level == logging.NOTSET:
        logger_level = logging.INFO

    if logger is None:
        logger = logging.getLogger(logger_name)

    logger.addHandler(tune_loggin_handler.log_handler)
    logger.setLevel(level=logger_level)

    return logger
