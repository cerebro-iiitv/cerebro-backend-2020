from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.accountListView.as_view(), name='account_api'),  # list view of users
    path('create/', views.accountCreateView.as_view(), name='account-create'),  # create user view
    path('view/<int:pk>/', views.accountRUDView.as_view(), name='account-RUD'),  # RetrieveUpdateDestroyAPIView
    path('signup/', views.signup, name='signup'),
    path('optimus/', views.OptimusView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
