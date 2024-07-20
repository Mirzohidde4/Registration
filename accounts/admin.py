from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreate, UserChange
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreate
    form = UserChange
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'age', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)    