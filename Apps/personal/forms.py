from django import forms
from .models import Personal
class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['nombre','dpi','telefono','proyecto','estado','observaciones']
