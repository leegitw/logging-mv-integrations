#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2018 TUNE, Inc. (http://www.tune.com)
#  @namespace logging_mv_integrations
"""
Helpers: Singleton
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # print('Singleton', cls.__name__, '__call__')
        if cls not in cls._instances:
            new_instance = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = new_instance

        instance = cls._instances[cls]
        # print('Singleton', cls.__name__, id(instance))
        return instance
