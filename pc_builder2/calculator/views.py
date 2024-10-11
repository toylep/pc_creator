from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from calculator.tech_city.GPU_parser import TechCityGPUParser
from calculator.tech_city.CPU_parser import TechCityCPUParser
# Create your views here.

class TechCityGPUParserView(GenericAPIView):
    
    def get(self,request):
        parcer = TechCityGPUParser().parse()
        #parcer.extraction()
        return Response({"message": "suck_dick"})
    

class TechCityCPUParserView(GenericAPIView):
    
    def get(self,request):
        parcer = TechCityCPUParser().parse()
        #parcer.extraction()
        return Response({"message": "suck_cock"})