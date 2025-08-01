from django import forms
from .models import UserInteraction

class InteractionForm(forms.ModelForm):
    class Meta:
        model = UserInteraction
        fields = ['user_name', 'message']