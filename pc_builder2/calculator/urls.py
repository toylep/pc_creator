from django.urls import path

from calculator.views import TechCityTestParser

urlpatterns = [
    path("parse/techcity", TechCityTestParser.as_view()),
]