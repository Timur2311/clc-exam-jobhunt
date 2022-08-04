

from django.urls import path

from .views import StatisticsList, CategoryListView
urlpatterns = [
    path('statistic/', StatisticsList.as_view()),
    path('jobs/', CategoryListView.as_view())
]
