from django.urls import path
from . import views

app_name = 'app_contract'

urlpatterns = [
    path('', views.contract_list, name='contract_list'),
    path('<int:pk>/edit', views.contract_edit, name='contract_edit'),
    path('add/', views.contract_add, name='contract_add'),
    path('add/vehicle/(?P<vehicle_id>\d+)/', views.contract_add, name='contract_add_with_vehicle'),
    path('add/person/(?P<person_id>\d+)/', views.contract_add, name='contract_add_with_person'),
    path('add/other/(?P<other_id>\d+)/', views.contract_add, name='contract_add_with_other'),
    path('<int:pk>/', views.contract_detail, name='contract_detail'),
    path('<int:pk>/delete/', views.contract_delete, name='contract_delete'),

    path('base_dashboard/', views.prime_company_dashboard_monthly, name='base_dashboard'),
    path('dashboard_prime_auto/', views.prime_vehicle_dashboard_monthly, name='dashboard_prime_auto'),
    path('dashboard_prime_person/', views.prime_person_dashboard_monthly, name='dashboard_prime_person'),
    path('dashboard_prime_dommage/', views.prime_dommage_dashboard_monthly, name='dashboard_prime_dommage'),
    path('dashboard_prime_company/', views.prime_company_dashboard, name='dashboard_prime_company'),

    path('dashboard_prime_type/', views.prime_type_dashboard, name='dashboard_prime_type'),


    path('dashboard_prime/', views.prime_dashboard, name='dashboard_prime'),
    path('expiring-contracts/', views.expiring_contracts_list, name='expiring_contract'),
    path('expired-contracts/', views.expired_contracts_list, name='expired_contracts'),
    path('sanlam_contracts/', views.sanlam_contracts, name='sanlam_contracts'),
    path('nsia_contracts/', views.nsia_contracts, name='nsia_contracts'),
    path('fidelia_contracts/', views.fidelia_contracts, name='fidelia_contracts'),

    path('export-contracts/', views.export_data, name='export_to_excel'),
    path('sanlam-export-contracts/', views.export_data_sanlam, name='sanlam_export_to_excel'),
    path('nsia-export-contracts/', views.export_data_nsia, name='nsia_export_to_excel'),
    path('fidelia-export-contracts/', views.export_data_fidelia, name='fidelia_export_to_excel'),
]
