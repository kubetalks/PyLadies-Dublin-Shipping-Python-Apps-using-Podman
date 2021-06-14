from django.shortcuts import render


def index(request):
    """ The view that will render the home page """
    return render(request, 'mainapp/home.html', context={})
