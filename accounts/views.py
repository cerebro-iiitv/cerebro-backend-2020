from django.shortcuts import render, redirect
from accounts.forms import SignUpForm
from django.contrib.auth import login as auth_login
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
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


class AccountListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    serializer_class = AccountSerializers

    def get_queryset(self):
        return Account.objects.all()


class AccountCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    serializer_class = AccountSerializers

    def get_queryset(self):
        return Account.objects.all()


class AccountRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    serializer_class = AccountSerializers

    def get_queryset(self):
        return Account.objects.all()


class OptimusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            'message': 'Autobots, Roll Out',
        }
        return Response(content)
