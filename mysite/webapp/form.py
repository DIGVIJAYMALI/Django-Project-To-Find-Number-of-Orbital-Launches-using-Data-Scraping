from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='launch_year', max_length=100)