from email.policy import default
from django import forms
from .models import b2p_project_name
from .models import b2p_site

class project_lists_form(forms.Form):

    project_1 = forms.CharField(max_length=255)
    site=forms.ModelChoiceField(queryset=b2p_site.objects.all())
    project_2 = forms.CharField(max_length=255)
    is_active=forms.BooleanField()

    class Meta:
        model=b2p_project_name

