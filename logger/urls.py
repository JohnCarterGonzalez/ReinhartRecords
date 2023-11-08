from django.urls import path

from . import views

app_name = "logger"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("payments/", views.payments, name="payments" ),
]
