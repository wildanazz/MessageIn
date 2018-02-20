from django import forms
from .models import Send

# Create your forms here

class SendForm(forms.Form):
    
    sender_attrs = {
        'type': 'text',
        'class': 'sender-form',
        'placeholder':'From..'
    }
    
    receiver_attrs = {
        'type': 'text',
        'class': 'receiver-form',
        'placeholder':'To..'
    }
    
    text_attrs = {
        'type': 'text',
        'cols': 50,
        'rows': 4,
        'class': 'text-form',
        'placeholder':'Write your message here..'
    }
    
    sender = forms.CharField(label='', required=True, max_length=27, widget=forms.TextInput(attrs=sender_attrs))
    receiver = forms.CharField(label='', required=True, max_length=27, widget=forms.TextInput(attrs=receiver_attrs))
    text = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=text_attrs))

    
