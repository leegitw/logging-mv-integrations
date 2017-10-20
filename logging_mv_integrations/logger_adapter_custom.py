#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)
#  @namespace logging_mv_integrations

import copy
import logging

from .logging_levels import NOTE_NUM

class LoggerAdapterCustom(logging.LoggerAdapter):
    """
    An adapter for loggers which makes it easier to specify contextual
    information in logging output.
    """

    __logging_output = None
    __logging_file = None

    def __init__(self, logging_output, logging_file, *args, **kwargs):
        """
        Initialize the adapter
        """
        self.__logging_output = logging_output
        self.__logging_file = logging_file
        super(LoggerAdapterCustom, self).__init__(*args, **kwargs)

    @property
    def logging_output(self):
        return self.__logging_output

    @property
    def logging_file(self):
        return self.__logging_file

    def process(self, msg, kwargs):
        """
        Process the logging message and keyword arguments.
        """
        try:
            _kwargs = copy.deepcopy(kwargs)
        except TypeError:
            _kwargs = kwargs

        extra = _kwargs.get('extra')
        if extra:
            _kwargs['extra'].update({'version': self.extra['version']})
        else:
            _kwargs['extra'] = {'version': self.extra['version']}
        return msg, _kwargs

    def note(self, msg, *args, **kwargs):
        """
        Delegate an note call to the underlying logger.
        """
        self.log(NOTE_NUM, msg, *args, **kwargs)

    def getLevelName(self):
        return logging.getLevelName(self.getEffectiveLevel())