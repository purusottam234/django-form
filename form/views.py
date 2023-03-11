from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from .forms import MyForm, ContactForm

# this view don't save any instance of form in the database
from .models import Contact


def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            return HttpResponse("Thanks for submitting your form")
    else:
        form = MyForm()
    return render(request, 'myform_template.html', {'form': form})


# to save the form instance we need to create a model and save the form instance on it

def form_view(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contact = Contact.objects.create(name=name,email=email, message=message)
            return redirect("form-view")
    else:
        form = MyForm()

    return render(request, 'myform_template.html', {'form': form})


def model_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # no need to cleaned_data in model form
            form.save()
            return redirect("form-view")
    else:
        form = ContactForm()

    return render(request, 'myform_template.html', {'form': form})


