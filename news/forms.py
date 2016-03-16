from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['name', 'surname', 'email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		return email

	def clean_name(self):
		name = self.cleaned_data.get('name')
		return name

	def clean_surname(self):
		surname = self.cleaned_data.get('surname')
		return surname