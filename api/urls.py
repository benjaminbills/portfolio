from django.urls import path
from .views import ProjectList

app_name = 'api'

urlpatterns = [
    path('', ProjectList.as_view(), name='list'),
]
