from django.urls import path
from . import views


app_name = 'payment'

urlpatterns = [
    path('process/', views.create_checkout_session, name='process'),
    path('completed/', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),
    # path('webhooks/', webhooks.stripe_webhook, name='stripe-webhooks')
]