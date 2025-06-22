from django.contrib import admin
from .models import Resourcecategory, Resource, Humanresource, Accountdetail, Menucategory, Menuitem, Feedback, Sales, Foodsales

# Admin class for Resourcecategory
class ResourcecategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

# Admin class for Resource
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'description', 'weight', 'worth', 'price_per_unit')
    list_filter = ('category',)

# Admin class for Humanresource
class HumanresourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'salary', 'hire_date')

# Admin class for Accountdetail
class AccountdetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'accountnum', 'bank_name')

# Admin class for Menucategory
# class MenucategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'image')

# Admin class for Menuitem
# class MenuitemAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'description', 'price', 'image')
#     list_filter = ('category',)

# Admin class for Feedback
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'comment', 'rating')
    list_filter = ('item',)

# class FoodsalesAdmin(admin.ModelAdmin):
#     list_display = ['food', 'unit_sold', 'date']
#      # Assuming 'name' is a field in the Menuitem model

class SalesAdmin(admin.ModelAdmin):
    list_display = ['item', 'customer', 'unit_sold', 'date']
    

# Register models with their respective admin classes
admin.site.register(Resourcecategory, ResourcecategoryAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Humanresource, HumanresourceAdmin)
admin.site.register(Accountdetail, AccountdetailAdmin)
# admin.site.register(Menucategory, MenucategoryAdmin)
# admin.site.register(Menuitem, MenuitemAdmin)
admin.site.register(Feedback, FeedbackAdmin)
# admin.site.register(Foodsales, FoodsalesAdmin)
admin.site.register(Sales, SalesAdmin)
