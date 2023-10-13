from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse

from .forms import VehicleForm
from .models import Vehicle

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from app_contract.models import Contract  # Importez le modèle Contract


def vehicle_list(request):
    vehicles = Vehicle.objects.order_by('-id')

    # Recherche par immatriculation
    registration_query = request.GET.get('registration_query')
    if registration_query:
        vehicles = vehicles.filter(registration__icontains=registration_query)

    paginator = Paginator(vehicles, 5)
    page = request.GET.get('page')
    vehicles = paginator.get_page(page)
    vehicles_count = Vehicle.objects.all().count()
    return render(request, 'vehicles/vehicle_list.html', {
        'vehicles': vehicles,
        'registration_query': registration_query,
        'navbar': 'vehicle',
        'vehicles_count': vehicles_count
    })


def vehicle_add(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            existing_vehicle = Vehicle.objects.filter(registration=form.cleaned_data['registration'],
                                                      brand=form.cleaned_data['brand'])
            if not existing_vehicle:
                new_vehicle = form.save()
                return redirect('app_contract:contract_add_with_vehicle', vehicle_id=new_vehicle.id)
            else:
                error_message = "Un véhicule avec cette immatriculation existe deja"
                return render(request, 'errors/error_message.html',
                              {'error_message': error_message,
                               'return_url': reverse('app_vehicle:vehicle_list')})
        else:
            return render(request, 'vehicles/vehicle_form.html', {'form': form})
    else:
        form = VehicleForm()
        return render(request, 'vehicles/vehicle_form.html', {'form': form})


def vehicle_edit(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)

    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('app_vehicle:vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)

    return render(request, 'vehicles/vehicle_form.html', {'form': form, 'vehicle': vehicle})


def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    client = vehicle.contract_set.first().client
    contract = vehicle.contract_set.first()
    return render(request, 'vehicles/vehicle_detail.html', {'client': client, 'vehicle': vehicle, 'contract': contract})


def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('app_vehicle:vehicle_list')
    return render(request, 'vehicles/vehicle_confirm_delete.html', {'vehicle': vehicle})
