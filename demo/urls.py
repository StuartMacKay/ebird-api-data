from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.utils.translation import gettext_lazy as _
from django.views.generic import RedirectView

from .lists import (
    CommonNameList,
    CountryList,
    CountyList,
    LocationList,
    ObserverList,
    ScientificNameList,
    StateList,
)

from .views import ChecklistsView, ObservationsView, SpeciesView

urlpatterns = [
    # Change the path to the Django Admin to something non-standard.
    path("", RedirectView.as_view(pattern_name="checklists"), name="index"),
    path("admin/", admin.site.urls),  # type: ignore
    path(_("checklists/"), ChecklistsView.as_view(), name="checklists"),
    path(_("observations/"), ObservationsView.as_view(), name="observations"),
    path(_("species/"),SpeciesView.as_view(), name="species"),
    path("lists/countries/", CountryList.as_view(), name="countries"),
    path("lists/states/", StateList.as_view(), name="states"),
    path("lists/counties/", CountyList.as_view(), name="counties"),
    path("lists/locations/", LocationList.as_view(), name="locations"),
    path("lists/observers/", ObserverList.as_view(), name="observers"),
    path("lists/common-name", CommonNameList.as_view(), name="common-names"),
    path("lists/scientific-name", ScientificNameList.as_view(), name="scientific-names"),
] + staticfiles_urlpatterns()
