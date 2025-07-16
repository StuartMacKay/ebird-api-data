import json

from django.urls import reverse

import pytest

pytestmark = pytest.mark.django_db

redirects = [
    (reverse("index"), reverse("checklists")),
]

autocompletes = [
    reverse("counties"),
    reverse("states"),
    reverse("counties"),
    reverse("locations"),
    reverse("observers"),
    reverse("common-names"),
    reverse("scientific-names"),
]

pages = [
    (reverse("checklists"), None),
    (reverse("observations"), None),
    (reverse("species"), None),
]

@pytest.mark.parametrize("url,redirect", redirects)
def test_page_redirects(client, url, redirect):
    response = client.get(url, follow=False)
    assert response.url == redirect


@pytest.mark.parametrize("url", autocompletes)
def test_autocomplete_returns_data(client, url):
    response = client.get(url)
    json.loads(response.content)


@pytest.mark.parametrize("url,params", pages)
def test_page_is_displayed(client, url, params):
    response = client.get(url, query_params=params)
    assert response.status_code == 200
