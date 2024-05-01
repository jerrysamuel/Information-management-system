from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from decimal import Decimal 
from users.decorators import waiter_required, admin_required, customer_required
from apps.resource.models import *
from django.db.models import Sum
import json
from django.db.models import Count
from django.db.models.functions import TruncDate

from .models import *


def index(request):

  context = {
    'segment': 'dashboard',
  }
  return render(request, "dashboard/index.html", context)

def starter(request):

  context = {}
  return render(request, "pages/starter.html", context)

@login_required(login_url='/users/signin/')
@admin_required
def dashboard(request):
    total_menu = Menuitem.objects.count()
    human_resource_count = Humanresource.objects.count()
    account_details  = Accountdetail.objects.count()
    total_salaries = Humanresource.objects.aggregate(total_salary=models.Sum('salary'))['total_salary'] or 0
    net_worth_resources = Resource.objects.aggregate(net_worth=models.Sum('worth'))['net_worth'] or 0
    category_worth = (
        Resource.objects.values('category__name')
        .annotate(total_worth=Sum('worth'))
        .order_by('category__name')
    )

    # Calculate the total worth of all resources
    total_worth_all = Resource.objects.aggregate(total_worth_all=Sum('worth'))['total_worth_all']

    # Prepare the data for plotting
    categories = json.dumps([entry["category__name"] for entry in category_worth])
    worths = [entry['total_worth'] for entry in category_worth]
    worth_percentages_decimal = [round((worth / total_worth_all) * 100, 2) for worth in worths]
    worth_data_float = [float(value) for value in worth_percentages_decimal]
    worth_percentages = json.dumps(worth_data_float)
    male_count = Humanresource.objects.filter(gender='male').count()
    female_count = Humanresource.objects.filter(gender='female').count()

    
    # Calculate the percentages
    total_staff = male_count + female_count
    male_percentage = round((male_count / total_staff) * 100, 2)
    female_percentage = round((female_count / total_staff) * 100, 2)

    # Prepare the data for plotting
    genders = ['Male', 'Female']
    percentages = [male_percentage, female_percentage]
    staff_counts = Humanresource.objects.values('humancategory').annotate(count=Count('id'))

    # Prepare the data for the pie chart
    labels = json.dumps([entry['humancategory'] for entry in staff_counts])
    counts = json.dumps([entry['count'] for entry in staff_counts])

    total_unit_sold_worth = Foodsales.objects.aggregate(total_unit_sold_worth=Sum('unit_sold'))['total_unit_sold_worth'] or 0
    data = (
        Foodsales.objects.values('date')
        .annotate(total_units_sold=Sum('unit_sold'))
        .order_by('date')
    )

    # Prepare the data for plotting
    dates = json.dumps([entry['date'].strftime('%Y-%m-%d') for entry in data])
    units_sold = json.dumps([entry['total_units_sold'] for entry in data])

    context = {
       'total_menu':total_menu,
        'human_resource_count': human_resource_count,
        'account_details': account_details,
        'total_salaries': total_salaries,
        'net_worth_resources': net_worth_resources,
        "categories": categories,
        "worth_percentages": worth_percentages,
        'genders': json.dumps(genders),
        'percentages': json.dumps(percentages),
        'labels':labels,
        'counts':counts,
        'total_unit_sold_worth':total_unit_sold_worth,
        'dates': dates,
        'units_sold': units_sold,
    }
    
    return render(request, "dashboard/dashboard.html", context)
  
@login_required(login_url='/users/signin/')
@waiter_required
def waiter_dashboard(request):
    return render(request, 'dashboard/waiterdash/dashboard.html')

@login_required(login_url='/users/signin/')
@customer_required
def customer_dashboard(request):
    
    return render(request, 'dashboard/waiterdash/dashboard.html')




