
from django.shortcuts import render
from user.forms import UserSingIn

def signin(request):
    context = {
        "signin_form": UserSingIn()
    }
    return render(request, "sign_in.html", context)