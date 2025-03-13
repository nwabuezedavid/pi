from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render,redirect
from app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User  # To associate with Django's built-in User model
from django.db.models import Q
# Create your views here.
def wallet2(request):
    if request.method == "POST":
        wallet = request.POST.get("wallet")
        item = Item(wallet=wallet)
        item.save()
        messages.success(request, "pi transferred successfully , note : that the transaction can talk up to 24 hours")
        return redirect("wallet2")
    con ={
    }
    return render (request, "wallet.html",con)



def home(request):
    con ={
    }
    return render (request, "home.html",con)
def move(request):
    con ={
    }
    return render (request, "move.html",con)
def mov1(request):
    con ={
    }
    return render (request, "moves.html",con)