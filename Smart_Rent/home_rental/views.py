from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import AddRentalHome
from .forms import AddRentalHomeForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
import markdown

from django.db.models import Q


def homepage(request):
    q = request.GET.get('q', '')
    sort_order = request.GET.get('sort', '')

    if q:
        multiple_q = Q(Q(City__icontains=q) | Q(Street2__icontains=q))
        homedata = AddRentalHome.objects.filter(multiple_q)
    else:
        homedata = AddRentalHome.objects.all()

    if sort_order == 'asc':
        homedata = homedata.order_by('Rent')
    elif sort_order == 'desc':
        homedata = homedata.order_by('-Rent')
    return render(request, "home.html", {
        'homedata': homedata
    })


def about(request):
    return render(request, "about.html")


from django.shortcuts import render, redirect
from .forms import AddRentalHomeForm
import google.generativeai as genai

genai.configure(api_key='AIzaSyASefeu3w7RpGKJZGRzEcsyjFJ9wv2rv7A')
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_description(data):
    prompt = (
        f"Generate a detailed description for a rental home with the following details:\n"
        f"Street1: {data['Street1']}\n"
        f"Street2: {data.get('Street2', '')}\n"
        f"City: {data['City']}\n"
        f"State: {data['State']}\n"
        f"Pincode: {data['Pincode']}\n"
        f"Feature1: {data.get('Feature1', '')}\n"
        f"Feature2: {data.get('Feature2', '')}\n"
        f"Visiting Day: {data['Visiting_day']}\n"
        f"Rent: {data['Rent']}\n"
        f"Number Of People Allowed: {data['Number_Of_People_Allowed']}\n"
        f"Generate a detailed and engaging description based on the above information."
    )

    response = model.generate_content(prompt)
    # Adjust the following line based on actual response structure
    description = getattr(response, 'text', None)
    html = markdown.markdown(description)
    plain_text = html
    from bs4 import BeautifulSoup
    plain_text = BeautifulSoup(html, "html.parser").text
    print("Generated description (plain text):", plain_text)
    return plain_text


def add_home(request):
    if request.method == 'POST':
        form = AddRentalHomeForm(request.POST, request.FILES)
        if form.is_valid():
            # Generate description using Gemini AI
            data = form.cleaned_data
            description = generate_description(data)

            # Create a new instance of the form with the generated description
            home_instance = form.save(commit=False)
            home_instance.Description = description
            home_instance.save()

            return redirect('home_page')
        else:
            print("Form errors:", form.errors)
    else:
        form = AddRentalHomeForm()

    return render(request, 'add_home.html', {'form': form})


def detail_page(request, slug):
    identified_post = get_object_or_404(AddRentalHome, slug=slug)
    cart_url = reverse('home_rental:cart', args=[identified_post.slug])
    return render(request, "detail_page.html", {
        "home_detail": identified_post,
        "cart_url": cart_url
    })


def signin_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_rental:login_page')
    else:
        form = SignupForm()
    return render(request, 'signin.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_rental:home_page')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('login')


def cart(request, slug):
    identified_post = get_object_or_404(AddRentalHome, slug=slug)
    return render(request, "cart.html", {
        "home_detail": identified_post,
    })


