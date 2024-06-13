from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class regform(UserCreationForm):
    class Meta:
        model = User
        fields =["username","first_name","last_name","email","password1","password2"]
        
class loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class orderform(forms.Form):
    address=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"address","row":5}))