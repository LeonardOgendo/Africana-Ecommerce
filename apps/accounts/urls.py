from django.urls import path
from . import views

app_name = 'apps.accounts'

urlpatterns = [
    path('logout', views.custom_logout, name='custom_logout')
]