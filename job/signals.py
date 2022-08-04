from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from job.models import Category, Job

@receiver(post_save, sender=Job)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        category = Category.objects.get(id = instance.category.id)
        category.jobhunters_count+=1
        category.save()

