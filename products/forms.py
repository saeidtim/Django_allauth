from django.forms.models import ModelForm
from django.core.exceptions import ValidationError
from .models import *


class PorductFormComment(ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('body')
        if data.startswith('salam'):
            raise ValidationError('ba slam shooro kardi')
        else:
            return cleaned_data
    class Meta:
        model = ProductComment
        fields = ('body', 'stars', )


