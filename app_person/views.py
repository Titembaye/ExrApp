from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from datetime import datetime
from app_person.forms import PersonForm
from app_person.models import Person


def person_list(request):
    persons_list = Person.objects.all()

    # Recherche par nom
    search_query = request.GET.get('search_query')
    if search_query:
        persons_list = persons_list.filter(full_name__icontains=search_query)

    # Tri
    sort_by = request.GET.get('sort_by', '-id')
    persons_list = persons_list.order_by(sort_by)

    paginator = Paginator(persons_list, 5)
    page = request.GET.get('page')
    persons = paginator.get_page(page)
    persons_count = Person.objects.all().count()

    return render(request, 'persons/persons_list.html',
                  {'persons': persons, 'sort_by': sort_by, 'search_query': search_query, 'navbar': 'person',
                   'persons_count': persons_count})


def person_add(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            existing_person = Person.objects.filter(full_name=form.cleaned_data['full_name'],
                                                    birthday=form.cleaned_data['birthday'],
                                                    gender=form.cleaned_data['gender'])
            if not existing_person:
                new_person = form.save()
                return redirect('app_contract:contract_add_with_person', person_id=new_person.id)
            else:
                error_message = 'Ce contrat existe deja'
                return render(request, 'errors/error_message.html',
                              {'error_message': error_message,
                               'return_url': reverse('app_person:person_list')})
    else:
        form = PersonForm()

    return render(request, 'persons/person_form.html', {'form': form})


def person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('app_person:person_list')
    else:

        form = PersonForm(instance=person)

    return render(request, 'persons/person_form.html', {'form': form, 'person': person})


def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('app_person:person_list')  # Redirigez vers la liste des personnes après la suppression
    return render(request, 'persons/person_confirm_delete.html', {'person': person})


def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    client = person.contract_set.first().client
    contract = person.contract_set.first()
    return render(request, 'persons/person_detail.html', {'person': person,'client': client,'contract': contract})
