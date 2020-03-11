from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from accounts.serializers import AccountSerializers
from accounts.models import Account


def index(request):
    return render(request, 'accounts/base.html')


class AccountViewSets(ModelViewSet):
    serializer_class = AccountSerializers
    queryset = Account.objects.all()
