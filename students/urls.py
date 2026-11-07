from django.urls import path
from . views import *

urlpatterns = [
    path("first-year/", first_year, name='first_year'),
    path("second-year/", second_year, name='second_year'),
    path("third-year/", third_year, name='third_year'),
    path("achievements/", achievements, name='achievements'),
    
]