from django import forms
from .models import Ticket


class TicketsForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'id': 'title',
                    'placeholder': 'Enter title'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'description',
                    'rows': '3',
                    'placeholder': 'Enter description',
                    'style': 'max-width: 300px;',
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-select',
                    'id': 'selectField'
                }
            ),
        }
