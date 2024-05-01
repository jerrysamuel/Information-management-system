from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("starter/", views.starter, name="starter"),
    path("dashboard/", views.dashboard, name = "admin_dashboard"),
    path("customer_dashboard/", views.customer_dashboard, name = "customer_dashboard"),
    path("waiter_dashboard/", views.waiter_dashboard, name = "waiter_dashboard"),

   
]
