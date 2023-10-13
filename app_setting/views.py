from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from app_contract.models import Contract
from .forms import CompanyForm, GuarantteeForm, TypeForm
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Company, Guaranttee, Type

#-----------------------------------------------------------------------#
###########----------- GUARANTIE -------------###########################
#-----------------------------------------------------------------------#


def company_list(request):
    # Récupérer les valeurs des paramètres GET q et sort_by
    q = request.GET.get('q')
    sort_by = request.GET.get('sort_by')

    # Liste de tous les clients, triée par ordre d'enregistrement par défaut
    companies_list = Company.objects.all().order_by('-id')

    # Filtres
    if q:
        companies_list = companies_list.filter(name__icontains=q)

    # Tri par nom si demandé
    if sort_by == 'name':
        companies_list = companies_list.order_by('name')

    paginator = Paginator(companies_list, 5)
    page = request.GET.get('page')
    companies = paginator.get_page(page)

    return render(request, 'settings/company_list.html',
                  {'companies': companies, 'q': q, 'sort_by': sort_by, 'navbar': 'compagnie'})


def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'settings/company_detail.html', {'company': company})


def company_add(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            existing_company = Company.objects.filter(name=form.cleaned_data['name']).exists()
            if not existing_company:
                form.save()
                return redirect('app_setting:company_list')
            else:
                error_message = "Cette compagnie existe déjà"
                return render(request, 'errors/error_message.html',
                              {'error_message': error_message,
                               'return_url': reverse('app_setting:company_list')})
    else:
        form = CompanyForm()
    return render(request, 'settings/company_form.html', {'form': form})


def company_edit(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('app_setting:company_list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'settings/company_form.html', {'form': form, 'app_setting': company})


def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('app_setting:company_list')
    return render(request, 'settings/company_confirm_delete.html', {'app_setting': company})


#-----------------------------------------------------------------------#
###########----------- GUARANTIE -------------###########################
#-----------------------------------------------------------------------#


def guaranttee_list(request):
    # Récupérer les valeurs des paramètres GET q et sort_by
    q = request.GET.get('q')
    sort_by = request.GET.get('sort_by')

    # Liste de tous les clients, triée par ordre d'enregistrement par défaut
    guaranties_list = Guaranttee.objects.all().order_by('-id')

    # Filtres
    if q:
        guaranties_list = guaranties_list.filter(name__icontains=q)

    # Tri par nom si demandé
    if sort_by == 'libelle':
        guaranties_list = guaranties_list.order_by('libelle')

    paginator = Paginator(guaranties_list, 5)
    page = request.GET.get('page')
    guaranties = paginator.get_page(page)

    return render(request, 'settings/guaranttee_list.html',
                  {'guaranties': guaranties, 'q': q, 'sort_by': sort_by, 'navbar': 'garantie'})


def guaranttee_add(request):
    if request.method == 'POST':
        form = GuarantteeForm(request.POST)
        if form.is_valid():
            existing_guaranttee = Guaranttee.objects.filter(libelle=form.cleaned_data['libelle']).exists()
            if not existing_guaranttee:
                form.save()
                return redirect('app_setting:guaranttee_list')
            else:
                error_message = "Cette garantie existe déjà"
                return render(request, 'errors/error_message.html',
                              {'error_message': error_message,
                               'return_url': reverse('app_setting:guaranttee_list')})
    else:
        form = GuarantteeForm()
    return render(request, 'settings/guaranttee_form.html', {'form': form})


def guaranttee_edit(request, pk):
    guaranttee = get_object_or_404(Guaranttee, pk=pk)
    if request.method == 'POST':
        form = GuarantteeForm(request.POST, instance=guaranttee)
        if form.is_valid():
            form.save()
            return redirect('app_setting:guaranttee_list')
    else:
        form = GuarantteeForm(instance=guaranttee)
    return render(request, 'settings/guaranttee_form.html', {'form': form, 'app_setting': guaranttee})


def guaranttee_delete(request, pk):
    guaranttee = get_object_or_404(Guaranttee, pk=pk)
    if request.method == 'POST':
        guaranttee.delete()
        return redirect('app_setting:guaranttee_list')
    return render(request, 'settings/guaranttee_confirm_delete.html', {'app_setting': guaranttee})


#-----------------------------------------------------------------------#
###########----------- TYPE -------------###########################
#-----------------------------------------------------------------------#


def type_list(request):
    # Récupérer les valeurs des paramètres GET q et sort_by
    q = request.GET.get('q')
    sort_by = request.GET.get('sort_by')

    # Liste de tous les clients, triée par ordre d'enregistrement par défaut
    types_list = Type.objects.all().order_by('-id')

    # Filtres
    if q:
        types_list = types_list.filter(name__icontains=q)

    # Tri par nom si demandé
    if sort_by == 'libelle':
        types_list = types_list.order_by('libelle')

    paginator = Paginator(types_list, 5)
    page = request.GET.get('page')
    types = paginator.get_page(page)

    return render(request, 'settings/type_list.html',
                  {'types': types, 'q': q, 'sort_by': sort_by, 'navbar': 'type'})


def type_detail(request, pk):
    type_insurance = get_object_or_404(Type, pk=pk)
    return render(request, 'settings/type_detail.html', {'type_insurance': type_insurance})


def type_add(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            existing_type = Type.objects.filter(libelle=form.cleaned_data['libelle']).exists()
            if not existing_type:
                form.save()
                return redirect('app_setting:type_list')
            else:
                error_message = "Ce Type d'assurance existe déjà"
                return render(request, 'errors/error_message.html',
                              {'error_message': error_message,
                               'return_url': reverse('app_setting:type_list')})
    else:
        form = TypeForm()
    return render(request, 'settings/type_form.html', {'form': form})


def type_edit(request, pk):
    type_insurance = get_object_or_404(Type, pk=pk)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type_insurance)
        if form.is_valid():
            form.save()
            return redirect('app_setting:type_list')
    else:
        form = TypeForm(instance=type_insurance)
    return render(request, 'settings/type_form.html', {'form': form, 'app_setting': type_insurance})


def type_delete(request, pk):
    type_insurance = get_object_or_404(Type, pk=pk)
    if request.method == 'POST':
        type_insurance.delete()
        return redirect('app_setting:type_list')
    return render(request, 'settings/type_confirm_delete.html', {'app_setting': type_insurance})
