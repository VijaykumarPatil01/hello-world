from django.urls import path
from django.urls import re_path

"""
Import the view
"""
from .views import myhome, new_project, monthly_billing

urlpatterns = [
    re_path(r'home$', myhome),
    re_path(r'new_project$', new_project, name="add_new_project"),
    re_path(r'monthly_billing$', monthly_billing, name="add_billing_details")
]