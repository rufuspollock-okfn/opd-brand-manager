from django import forms
from .models import BrandType


class BrandProposalForm(forms.Form):
    brand_nm = forms.CharField(max_length=255, label='Brand name')
    brand_type = forms.ModelChoiceField(queryset=BrandType.objects.all())
    owner_nm = forms.CharField(
        max_length=255, label='Owner name', required=False)
    brand_link = forms.URLField(
        max_length=255, label='Brand website', required=False)
    brand_logo = forms.ImageField(
        label='Brand logo', required=False)
    comments = forms.CharField(
    max_length=255, label='Comments', required=False)
    sender = forms.EmailField(max_length=255, label='Your mail')
