from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path


urlpatterns = [
    # Change the path to the Django Admin to something non-standard.
    path("admin/", admin.site.urls),  # type: ignore
] + staticfiles_urlpatterns()
