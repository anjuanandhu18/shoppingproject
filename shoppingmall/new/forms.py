from django import forms
from .models import registerTable
class registerform(forms.ModelForm):
    class Meta:
        model=registerTable
        fields='__all__'