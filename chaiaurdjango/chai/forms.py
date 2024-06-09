from django import forms

from .models import chaiverity

#write a form name 

class chaiverityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(queryset=chaiverity.objects.all(), label='select chai varity')

    