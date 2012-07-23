from django import forms
from models import Signup

class OccurrenceSignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        exclude = ('occurrence',)

class EmailAttendantsForm(forms.Form):
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)