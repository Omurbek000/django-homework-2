from django.urls import path
from .import views 

 
urlpatterns = [
    path('home', views.event_list),
    path('add/', views.add_event),
    path('edit/', views.edit_event),
]