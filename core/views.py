from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:5]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {'items': items, 'categories': categories})


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                form.save()

            return redirect('/login')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})
