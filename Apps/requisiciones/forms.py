from django import forms
from .models import Requisicion
class RequisicionForm(forms.ModelForm):
    class Meta:
        model = Requisicion
        fields = ['proyecto','cantidad','justificacion']
