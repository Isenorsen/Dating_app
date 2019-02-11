from django.forms import ModelForm
from .models import UserAccounts

class AccountInfo(ModelForm):
    class Meta:
        model = UserAccounts
        fields = ['user_account_id', 'name', 'age', 'city', 'about', 'avatar']
