from django.urls import include, path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
]