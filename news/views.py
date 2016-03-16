from django.shortcuts import render
from .forms import SignUpForm
from django.core.mail import send_mail
from django.conf import settings
from .models import SignUp

# Create your views here.
def signup(request):
	title = "Sign-Up Now"
	form = SignUpForm(request.POST or None)

	context = {
		"title": title,
		"form": form

	}

	if form.is_valid():
		instance = form.save(commit=False)
		name = form.cleaned_data.get("name")
		surname = form.cleaned_data.get("surname")

		if not name:
			name = "New Name"
			instance.name = name

		instance.save()

		context = { "title": "Thank you"}

	return (render(request, "basic.html", context))