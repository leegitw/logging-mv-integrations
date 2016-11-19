
import logging
from logging_mv_integrations import (
    TuneLogging,
    TuneLoggingFormat,
    __version__
)

tune_logger_json = TuneLogging(
    logger_name=__name__.split('.')[0],
    logger_version=__version__,
    logger_level=logging.DEBUG,
    logger_format=TuneLoggingFormat.JSON
)

tune_logger_json.info(
    "logging: info",
    extra={
        'test': __name__
    }
)
tune_logger_json.debug(
    "logging: debug",
    extra={
        'test': __name__
    }
)
tune_logger_json.warning(
    "logging: warning",
    extra={
        'test': __name__
    }
)
tune_logger_json.error(
    "logging: error",
    extra={
        'test': __name__
    }
)
tune_logger_json.critical(
    "logging: critical",
    extra={
        'test': __name__
    }
)
tune_logger_json.exception(
    "logging: exception",
    extra={
        'test': __name__
    }
)