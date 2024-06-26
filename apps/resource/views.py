from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from users.decorators import waiter_required, admin_required, customer_required


@login_required(login_url='/users/signin/')
@admin_required
def check_resources(request):
    low_resources = Resource.objects.filter(quantity__lt=20).values('name')
    data = list(low_resources)
    return JsonResponse(data, safe=False)
@login_required(login_url='/users/signin/')
@admin_required
def HumanResource(request):
    Humanresources= Humanresource.objects.all()

    return render(request, './resources/human-resources.html', {"Humanresources":Humanresources})

def Menucat(request):
    menucategories = Menucategory.objects.all()

    return render(request, './resources/menucat.html', {'menucategories': menucategories})


def Menu(request, category):
    category_object = get_object_or_404(Menucategory, name=category)
    
    # Filter menu items based on the category object
    menuitems = Menuitem.objects.filter(category=category_object)

    return render(request, "./resources/menu.html", {"menuitems": menuitems})

@login_required(login_url='/users/signin/')
@admin_required
def Resources(request, category):
    category_object = get_object_or_404(Resourcecategory, name=category )
    resources= Resource.objects.filter(category=category_object)

    return render(request, "./resources/resources.html", {"resources":resources})

@login_required(login_url='/users/signin/')
@admin_required
def Accountnumbers(request):
    accountnums = Accountdetail.objects.all()

    return render(request, "./resources/account-details.html", {'accountnums':accountnums})

@login_required(login_url='/users/signin/')
@admin_required
def Resourcecat(request):
    resourcecat = Resourcecategory.objects.all()

    return render(request, "./resources/resourcecat.html", {'resourcecat':resourcecat})
@login_required(login_url='/users/signin/')
@admin_required
def Saleview(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            sale_instance = form.save(commit=False)
            # Get the associated Resource and subtract unit_sold
            resource = sale_instance.item
            resource.quantity -= sale_instance.unit_sold
            resource.save()
            # Save the Sales instance
            sale_instance.save()
            return redirect('sales')  # Redirect to the same page after successful submission
    else:
        form = SalesForm()
    
    sales = Sales.objects.all()
    return render(request, './resources/sales.html', {'form': form, 'sales': sales})
@login_required(login_url='/users/signin/')
@admin_required
def Foodsaleview(request):
    if request.method == 'POST':
        form = FoodsalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foodsales')  # Redirect to the same page after successful submission
    else:
        form = FoodsalesForm()
    
    foodsales = Foodsales.objects.all()
    return render(request, './resources/foodsales.html', {'form': form, 'foodsales': foodsales})

def menu_detail(request, category, menuitem_name):
    # Get the category object based on the provided category name
    category_object = get_object_or_404(Menucategory, name=category)
    
    # Get the menu item object based on the provided menuitem_name and category
    menuitem = get_object_or_404(Menuitem, category=category_object, name=menuitem_name)
    feedbacks = Feedback.objects.filter(item=menuitem)
    # Create a feedback form
    form = FeedbackForm()
    
    # Pass the category and menu item details to the template
    return render(request, './resources/menu-detail.html', {'category': category_object,'feedbacks':feedbacks, 'menuitem': menuitem, 'form': form})

def leave_feedback(request, category, menuitem_name):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Get the menu item object based on the provided menuitem_name and category
            menuitem = get_object_or_404(Menuitem, category__name=category, name=menuitem_name)
            # Save the feedback with the corresponding menu item
            feedback = form.save(commit=False)
            feedback.item = menuitem
            feedback.save()

            return redirect('menu_detail', category=category, menuitem_name=menuitem_name)
    else:
        form = FeedbackForm()
    return render(request, './resources/leave-feedback.html', {'form': form, 'category': category})
