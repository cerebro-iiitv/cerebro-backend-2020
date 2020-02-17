from django.shortcuts import render, redirect
from accounts.forms import SignUpForm
from django.contrib.auth import login as auth_login
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from accounts.models import Account
from accounts.serializers import AccountSerializers


def index(request):
    return render(request, 'accounts/base.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')

    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})


class AccountViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AccountSerializers
    queryset = Account.objects.all()
