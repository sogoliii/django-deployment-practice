from django import forms
from django.contrib.auth.models import User
from formPage.models import userSignup,userProfileInfo

class userForm(forms.ModelForm):
    """password section for User"""
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username' , 'email' , 'password')

class userProfileInfoForm(forms.ModelForm):
    portfolio = forms.URLField(required = False)
    picture = forms.ImageField(required = False)
    class Meta:
        model = userProfileInfo
        fields = ('portfolio' , 'picture')


class userSignupForm(forms.ModelForm):
    """signup model form"""
    class Meta:
        model = userSignup
        fields = '__all__'
