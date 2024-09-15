from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from calculator.tech_city.parser import TechCityParser
# Create your views here.

class TechCityTestParser(GenericAPIView):
    
    def get(self,request):
        parcer = TechCityParser()
        #parcer.extraction()
        return Response({"test": parcer.extraction()})