from django.shortcuts import render

# from myapp_person.models import Person
from .models import Person
from .forms import PersonForm

def person_list(request):
    persons = Person.objects.all()
    context = {'persons': persons}
    return render(request, 'myapp_person/person_list.html', context)


from django.shortcuts import render, redirect
def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'myapp_person/person_create.html', {'form': form})

from django.shortcuts import get_object_or_404
def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'myapp_person/person_delete.html', {'person': person})