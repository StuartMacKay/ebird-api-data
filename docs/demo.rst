====
Demo
====

If you check out the code from the repository there is a fully functioning
Django site. It only contains the admin pages, but that is sufficient for
you to browse the data.

.. code-block:: console

    git clone git@github.com:StuartMacKay/ebird-api-data.git
    cd ebird-api-data

Create the virtual environment:

.. code-block:: console

    uv venv

Activate it:

.. code-block:: console

    source venv/bin/activate

Install the requirements:

.. code-block:: console

    uv sync

Create a copy of the .env.example file and add your API key:

.. code-block:: python

    cp .env.example .env

For example:

.. code-block:: python

    EBIRD_API_KEY=<my api key>

Run the database migrations:

.. code-block:: console

    python manage.py migrate

Create a user:

.. code-block:: console

    python manage.py createsuperuser

Now, download data from the API:

.. code-block:: console

    python manage.py add_checklists --days 2 US-NY-109

This loads all the checklists, submitted in the past two days by birders in
Tompkins County, New York, where the Cornell Lab is based. You can use any
location code used by eBird, whether it's for a country, state/region, or
county. Remember, read the terms of use.

Run the demo:

.. code-block:: console

    python manage.py runserver

Now log into the `Django Admin <http:localhost:8000/admin>` to browse the tables.
