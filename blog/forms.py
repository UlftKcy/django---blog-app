from .models import User,Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class ProfileForm(forms.ModelForm):
    class Meta:        
        model = Profile
        fields = ('username', 'email', 'image', 'bio')
