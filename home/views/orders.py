from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from senior_project.utils import login_required, get_full_url
from home.models import Order
from home.forms import OrderForm
import environ

env = environ.Env(
	# set casting, default value
	DEBUG=(bool, False)
)


@login_required
def order_list(request):
	orders = Order.get_users_orders(request.user)
	return render(request, 'home/orders/list.html', {'orders': orders})


@login_required
def order_confirmation(request, order_uuid):
	order = Order.objects.get(uuid=order_uuid)
	if (order.creator == request.user) or request.user.is_superuser:
		if request.method == 'POST':
			form = OrderForm(request.POST, instance=order)
			if form.is_valid():
				order = form.save(commit=False)
				order.updater = request.user
				order.save()
				url = get_full_url(order.get_read_url())
				send_mail(f"Updates to your order", f"Changes have been made to your order, view them here -> {url}", env('ADMIN_EMAIL'), [order.creator.email])
				return redirect(order.get_read_url())
		else:
			form = OrderForm(instance=order)

		context = {
			'order': order,
			'order_model': Order,
			'form': form,
		}
		return render(request, 'home/orders/confirmation.html', context)
	else:
		return HttpResponseForbidden()
