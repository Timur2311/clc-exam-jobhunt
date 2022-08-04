from django.db import models

from django.contrib.auth.models import User



class Company(models.Model):
    title = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="companies")



class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    jobhunters_count = models.IntegerField(default=0)
    
    
class Job(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="jobs")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary_from = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="narx")
    
    
    
    
    
