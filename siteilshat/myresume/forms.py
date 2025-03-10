from django import forms
from myresume.models import Category, Photo


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
