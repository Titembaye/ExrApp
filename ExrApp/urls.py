
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("clients/", include("app_client.urls")),
    path("vehicles/", include("app_vehicle.urls")),
    path("contracts/", include("app_contract.urls")),
    path("persons/", include("app_person.urls")),
    path("others/", include("app_dommage.urls")),
    path("app_setting/", include("app_setting.urls"))
]
