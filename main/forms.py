from django import forms
from django.contrib.auth.forms import UserCreationForm


class profilecreater(forms.Form):
    Name=forms.CharField(max_length=100)
    Email=forms.EmailField()
    Password=forms.CharField(max_length=8,widget=forms.PasswordInput)
    ConfirmPassword=forms.CharField(max_length=8,widget=forms.PasswordInput)
    Profile_Pic=forms.ImageField()

class CreateBlogs(forms.Form):
    Photo=forms.ImageField()
    Headline=forms.CharField(max_length=200)
    Post=forms.CharField(widget=forms.Textarea)




