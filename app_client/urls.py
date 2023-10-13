from django.urls import path
from . import views

app_name = 'app_client'

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('<int:pk>/', views.client_detail, name='client_detail'),
    path('add/', views.client_add, name='client_add'),
    path('<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('<int:pk>/delete/', views.client_delete, name='client_delete'),

]
