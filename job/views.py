from django.shortcuts import render
from rest_framework.response import Response
from .serilazers import  CategorySerializer 
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User
from job.models import Company, Job, Category
from django.db import models


from django.db.models import Avg, Max, Min



# Create your views here.

class StatisticsList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        users = User.objects.all().count()
        companies = Company.objects.all().count()
        jobs =  Job.objects.all().count()
        
        
        return Response({"users": users,"jobs":jobs, "companies": companies})
    
from django.db.models.lookups import GreaterThan

class CategoryListView(generics.ListAPIView):
    max_price = Max('jobs__salary_from')
    min_price = Min("jobs__salary_from")
    average_price = Avg('jobs__salary_from')
    
    queryset = Category.objects.all().annotate(max_price = max_price , min_price = min_price, average_price = average_price )
    serializer_class = CategorySerializer
    
    def get_queryset(self):
      
        return self.queryset.annotate(
            price = models.Case(
                models.When(GreaterThan(models.F('min_price')*2, models.F('max_price')), then = (models.F('max_price')+models.F('min_price'))/2),
                default = 0,            
                output_field=models.IntegerField()
                
            ), 
            price_from = models.Case(
                models.When(GreaterThan(models.F('max_price'),models.F('min_price')*2), then = (models.F('min_price')+models.F('average_price'))/2),

                default = 0,            
                output_field=models.IntegerField()
                
            ), 
            price_to= models.Case(
                models.When(GreaterThan(models.F('max_price'),models.F('min_price')*2), then = (models.F('average_price')+models.F('max_price'))/2),

                default = 0,            
                output_field=models.IntegerField()
                
            ), 
            
        )
    
    
    
    
   
        
    