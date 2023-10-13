from django.urls import path
from . import views

app_name = 'app_person'

urlpatterns = [
    path('', views.person_list, name='person_list'),
    path('<int:pk>/', views.person_detail, name='person_detail'),
    path('add/', views.person_add, name='person_add'),
    path('<int:pk>/edit/', views.person_edit, name='person_edit'),
    path('<int:pk>/delete/', views.person_delete, name='person_delete'),
]
