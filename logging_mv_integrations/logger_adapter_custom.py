#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)
#  @namespace logging_mv_integrations

import copy
import logging

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
        kwargs_clone = copy.deepcopy(kwargs)
        extra = kwargs_clone.get('extra')
        if extra:
            kwargs_clone['extra'].update({'version': self.extra['version']})
        else:
            kwargs_clone['extra'] = {'version': self.extra['version']}
        return msg, kwargs_clone
