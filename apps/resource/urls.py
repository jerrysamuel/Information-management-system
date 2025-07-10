from django.urls import path
from . import views

urlpatterns = [
    path('human-resources/', views.HumanResource, name='human_resources'),
    path('menu/<str:category>/', views.Menu, name='menu'),
    path('menu/<str:category>/<str:menuitem_name>/', views.menu_detail, name='menu_detail'),
    path('menu/<str:category>/<str:menuitem_name>/leave_feedback/', views.leave_feedback, name='leave_feedback'),
    # path('resources/<str:category>/', views.Resources, name='resources'),
    path('resources/', views.Resources, name='resources'),
    path('account-numbers/', views.Accountnumbers, name='account_numbers'),
    path('resource-category/', views.Resourcecat, name='resource_category'),
    path('menu-categories/', views.Menucat, name='menu_categories'),
    path('sales/', views.Saleview, name='sales'),
    path('foodsales/', views.Foodsaleview, name='foodsales'),
    path('check_resources/', views.check_resources, name='check_resources'),
    path('sales_report/', views.sales_report, name='sales_report'),
    
    
]