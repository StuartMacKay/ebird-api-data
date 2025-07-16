import json

from django import forms
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

from dal import autocomplete
from ebird.api.data.models import Country, County, Location, Observer, Species, State


class FilterForm(forms.Form):
    form_id = None
    form_title = None
    filters = {}

    def get_filters(self):
        return {
            expr: self.cleaned_data[field]
            for field, expr in self.filters.items()
            if self.cleaned_data.get(field)
        }

    def get_ordering(self):
        return []


class LocationFilter(FilterForm):
    form_id = "location"
    form_title = _("By Location")

    country = forms.ModelChoiceField(
        label=_("Country"),
        required=False,
        queryset=Country.objects.all(),
        widget=autocomplete.Select2(
            url="countries",
            attrs={"placeholder": _("Select one or more countries")},
        ),
    )

    state = forms.ModelMultipleChoiceField(
        label=_("State"),
        required=False,
        queryset=State.objects.all(),
        widget=autocomplete.Select2Multiple(
            url="states",
            forward=["country"],
            attrs={
                "data-placeholder": _("Select one or more states"),
            },
        ),
    )

    county = forms.ModelMultipleChoiceField(
        label=_("County"),
        required=False,
        queryset=County.objects.all(),
        widget=autocomplete.Select2Multiple(
            url="counties",
            forward=["state", "country"],
            attrs={
                "data-placeholder": _("Select one or more counties"),
            },
        ),
    )

    location = forms.ModelMultipleChoiceField(
        label=_("Location"),
        required=False,
        queryset=Location.objects.all(),
        widget=autocomplete.Select2Multiple(
            url="locations",
            forward=["county", "state", "country"],
            attrs={
                "data-placeholder": _("Select one or more locations"),
            },
        ),
    )

    hotspot = forms.ChoiceField(
        label=_("Hotspots only"),
        choices=(
            ("", _("No")),
            ("True", _("Yes")),
        ),
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    filters = {
        "country": "country",
        "state": "state__in",
        "county": "county__in",
        "location": "location__in",
        "hotspot": "location__hotspot",
    }


class ObserverFilter(FilterForm):
    form_id = "observer"
    form_title = _("By Observer")

    observer = forms.ModelChoiceField(
        label=_("Observer"),
        required=False,
        queryset=Observer.objects.all(),
        widget=autocomplete.Select2(
            url="observers",
            attrs={"class": "form-select", "data-theme": "bootstrap-5"},
        ),
    )

    filters = {
        "observer": "observer",
    }


class SpeciesFilter(FilterForm):
    form_id = "species"
    form_title = _("By Species")

    common_name = forms.ModelChoiceField(
        label=_("Common name"),
        required=False,
        queryset=Species.objects.all(),
        widget=autocomplete.Select2(
            url="common-names",
            attrs={"class": "form-select", "data-theme": "bootstrap-5"},
        ),
    )

    scientific_name = forms.ModelChoiceField(
        label=_("Scientific name"),
        required=False,
        queryset=Species.objects.all(),
        widget=autocomplete.Select2(
            url="scientific-names",
            attrs={"class": "form-select", "data-theme": "bootstrap-5"},
        ),
    )

    filters = {
        "common_name": "species",
        "scientific_name": "species",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_bound:
            self.fields["common_name"].choices = self.get_common_name_choice()

    def get_common_name_choice(self):
        choices = []
        if code := self.data.get("common_name"):
            choice = (
                Species.objects.filter(species_code=code)
                .values_list("species_code", "common_name")
                .first()
            )
            if choice:
                choices = [(choice[0], json.loads(choice[1])[get_language()])]
        return choices


class DateRangeFilter(FilterForm):
    form_id = "date-range"
    form_title = _("By Date")

    DATES_SWAPPED = _("This date is later than the until date.")

    start = forms.DateField(
        label=_("From"),
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
    )
    finish = forms.DateField(
        label=_("Until"),
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
    )

    filters = {
        "start": "date__gte",
        "finish": "date__lte",
    }

    def clean(self):
        start = self.cleaned_data.get("start")
        finish = self.cleaned_data.get("finish")

        if start and finish and start > finish:
            self.add_error("start", self.DATES_SWAPPED)


class CategoryFilter(FilterForm):
    form_id = "category"
    form_title = _("By Category")

    category = forms.ChoiceField(
        label=_("Category"),
        choices=Species.Category.choices,
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    filters = {
        "category": "species__category",
    }
