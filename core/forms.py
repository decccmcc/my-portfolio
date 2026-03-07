from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your name',
            'class': 'form-input',
            'required': True,
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'placeholder': 'your@email.com',
            'class': 'form-input',
            'required': True,
        })
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={
            'placeholder': 'Your message...',
            'class': 'form-input form-textarea',
            'rows': 6,
            'required': True,
        })
    )
