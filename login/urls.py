from django.urls import include, path
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls, name='admin'),
]