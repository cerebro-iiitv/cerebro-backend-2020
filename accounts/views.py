from django.shortcuts import render, redirect
# from accounts.forms import SignUpForm
from django.contrib.auth import login as auth_login
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


def index(request):
    return render(request, 'accounts/base.html')
