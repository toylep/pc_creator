from django.urls import path

from calculator.views import TechCityGPUParserView, TechCityCPUParserView

urlpatterns = [
    path("parse/techcity/gpu", TechCityGPUParserView.as_view()),
    path("parse/techcity/cpu", TechCityCPUParserView.as_view()),
]
