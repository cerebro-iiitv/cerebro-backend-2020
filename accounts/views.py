from django.shortcuts import render


def index(request):
    return render(request, 'accounts/base.html')


def signup(request):
    return render(request, 'accounts/signup.html')