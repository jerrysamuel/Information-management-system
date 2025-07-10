from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from users.decorators import waiter_required, admin_required, customer_required
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator



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
def Resources(request):
    resources = Resource.objects.all()

    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)  # include request.FILES if file uploads involved
        if form.is_valid():
            form.save()
            messages.success(request, "Resource added successfully.")
            return redirect('resources')  # use the URL name
        else:
            messages.error(request, "There was an error adding the resource.")
    else:
        form = ResourceForm()

    return render(request, "resources/resources.html", {
        "resources": resources,
        "form": form
    })

# def Resources(request, category):
#     category_object = get_object_or_404(Resourcecategory, name=category)
#     resources = Resource.objects.filter(category=category_object)

#     if request.method == 'POST':
#         form = ResourceForm(request.POST)
#         if form.is_valid():
#             new_resource = form.save(commit=False)
#             new_resource.category = category_object  # override category field from URL
#             new_resource.save()
#             return redirect('resources', category=category)  # or your URL name
#     else:
#         form = ResourceForm()

#     return render(request, "resources/resources.html", {
#         "resources": resources,
#         "form": form,
#         "category": category_object
#     })


@login_required(login_url='/users/signin/')
@admin_required
def Accountnumbers(request):
    accountnums = Accountdetail.objects.all()

    return render(request, "./resources/account-details.html", {'accountnums':accountnums})

@login_required(login_url='/users/signin/')
@admin_required
def Resourcecat(request):
    resourcecat = Resourcecategory.objects.all()

    if request.method == 'POST':
        form = ResourcecatForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Resource category added successfully.")
                return redirect('resource_category')
            except Exception as e:
                print(f"Error saving form: {e}")
                messages.error(request, "Something went wrong while saving.")
        else:
            print("Form errors:", form.errors)
            messages.error(request, "Invalid form input.")
    else:
        form = ResourcecatForm()

    return render(request, "resources/resourcecat.html", {
        "resourcecat": resourcecat,
        "form": form
    })



   
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


def sales_report(request):
    filter_by = request.GET.get('filter', 'monthly')  # 'monthly' or 'weekly'
    today = timezone.now()

    if filter_by == 'weekly':
        start_date = today - timedelta(days=7)
    else:  # default to monthly
        start_date = today.replace(day=1)

    sales_list = Sales.objects.filter(date__gte=start_date).order_by('-date')

    # Pagination
    paginator = Paginator(sales_list, 10)  # Show 10 sales per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'filter_by': filter_by,
    }
    return render(request, 'resources/sales_report.html', context)
