from django.urls import path
from .views import *

urlpatterns = [
    path('', demo_firstpage, name = 'demo_firstpage'),
]