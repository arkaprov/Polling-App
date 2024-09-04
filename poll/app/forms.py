from django import forms
from .models import Question,Choice
class voteFrom(forms.ModelForm):
    class Meta:
        model=Choice
        fields="__all__"