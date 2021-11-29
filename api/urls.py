from django.urls import path
from .views import SendMail, projectList

app_name = 'api'

urlpatterns = [
    path('', projectList, name='list'),
    path('email', SendMail, name='send-email')
]
