from django import forms

class NameForm(forms.Form):
    author = forms.CharField(label='Author', max_length=100)
    title = forms.CharField(label = 'Title', max_length=100)
    entry = forms.CharField(label = 'Entry', max_length = 10000)
