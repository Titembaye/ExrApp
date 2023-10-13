from django.urls import path, include
from .models import Vehicle
from . import views

app_name = 'app_vehicle'

urlpatterns = [
    path('', views.vehicle_list, name='vehicle_list'),
    path('<int:pk>/edit/', views.vehicle_edit, name='vehicle_edit'),
    path('add/', views.vehicle_add, name='vehicle_add'),
    path('<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('<int:pk>/delete/', views.vehicle_delete, name='vehicle_delete'),
]
