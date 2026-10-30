from django.urls import path
from . views import *

urlpatterns = [
    path("", index, name='index'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
    path("achievements/", achievements, name='achievements'),
    path("sign-up/", sign_up, name='sign_up'),
    path("sign-in/", sign_in, name='sign_in'),
]