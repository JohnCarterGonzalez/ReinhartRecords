from django.shortcuts import render

def dashboard(req):
    return render(req, "base.html")

def payments(req):
    return render(req, "payments.html")
