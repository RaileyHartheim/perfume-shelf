from django import forms
from .models import Comment, Perfume


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
            'base_notes',
            'have_it',
            'had_it',
            'want_it',
            'test_it'
        ]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
