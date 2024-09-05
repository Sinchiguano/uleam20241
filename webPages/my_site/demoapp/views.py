from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. This is the index view of demoapp.")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():  
            # Process the form data here
            name = form.cleaned_data['name']
            #basic validation by default, that is in django
            email = form.cleaned_data['email']  
            message = form.cleaned_data['message']
            # Do something with  the data, e.g., send an email
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})
