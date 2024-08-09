# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('home/', views.homepage,name="home_page"),
#     path('about', views.about,name="about_page"),
#     path('add_home/', views.add_home, name="add_home_page"),
#     path('detail_page/<slug:slug>/', views.detail_page, name='detail_page'),
#     path('signin_page', views.signin_page, name="signin_page"),
#     path('', views.login_page, name="login_page"),
#     path('logout_page', views.logout_page, name="logout_page"),
#     path('cart/<slug:slug>/', views.cart, name='cart'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home_rental.api.api_views import (
    AddRentalHomeViewSet,
    UserInformationViewSet,
)
from . import views

app_name = 'home_rental'

# Set up the router for the API ViewSets
router = DefaultRouter()
router.register(r'rental-homes', AddRentalHomeViewSet, basename='rentalhome')
router.register(r'user-information', UserInformationViewSet, basename='userinfo')

# Combine the existing urlpatterns with the router URLs
urlpatterns = [
    path('home/', views.homepage, name="home_page"),
    path('about/', views.about, name="about_page"),
    path('add_home/', views.add_home, name="add_home_page"),
    path('detail_page/<slug:slug>/', views.detail_page, name='detail_page'),
    path('signin_page/', views.signin_page, name="signin_page"),
    path('', views.login_page, name="login_page"),
    path('logout_page/', views.logout_page, name="logout_page"),
    path('cart/<slug:slug>/', views.cart, name='cart'),

    # Include the router URLs for the API
    path('api/', include(router.urls)),
]
