from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.AccountListView.as_view(), name='account_api'),  # list view of users
    path('create/', views.AccountCreateView.as_view(), name='account-create'),  # create user view
    path('view/<int:pk>/', views.AccountRUDView.as_view(), name='account-RUD'),  # RetrieveUpdateDestroyAPIView
    path('signup/', views.signup, name='signup'),
    path('optimus/', views.OptimusView.as_view()),
    path('api-token/', obtain_auth_token, name='api-token'),  # obtaining token
]

urlpatterns = format_suffix_patterns(urlpatterns)
