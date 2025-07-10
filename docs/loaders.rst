============
Loading Data
============
The `eBird API 2.0`_ provides access to the checklists submitted to eBird,
world-wide.

To get started, you will need to `sign up`_ for an eBird account, if you don't
already have one, and `register`_ to get an API key. Make sure you read and
understand the `Terms of use`_, and remember bandwidth and servers cost money,
so don't abuse the service.

The first step is to add the API key to your Django settings:

.. code-block:: python

    EBIRD_API_KEY = <your api key>

Next, you need to add a map from the language code(s) you want to use with
Django to the locale code(s) used for the eBird Taxonomy. This is used when
adding Species, so the common and family names can be displayed in the currently
activated language. For example:

.. code-block:: python

    EBIRD_LOCALES = '{"es": "es"}'

You can easily select multiple languages. The names are stored in the common_name
and family_common_name fields as JSON dicts, and the project has multi-value
form fields and widgets so you can easily edit the values, if necessary.

You can find a complete list of locales supported in the eBird Taxonomy using the
eBird API Requests function get_taxonomy_locales():

.. code-block:: python

    from django.conf import settings
    from ebird.api.requests import get_taxonomy_locales

    locales = get_taxonomy_locales(settings.EBIRD_API_KEY)

Now, it is time to load some checklists:

.. code-block:: console

    python manage.py add_checklists --days 7 US-NY-109

This will load checklists added in the past week for Tompkins county Ney York, USA,
where the Cornell Lab of Ornithology is located. You can use any country code (US),
state code (US-NY), county code (US-NY-109), or hotspot identifier (L97555). The
management command also allows you to pass multiple codes in a single call.

The management commands calls get_visits() from the ebird.api, which lists the
visits made on each day. The eBird API limits the number of results to 200. To
workaround this, if the limit is reached then the visits to each sub-region are
fetched. That way you can still download all the checklists submitted. Since
this command only downloads checklists that don't already exist in the database
you can run it frequently and be sure you are getting all the submissions.

You automate running the command using a scheduler such as cron. If you use the
absolute paths to python and the command, then you don't need to deal with
activating the virtual environment, for example:

.. code-block:: console

    # Every 4 hours, load all new checklists, for New York state, submitted for the past week
    0 */4 * * * /home/me/my-project/.venv/bin/python /home/me/my-project/manage.py add_checklists --days 7 US-NY

That way you can be pretty sure you're getting all the observations for a region.

IMPORTANT: The loader currently only loads new checklists. It does not update
existing ones. The reason is that only about 1% of submitted checklists are updated,
and because of the limitations of the eBird API, you can only find out if a checklist
has changed by downloading it. So, to pick up all the changes you have to repeatedly
download all the checklists for a given period in case something changed. That is
more or less practical for small windows of time, for example, the past three days.
However, you are still downloading hundreds or maybe thousands of checklist to pick
up the handful which were edited. For larger windows it becomes really expensive in
terms of load on the eBird servers. They also have to pay for the network connections
and bandwidth too. You can't download everything, all the time, in case something
changed. You should really treat the API as a news service, and accept that there
will be gaps in the data. For accuracy and completeness, sign up to get access to
the eBird Basic Dataset, which is published on the 15th of each month.

Using cron, you can schedule running the add_checklists management command, to pick up
most of the submissions:

.. code-block:: console

    # Every hour, load new checklists submitted today
    0 * * * * /home/me/my-project/.venv/bin/python /home/me/my-project/manage.py add_checklists --days 1 US-NY
    # Every 4 hours, load new checklists submitted today and yesterday
    0 */4 * * * /home/me/my-project/.venv/bin/python /home/me/my-project/manage.py add_checklists --days 2 US-NY
    # Every day at midnight, load new checklists submitted in the past week
    0 0 * * * /home/me/my-project/.venv/bin/python /home/me/my-project/manage.py add_checklists --days 7 US-NY


This schedule, or something similar, should ensure that the database contains the
majority of the checklists that eBird has.

These examples showed how to do it with Linux. For Windows you will need to write
scripts, and use the Scheduler to run them at a given time.

.. _eBird API 2.0: https://documenter.getpostman.com/view/664302/S1ENwy59
.. _sign up: https://secure.birds.cornell.edu/identity/account/create
.. _register: https://ebird.org/data/download
.. _Terms of use: https://www.birds.cornell.edu/home/ebird-api-terms-of-use/
