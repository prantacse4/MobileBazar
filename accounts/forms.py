from django.core import validators
from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.core import validators



class ProfileForm(forms.ModelForm):
    name = forms.CharField(required=False)
    location = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    image = forms.ImageField( required=False)
    class Meta:
        model = Profile
        fields = ['name', 'location','phone', 'image']





class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        for instance in User.objects.all():
            if instance.email == email:
                raise forms.ValidationError("Email Should Be Unique.")
     
        return email