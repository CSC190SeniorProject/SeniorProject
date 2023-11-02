from django.core.mail import send_mail
from django.shortcuts import redirect, render
from home.forms import ContactForm
from home.models import Product, Configurations, Order
import environ

env = environ.Env(
	# set casting, default value
	DEBUG=(bool, False)
)


def about(request):
	return render(request, 'home/about.html')


def contact(request):
	config = Configurations.get_first_configuration()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			#try:
			send_mail(subject, f" \nFrom: {env('ADMIN_EMAIL')}\n\n" + message, env('FROM_EMAIL'), [env('ADMIN_EMAIL')])  # todo: change to_email
			#messages.success(request, f'Email sent successfully.')
			return redirect('home:home')
			#except:
				#return HttpResponseServerError('There was a problem sending the email. Please contact the email listed on the contact page directly.')
	return render(request, 'home/contact.html', {"config": config})


def home(request):
	products = Product.get_active_products()
	is_superuser = request.user.is_superuser
	return render(request, 'home/home.html', {'products': products, 'is_superuser': is_superuser})


def order(request):
	return render(request, 'home/order.html')


def product(request):
	return render(request, 'home/product.html')


def report(request):
	months, order_counts = Order.get_order_counts_by_month_for_year(2023)

	status_counts = Order.get_order_status_counts()
	order_status = list(status_counts.values_list('status', flat=True))
	order_total = list(status_counts.values_list('total', flat=True))
	return render(request, 'home/report.html', {'months': months, 'order_counts': order_counts, 'order_status': order_status, 'order_total': order_total})


def cart_demo(request):
	return render(request, 'home/addtocart.html')
