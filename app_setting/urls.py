from django.urls import path
from . import views

app_name = 'app_setting'

urlpatterns = [
    # -------------------------------COMPANY------------------------------------#
    path('company/', views.company_list, name='company_list'),
    path('company/add/', views.company_add, name='company_add'),
    path('company/edit/<int:pk>/', views.company_edit, name='company_edit'),
    path('company/delete/<int:pk>/', views.company_delete, name='company_delete'),

    # -------------------------------GUARANTTEE------------------------------------#
    path('guaranttee/', views.guaranttee_list, name='guaranttee_list'),
    path('guaranttee/add/', views.guaranttee_add, name='guaranttee_add'),
    path('guaranttee/edit/<int:pk>/', views.guaranttee_edit, name='guaranttee_edit'),
    path('guaranttee/delete/<int:pk>/', views.guaranttee_delete, name='guaranttee_delete'),

    # ----------------------------------TYPE----------------------------------------#
    path('type/', views.type_list, name='type_list'),
    path('type/add/', views.type_add, name='type_add'),
    path('type/edit/<int:pk>/', views.type_edit, name='type_edit'),
    path('type/delete/<int:pk>/', views.type_delete, name='type_delete'),
]
