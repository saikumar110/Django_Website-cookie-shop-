from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import Contact, Orders, posts


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        date = request.POST.get("date")
        time = request.POST.get("time")
        orders = Orders(name=name, email=email, subject=subject, message=message, date=date,time=time)
        orders.save()

    return render(request, "index.html")


def about(request):
    return render(request, "single.html")


def Menu(request):
    return render(request, "menu.html")


def Contactsss(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        contact = Contact(name=name, email=email, subject=subject, message=message, date=datetime.now())
        contact.save()
    return render(request, "contact.html")


def Archieve(request):
    post= posts.objects.all()
    return render(request, "archive.html",{"post":post})
