from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class UserCreate(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age')


class UserChange(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'age')
