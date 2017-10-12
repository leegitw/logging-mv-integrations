.. -*- mode: rst -*-

========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |license|
    * - tests
      - |travis| |coveralls|
    * - package
      - |version| |supported-versions|

.. |docs| image:: https://readthedocs.org/projects/logging-mv-integrations/badge/?style=flat
    :alt: Documentation Status
    :target: https://readthedocs.org/projects/logging-mv-integrations

.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: License Status
    :target: https://opensource.org/licenses/MIT

.. |travis| image:: https://travis-ci.org/TuneLab/logging-mv-integrations.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/TuneLab/logging-mv-integrations

.. |coveralls| image:: https://coveralls.io/repos/TuneLab/logging-mv-integrations/badge.svg?branch=master&service=github
    :alt: Code Coverage Status
    :target: https://coveralls.io/r/TuneLab/logging-mv-integrations

.. |requires| image:: https://requires.io/github/TuneLab/logging-mv-integrations/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/TuneLab/logging-mv-integrations/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/logging_mv_integrations.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/logging_mv_integrations

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/tune_reporting.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/tune_reporting

.. end-badges

logging-mv-integrations
========================

``logging-mv-integrations`` is a Python logging library for TUNE Multiverse Integrations.

Usage
-----

.. code-block:: python
    import logging

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

Example
-------

.. code-block:: bash
    python3 examples/example_logger_json.py

    2017-10-12 15:13:44,235 root         DEBUG    often makes a very good meal of visiting tourists
    2017-10-12 15:13:44,236 root         INFO     Hello World
    2017-10-12 15:13:44,236 root         DEBUG    This message should go to the log file
    2017-10-12 15:13:44,236 root         INFO     So should this
    2017-10-12 15:13:44,236 root         WARNING  And this, too
    2017-10-12 15:13:44,237 root         INFO     Hello World

    {"message": "Hello World"}
    {"asctime": "2017-10-12 15:13:44,238", "levelname": "DEBUG", "process": 6029, "thread": 140737014789056, "module": "example_logger_json", "message": "foo"}
    2017-10-12 15:13:44,238 my_logger    DEBUG    foo
    {"message": "foo"}
    {"asctime": "2017-10-12 15:13:44,238", "levelname": "DEBUG", "process": 6029, "thread": 140737014789056, "module": "example_logger_json", "message": "bar"}
    2017-10-12 15:13:44,238 my_logger    DEBUG    bar
    {"message": "bar"}

Dependencies
============

``logging-mv-integrations`` module is built upon Python 3 and is build upon
several custom modules that are held within .. _PyPI: https://pypi.python.org/pypi

.. code-block:: bash
    python3 -m pip install --upgrade -r requirements.txt

TuneLab Generic Custom Packages
-------------------------------

These other packages provide support functionality but are not core
to Multiverse. Thereby, test and documentation could be shared
amongst the team.

* .. _safe-cast: https://pypi.python.org/pypi/safe-cast

Required Support Packages
-------------------------

* .. _coloredlogs: https://pypi.python.org/pypi/coloredlogs
* .. _pprintpp: https://pypi.python.org/pypi/pprintpp
* .. _python-json-logger: https://pypi.python.org/pypi/python-json-logger
* .. _Pygments: https://pypi.python.org/pypi/Pygments
* .. _wheel: https://pypi.python.org/pypi/wheel


Acknowledgements
================

.. include:: AUTHORS.rst

Reporting Issues
================

We definitely want to hear your feedback.

Report issues using the `Github Issue Tracker`:
https://github.com/TuneLab/tune-mv-integration-python/issues

HISTORY
=======

.. include:: HISTORY.rst
