from django.urls import path

from .apps import HomeConfig
from .views import HomePageView

app_name = HomeConfig.name

urlpatterns = [
    path("", view=HomePageView.as_view(), name="home"),
]