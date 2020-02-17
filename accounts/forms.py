from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account


class SignUpForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
        
