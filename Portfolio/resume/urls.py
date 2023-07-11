from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('portfolio/', portfolio, name="portfolio"),
    path('about_me/', about_me, name="about_me"),
    path('', home , name="home"),
    

]
