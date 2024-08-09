# from django.shortcuts import render
#
# # Create your views here.
# from decimal import Decimal
# import stripe
# from django.conf import settings
# from django.http import HttpResponse
# from django.shortcuts import render, redirect, reverse, \
#     get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
#
# # from home_rental.models import Property
#
# # Create your views here.
# stripe.api_key = settings.STRIPE_SECRET_KEY
# stripe.api_version = settings.STRIPE_API_VERSION
#
#
# def payment_process(request):
#     # order_id = request.session.get('order_id', None)
#     # order = get_object_or_404(Property, id=order_id)
#     #
#     # if request.method == 'POST':
#     #     success_url = request.build_absolute_uri(reverse('payment:completed'))
#     #     cancel_url = request.build_absolute_uri(reverse('payment:canceled'))
#     #     session_data = {
#     #         'mode': 'payment',
#     #         'client_reference_id': order.id,
#     #         'success_url': success_url,
#     #         'cancel_url': cancel_url,
#     #         'line_items': []
#     #     }
#     #
#     #     for item in order.items.all():
#     #         session_data['line_items'].append({
#     #             'price_data': {
#     #                 'unit_amount': int(item.price * Decimal('100')),
#     #                 'currency': 'usd',
#     #                 'product_data': {
#     #                     'name': item.product.name,
#     #                 },
#     #             },
#     #             'quantity': item.quantity,
#     #         })
#     #     if order.coupon:
#     #         stripe_coupon = stripe.Coupon.create(name=order.coupon.code,
#     #                                              percent_off=order.discount,
#     #                                              duration='once')
#     #         session_data['discounts'] = [{
#     #             'coupon': stripe_coupon.id
#     #         }]
#     #
#     #     session = stripe.checkout.Session.create(**session_data)
#     #     return redirect(session.url, code=303)
#     # else:
#     return render(request, 'process.html')
#
#
def payment_completed(request):
    return render(request, 'completed.html')


def payment_canceled(request):
    return render(request, 'cancelled.html')


#
# @csrf_exempt
# def stripe_webhook(request):
#     payload = request.body
#     sig_header = request.META['HTTP_STRIPE_SIGNATURE']
#     event = None
#
#     try:
#         event = stripe.Webhook.construct_event(payload, sig_header,
#                                                settings.STRIPE_WEBHOOK_SECRET)
#     except ValueError as e:
#         # Invalid payload
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError as e:
#         # Invalid signature
#         return HttpResponse(status=400)
#
#     if event.type == 'checkout.session.completed':
#         session = event.data.object
#         if session.mode == 'payment' and session.payment_status == 'paid':
#             try:
#                 order = Order.objects.get(id=session.client_reference_id)
#             except Order.DoesNotExist:
#                 return HttpResponse(status=404)
#             # mark order as paid
#             order.paid = True
#             order.stripe_id = session.payment_intent
#             order.save()
#             payment_completed.delay(order.id)
#     return HttpResponse(status=200)

#
# # views.py
from django.conf import settings
from django.shortcuts import render, redirect
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(request):
    if request.method == 'POST':
        YOUR_DOMAIN = 'http://localhost:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'sle',
                        'product_data': {
                            'name': 'Home Rental',
                        },
                        'unit_amount': 2000,  # Amount in cents
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url, code=303)

    return render(request, 'process.html')
