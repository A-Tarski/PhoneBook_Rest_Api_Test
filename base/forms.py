from django import forms
from . import models

class AddRecordForm(forms.ModelForm):
    class Meta:
        model = models.Record
        fields = ('name', 'number',)

class GetRecordForm(forms.ModelForm):
    class Meta:
        model = models.Record
        fields = ('name', )
