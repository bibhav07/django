
from django.urls import path
from . import views

app_name = 'travel'
urlpatterns = [
    path('', views.travello,name='travello'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('destinations/',views.destinations,name='destinations'),
    path('elements/',views.elements,name='elements'),
    path('news/',views.news,name='news'),

]
