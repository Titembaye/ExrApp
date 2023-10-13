from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from app_contract.models import Contract
from .forms import ClientForm
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Client


def client_list(request):
    # Récupérer les valeurs des paramètres GET q et sort_by
    q = request.GET.get('q')
    sort_by = request.GET.get('sort_by')

    # Liste de tous les clients, triée par ordre d'enregistrement par défaut
    clients_list = Client.objects.all().order_by('-id')

    # Filtres
    if q:
        clients_list = clients_list.filter(full_name__icontains=q)

    # Tri par nom si demandé
    if sort_by == 'full_name':
        clients_list = clients_list.order_by('full_name')

    paginator = Paginator(clients_list, 5)
    page = request.GET.get('page')
    clients = paginator.get_page(page)

    return render(request, 'clients/client_list.html',
                  {'clients': clients, 'q': q, 'sort_by': sort_by, 'navbar': 'client'})


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    contracts = Contract.objects.filter(client=client)  # Récupérez les contrats liés à ce client
    return render(request, 'clients/client_detail.html', {'client': client, 'contracts': contracts})


def client_add(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            existing_client = Client.objects.filter(full_name=form.cleaned_data['full_name']).exists()
            if not existing_client:
                form.save()
                return redirect('app_client:client_list')
            else:
                error_message = "Le client existe déjà"
                return render(request, 'errors/error_message.html',
                              {'error_message': error_message,
                               'return_url': reverse('app_client:client_list')})
    else:
        form = ClientForm()
    return render(request, 'clients/client_form.html', {'form': form})


def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('app_client:client_detail', pk=pk)
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/client_form.html', {'form': form, 'app_client': client})


def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('app_client:client_list')
    return render(request, 'clients/client_confirm_delete.html', {'app_client': client})


def client_find(request):
    clients = Client.objects.all()

    query = request.GET.get('q')
    if query:
        clients = clients.filter(full_name__icontains=query)

    return render(request, 'app_client/client_list.html', {'app_client': clients})
