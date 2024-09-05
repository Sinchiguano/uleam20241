from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    age=forms.IntegerField(help_text='A valid age is required')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     # Add custom validation logic here, e.g., check for domain-specific restrictions
    #     return email