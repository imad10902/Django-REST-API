from django.urls import path
from . import views
# API to either add data or fetch data
urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
]