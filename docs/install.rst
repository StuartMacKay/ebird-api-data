============
Installation
============

Requirements
============
* `Django <https://www.djangoproject.com/>`_ >= 4.2 LTS
* `Python <https://www.python.org/>`_ >= 3.10

The app is tested on Python 3.10+, and officially supports Django 4.2, 5.0,
and 5.1. However, it almost certainly works with earlier versions of both python
and Django.

Install
=======
You can use either `pip`_ or `uv`_ to download the `package`_ from PyPI and
install it into a virtualenv:

.. code-block:: console

    pip install ebird-api-data

or:

.. code-block:: console

    uv add ebird-api-data

Update ``INSTALLED_APPS`` in your Django setting:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        ebird.api.data
    ]

Finally, run the migrations to create the tables:

.. code-block:: python

    python manage.py migrate

.. _pip: https://pip.pypa.io/en/stable/
.. _uv: https://docs.astral.sh/uv/
.. _package: https://pypi.org/project/ebird-api-data/
