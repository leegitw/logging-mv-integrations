#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2016 TUNE, Inc. (http://www.tune.com)

import logging
from pythonjsonlogger import jsonlogger
from logging.config import dictConfig

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.debug('often makes a very good meal of %s', 'visiting tourists')

logger.info("Hello World")

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

logger.info("Hello World")

log_config = {
    'version': 1,
    'formatters': {
        'json': {
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'fmt': '[%(asctime)s] %(levelname)s::[%(process)d %(thread)d]::%(module)s - %(message)s',
        },
    },
    'handlers': {
        'stream': {
            'level': 'DEBUG',
            'formatter': 'json',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'my_logger': {
            'handlers': ['stream'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

dictConfig(log_config)
logger = logging.getLogger('my_logger')

logger.debug('foo')
logger.debug('bar')
