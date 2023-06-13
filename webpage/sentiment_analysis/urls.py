from django.urls import path
from .views import *



urlpatterns = [
    path('',HomePageView,name='home'),
    path('abouts/',AboutsPageView, name='abouts')
]
