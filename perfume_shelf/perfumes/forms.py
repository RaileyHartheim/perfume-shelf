from django import forms
from .models import Perfume


class PerfumeForm(forms.ModelForm):

    class Meta:
        model = Perfume
        fields = [
            'perfume_name',
            'brand',
            'gender',
            'perfume_group',
            'season',
            'usage',
            'image_url',
            'top_notes',
            'middle_notes',
            'base_notes'
        ]
