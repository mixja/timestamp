git-stamp
=========

This package installs a utility called :code:`timestamp` that resets file system created/modified attributes to Git commit timestamps.

This is useful for creating repeatable builds where content does not change but due to file system created/modified attributes a change is detected in application packaging mechanisms.

This utility was specifically created to address this problem with ZIP packages created for AWS Lambda functions.

Usage
-----

.. code:: text
  
  $ timestamp -h
  usage: timestamp [-h] [-s SOURCE] [-p PATH]

  Fix timestamps to ensure repeatable builds

  optional arguments:
    -h, --help            show this help message and exit
    -s SOURCE, --source SOURCE
                          A single source file to use for the timestamp. If not
                          specified each files last commit timestamp is used.
    -p PATH, --path PATH  Target path that should have timestamps applied.
                          Defaults to directory root.

By default, if you don't specify any arguments :code:`timestamp` will perform the equivalent of :code:`git ls-files` and apply the current commit timestamp to matching files in the repository.

You can also apply a specific Git timestamp from a given source file using the :code:`-s` or :code:`--source` flag and apply that timestamp to all files within a given path specified by the :code:`-p` or :code:`--path` flag.

The following example applies the Git timestamp of the :code:`Pipfile.lock` file to all files in :code:`build/dependencies/python`.  This specific example is useful for building same AWS Lambda Layer content for dependencies that have not changed between builds.

.. code:: bash
  
  $ timestamp -s Pipfile.lock -p build/dependencies/python
  build/dependencies/python/dateutil/_version.py - setting timestamp 1566516602
  build/dependencies/python/dateutil/_common.py - setting timestamp 1566516602
  build/dependencies/python/dateutil/__init__.py - setting timestamp 1566516602
  build/dependencies/python/dateutil/tzwin.py - setting timestamp 1566516602
  ...
  ...

Installation
------------

    pip install git-stamp

Requirements
------------

- Python 3.x
- dulwich_

.. _dulwich: https://github.com/dulwich/dulwich

Authors
-------

- `Justin Menga`_

.. _Justin Menga: https://github.com/mixja
