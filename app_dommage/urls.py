from django.urls import path
from . import views

app_name = 'app_dommage'

urlpatterns = [
    path('', views.other_list, name='other_list'),
    path('<int:pk>/', views.other_detail, name='other_detail'),
    path('add/', views.other_add, name='other_add'),
    path('<int:pk>/edit/', views.other_edit, name='other_edit'),
    path('<int:pk>/delete/', views.other_delete, name='other_delete'),
]
