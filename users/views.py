from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, "users/index.html")


@login_required(login_url="/accounts/login/")
def profile(request):
    return render(request, "account/profile.html")

