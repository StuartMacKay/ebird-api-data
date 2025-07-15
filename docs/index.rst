.. eBird API Data documentation master file, created by
   sphinx-quickstart on Tue Dec 24 07:15:15 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

eBird API Data
==============

The Cornell Laboratory of Ornithology in Ithaca, New York runs the eBird database
which collects observations of birds from all over the world. All the observations
are published on `eBird.org`_, and they also make them available via an `API`_.
This project contains a loader and models to take data from the API and load it into
a database. From there you can analyse the data with python, jupyter notebooks, or
build a web site.

To get started, you will need to `sign up`_ for an eBird account, if you don't
already have one and `register`_ to get an API key. Make sure you read and
understand the `Terms of use`_, and remember bandwidth and servers cost money,
so don't abuse the service. If you need large numbers of observations, then
sign up to receive the `eBird Basic Dataset`_.

.. _eBird.org: https://ebird.org
.. _API: https://documenter.getpostman.com/view/664302/S1ENwy59
.. _sign up: https://secure.birds.cornell.edu/identity/account/create
.. _register: https://ebird.org/data/download
.. _Terms of use: https://www.birds.cornell.edu/home/ebird-api-terms-of-use/
.. _eBird Basic Dataset: https://science.ebird.org/en/use-ebird-data/download-ebird-data-products

Table of Contents
-----------------
.. toctree::
   :maxdepth: 1

   install
   loaders
   database
   demo
   changelog
   license
