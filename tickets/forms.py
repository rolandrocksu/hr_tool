from django import forms
from .models import Tickets
from .choices import TicketstatusChoices


class TicketsForm(forms.ModelForm):

    class Meta:
        model = Tickets
        fields = ['title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(),
            'description': forms.TextInput(),
            'status': forms.Select()
        }

    status = forms.ChoiceField(choices=TicketstatusChoices.choices)
