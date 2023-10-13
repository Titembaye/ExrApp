from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from app_contract.models import Contract
from .forms import OtherForm
from .models import Other


def other_list(request):
    others_list = Other.objects.all()

    # Recherche par title
    search_query = request.GET.get('search_query')
    if search_query:
        others_list = others_list.filter(title__icontains=search_query)

    # Tri
    sort_by = request.GET.get('sort_by', '-id')
    others_list = others_list.order_by(sort_by)
    others_count = Other.objects.all().count
    paginator = Paginator(others_list, 5)
    page = request.GET.get('page')
    others = paginator.get_page(page)

    return render(request, 'others/other_list.html',
                  {'others': others, 'sort_by': sort_by, 'search_query': search_query, 'others_count': others_count})


def other_add(request):
    if request.method == 'POST':
        form = OtherForm(request.POST)
        if form.is_valid():
            # verifier si l'objet existe deja
            existing_other = Other.objects.filter(
                description=form.cleaned_data['description'],
                comment=form.cleaned_data['comment'],
            ).exists()

            if not existing_other:
                new_other = form.save()
                return redirect('app_contract:contract_add_with_other', other_id=new_other.id)
            else:
                error_message = "L'objet existe déjà."
                return render(request, 'errors/error_message.html',
                              {'error_message': error_message,
                               'return_url': reverse('app_dommage:other_list')})
    else:
        form = OtherForm()

    return render(request, 'others/other_form.html', {'form': form})


def other_edit(request, pk):
    other = get_object_or_404(Other, pk=pk)

    if request.method == 'POST':
        form = OtherForm(request.POST, instance=other)
        if form.is_valid():
            form.save()
            return redirect('app_dommage:other_list')
    else:
        form = OtherForm(instance=other)

    return render(request, 'others/other_form.html', {'form': form, 'other': other})


def other_delete(request, pk):
    other = get_object_or_404(Other, pk=pk)

    if request.method == 'POST':
        other.delete()
        return redirect('app_dommage:other_list')

    return render(request, 'others/other_confirm_delete.html', {'other': other})


def other_detail(request, pk):
    other = get_object_or_404(Other, pk=pk)
    contract = other.contract_set.first()
    client = contract.client

    return render(request, 'others/other_detail.html', {'other': other, 'contract': contract, 'client': client})
