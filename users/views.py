from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Profile
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse


def register(request):
    print('зашли сюда')
    form = NewUserForm()
    if request.method == "POST":
        print('постик')
        form = NewUserForm(request.POST)
        print(form)
        if form.is_valid():
            print("Форма нормис")
            user = form.save()
            login(request, user)
            response = redirect("myapp:index")
            print(user.username)
            response.set_cookie('name', user.username)
            return response
        else:
            print("Всё плохо")
            context = {"form": form}
            print(context)
            print(context["form"])
            return render(request, "users/register.html", context)
    context = {"form": form}
    return render(request, "users/register.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        contact_number = request.POST.get("number")
        image = request.FILES["upload"]
        user = request.user
        profile = Profile(user=user, contact_number=contact_number, image=image)
        profile.save()

    return render(request, "users/profile.html")


def seller_profile(request, id):
    seller = User.objects.get(id=id)
    print(seller)
    print(seller.contact_number)
    context = {
        'seller': seller
    }

    return render(request, 'users/sellerprofile.html', context)