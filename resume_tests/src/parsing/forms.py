from django import forms
from resume_tests.src.parsing.models import City,Language
# from parsing.models import City, Language


class FindForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name='slug', required=True,
                                  widget=forms.Select(attrs={'class': 'form-control'}),
                                  label='Город')
    language = forms.ModelChoiceField(queryset=Language.objects.all(), to_field_name='slug', required=True,
                                      widget=forms.Select(attrs={'class': 'form-control'}),
                                      label='Специальность')




