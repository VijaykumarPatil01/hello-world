from django.shortcuts import render
import os
from .models import project, monthlyBilling

from .forms import projectForm, billingForm
# Create your views here.

def myhome(request):
    appProjs = project.objects.approvedProjs()
    """projlist = "\n"
    for proj in appProjs:
        projlist = projlist + "Group = " + proj['group'] + " Name = " + proj['name'] + " NWA Code = " + proj['nwa_code']
        projlist += "\t \t"
    """
    waitprojs = project.objects.notApprovedProjs()
    return render(request, "sowtracker/home.html", {'approvedprojs': appProjs, 'waitingprojs': waitprojs})

def new_project(request):
    if request.method == "POST":
        myform = projectForm(data=request.POST)
        if myform.is_valid():
            myform.save()
            appProjs = project.objects.approvedProjs()
            return render(request, "sowtracker/home.html", {'projdetails': appProjs})
    else:
        myform = projectForm()
    return render(request, "sowtracker/new_project_form.html", {'form': myform})

def monthly_billing(request):
    if request.method == "POST":
        billform = billingForm(request.POST)
        if billform.is_valid():
            billform.save()
            appProjs = project.objects.approvedProjs()
            return render(request, "sowtracker/home.html", {'projdetails': appProjs})
    else:
        billform = billingForm()
    return render(request, "sowtracker/new_billing_form.html", {'form': billform})