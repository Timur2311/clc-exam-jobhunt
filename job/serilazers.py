from rest_framework import serializers

from job.models import Category





        
class CategorySerializer(serializers.ModelSerializer):
    max_price = serializers.IntegerField()
    min_price = serializers.IntegerField()
    price = serializers.IntegerField()
    price_from = serializers.CharField()
    price_to = serializers.CharField()
    average_price = serializers.IntegerField()
    class Meta:
        model = Category
        fields = ('title', 'jobhunters_count',"max_price","min_price","average_price","price","price_from", "price_to")