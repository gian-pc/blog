from django.urls import path
from .views import home, about, test, post, skill_detail, skill_search

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('test/', test, name='test'),
    path('post/', post, name='post'),
    path('skill_detail/<cod>', skill_detail, name='skill_detail'),
    path('skill_search/', skill_search, name='skill_search'),
]
