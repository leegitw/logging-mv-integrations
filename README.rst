.. -*- mode: rst -*-

logging-mv-integrations
-----------------------

Extension to Python `logging <https://docs.python.org/3/library/logging.html>`_ functionality
intended for TUNE Multiverse Integrations.


Badges
------

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs| |license|
    * - info
      - |hits| |contributors|
    * - tests
      - |travis| |coveralls|
    * - package
      - |version| |supported-versions|
    * - other
      - |requires|


.. |docs| image:: https://readthedocs.org/projects/logging-mv-integrations/badge/?style=flat
    :alt: Documentation Status
    :target: http://logging-mv-integrations.readthedocs.io

.. |hits| image:: http://hits.dwyl.io/TuneLab/logging-mv-integrations.svg
    :alt: Hit Count
    :target: http://hits.dwyl.io/TuneLab/logging-mv-integrations

.. |contributors| image:: https://img.shields.io/github/contributors/TuneLab/logging-mv-integrations.svg
    :alt: Contributors
    :target: https://github.com/TuneLab/logging-mv-integrations/graphs/contributors

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

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/logging-mv-integrations.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/logging-mv-integrations

.. end-badges


Install
-------

.. code-block:: bash

    pip install logging_mv_integrations


Architecture
------------

``logging-mv-integrations`` is an extension of the `logging facility for Python <https://docs.python.org/3/library/logging.html>`_
used for TUNE Multiverse Integrations providing custom logger levels, format, and output.

.. image:: ./images/logging_mv_integrations.png
   :scale: 50 %
   :alt: UML logging-mv-integrations


Function: get_logger()
----------------------

.. code-block:: python

    def get_logger(
        logger_name,
        logger_version=None,
        logger_level=logging.INFO,
        logger_format=LoggingFormat.JSON,
        logger_output=LoggingOutput.STDOUT_COLOR,
        logger_handler=None
    ):


get_logger(): Parameters
^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------+-------------------------------------------------------------------------------------------------------------------------+
| Parameter       | Purpose                                                                                                                 |
+=================+=========================================================================================================================+
| logger_name     | Return a logger with the specified name or, if name is None, return a logger which is the root logger of the hierarchy. |
+-----------------+-------------------------------------------------------------------------------------------------------------------------+
| logger_version  |                                                                                                                         |
+-----------------+-------------------------------------------------------------------------------------------------------------------------+
| logger_format   | LoggingFormat                                                                                                           |
+-----------------+-------------------------------------------------------------------------------------------------------------------------+
| logger_output   | LoggingOutput                                                                                                           |
+-----------------+-------------------------------------------------------------------------------------------------------------------------+
| logger_handler  | logging.StreamHandler() or logging.FileHandler()                                                                        |
+-----------------+-------------------------------------------------------------------------------------------------------------------------+



Logging Levels
^^^^^^^^^^^^^^

Same Python logging levels, including one additional level NOTE.

+------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Level      | Purpose                                                                                                                                        |
+============+================================================================================================================================================+
| DEBUG      | Detailed information, typically of interest only when diagnosing problems.                                                                     |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| NOTE       | Detailed information, request processing, for example, request using cURL.                                                                     |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| INFO       | Confirmation that things are working as expected.  *[DEFAULT]*                                                                                 |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| WARNING    | An indication that something unexpected happened, or indicative of some problem in the near future. The software is still working as expected. |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| ERROR      | Due to a more serious problem, the software has not been able to perform some function.                                                        |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| CRITICAL   | A serious error, indicating that the program itself may be unable to continue running.                                                         |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------+



Logging Format
^^^^^^^^^^^^^^

+------------+-------------------------------------------------------------------------------------------------------+
| Format     | Purpose                                                                                               |
+============+=======================================================================================================+
| STANDARD   | Standard logging format.                                                                              |
+------------+-------------------------------------------------------------------------------------------------------+
| JSON       | JSON logging format.  *[DEFAULT]*                                                                     |
+------------+-------------------------------------------------------------------------------------------------------+


.. code-block:: python

    class LoggingFormat(object):
        """TUNE Logging Format ENUM
        """
        STANDARD = "standard"
        JSON = "json"



Logging Output
^^^^^^^^^^^^^^

+--------------+----------------------------------------------------------------------------------------------+
| Output       | Purpose                                                                                      |
+==============+==============================================================================================+
| STDOUT       | Standard Output to terminal                                                                  |
+--------------+----------------------------------------------------------------------------------------------+
| STDOUT_COLOR | Standard Output using colored terminal                                                       |
+--------------+----------------------------------------------------------------------------------------------+
| FILE         | Standard Output to file created within *./tmp/log_<epoch time seconds>.json*.                |
+--------------+----------------------------------------------------------------------------------------------+


.. code-block:: python

    class LoggingOutput(object):
        """TUNE Logging Output ENUM
        """
        STDOUT = "stdout"
        STDOUT_COLOR = "color"
        FILE = "file"


Logging JSON Format
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import logging
    from logging_mv_integrations import (LoggingFormat, get_logger, __version__)

    log = get_logger(
        logger_name=__name__,
        logger_version=__version__,
        logger_format=LoggingFormat.JSON,
        logger_level=logging.NOTE
    )

    log.info("logging: info", extra={'test': __name__})
    log.note("logging: note", extra={'test': __name__})
    log.debug("logging: debug", extra={'test': __name__})
    log.warning("logging: warning", extra={'test': __name__})
    log.error("logging: error", extra={'test': __name__})
    log.critical("logging: critical", extra={'test': __name__})
    log.exception("logging: exception", extra={'test': __name__})


Logging JSON Example Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ python3 examples/example_logging_json.py

    {"asctime": "2017-10-20 08:31:14 -0700", "levelname": "INFO", "name": "__main__",
    "version": "0.1.6", "message": "logging: info", "test": "__main__"}
    {"asctime": "2017-10-20 08:31:14 -0700", "levelname": "NOTE", "name": "__main__",
    "version": "0.1.6", "message": "logging: note", "test": "__main__"}
    {"asctime": "2017-10-20 08:31:14 -0700", "levelname": "WARNING", "name": "__main__",
    "version": "0.1.6", "message": "logging: warning", "test": "__main__"}
    {"asctime": "2017-10-20 08:31:14 -0700", "levelname": "ERROR", "name": "__main__",
    "version": "0.1.6", "message": "logging: error", "test": "__main__"}
    {"asctime": "2017-10-20 08:31:14 -0700", "levelname": "CRITICAL", "name": "__main__",
    "version": "0.1.6", "message": "logging: critical", "test": "__main__"}
    {"asctime": "2017-10-20 08:31:14 -0700", "levelname": "ERROR", "name": "__main__",
    "version": "0.1.6", "message": "logging: exception", "exc_info": "NoneType: None",
    "test": "__main__"}


Requirements
------------

``logging-mv-integrations`` module is built upon Python 3 and has dependencies upon
several Python modules available within `Python Package Index PyPI <https://pypi.python.org/pypi>`_.

.. code-block:: bash

    make install-requirements

or


.. code-block:: bash

    python3 -m pip uninstall --yes --no-input -r requirements.txt
    python3 -m pip install --upgrade -r requirements.txt


Dependencies
^^^^^^^^^^^^

- coloredlogs: https://pypi.python.org/pypi/coloredlogs
- pprintpp: https://pypi.python.org/pypi/pprintpp
- python-json-logger: https://pypi.python.org/pypi/python-json-logger
- Pygments: https://pypi.python.org/pypi/Pygments
- safe-cast: https://pypi.python.org/pypi/safe-cast
- wheel: https://pypi.python.org/pypi/wheel
