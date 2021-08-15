from django.shortcuts import render


def login_view(request, *args, **kwargs):
    return render(request, "login.html")


def send_view(request, *args, **kwargs):
    return render(request, "send_cert.html")


def verify_view(request, *args, **kwargs):
    return render(request, "verify.html")
