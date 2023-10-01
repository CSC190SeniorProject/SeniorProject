from pyexpat.errors import messages
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseServerError
from django.shortcuts import redirect, render
from ..forms import ContactForm
import environ
import os

env = environ.Env(
	# set casting, default value
	DEBUG=(bool, False)
)


def about(request):
	return render(request, 'home/about.html')


def blog(request):
	return render(request, 'home/blog.html')


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			#try:
			send_mail(subject, message, env('FROM_EMAIL'), [env('ADMIN_EMAIL')])  # todo change this to the submitted email
			#messages.success(request, f'Email sent successfully.')
			return redirect('home:home')
			#except:
				#return HttpResponseServerError('There was a problem sending the email. Please contact the email listed on the contact page directly.')
	return render(request, 'home/contact.html')


def home(request):
	return render(request, 'home/home.html')


def order(request):
	return render(request, 'home/order.html')


def product(request):
	return render(request, 'home/product.html')


def report(request):
	return render(request, 'home/report.html')
