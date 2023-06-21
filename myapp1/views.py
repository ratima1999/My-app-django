from django.shortcuts import render
from .forms import MyForm
from django.http import HttpResponse 
def hello(request): 
 return HttpResponse("Hello, worl a view function that takes a request object as its argument and returns an HTTP response.d!")


def my_function(request):
 # Your function logic here 
 return HttpResponse("Hello, World!")
def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Form is valid, do something with the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Save data to database, send email, etc.
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})
 