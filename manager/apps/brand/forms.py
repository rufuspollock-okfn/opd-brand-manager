from django import forms


class BrandProposalForm(forms.Form):
    brand_nm = forms.CharField(max_length=255, label='Brand name')
    brand_type = forms.ChoiceField(choices=(('test', '1'), ('test2', '2')))
    owner_nm = forms.CharField(
        max_length=255, label='Owner name', required=False)
    brand_link = forms.URLField(
        max_length=255, label='Brand website', required=False)
    #Add logo
    comments = forms.CharField(
    max_length=255, label='Comments', required=False)
    sender = forms.EmailField(max_length=255, label='Your mail')
