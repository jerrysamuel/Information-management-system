from django import forms
from .models import Resourcecategory, Resource, Humanresource, Menucategory, Menuitem, Feedback, Accountdetail, Sales, Foodsales


class ResourcecatForm(forms.ModelForm):
    class Meta:
        model = Resourcecategory

        fields = '__all__'
    
class MenucatForm(forms.ModelForm):
    class Meta:
        model = Menucategory

        fields = '__all__'

class MenuitemForm(forms.ModelForm):
    class Meta:
        model = Menuitem

        fields = '__all__'


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource

        fields = '__all__'
    
class HumanesourceForm(forms.ModelForm):
    class Meta:
        model = Humanresource

        fields = '__all__'
    

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['item', 'customer', 'unit_sold']
        widgets = {
            'item': forms.Select(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500',
                'placeholder': 'Item'
            }),
            'customer': forms.TextInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500',
                'placeholder': 'Customer'
            }),
            'unit_sold': forms.NumberInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500',
                'placeholder': 'Unit Sold'
            })
        }


class FoodsalesForm(forms.ModelForm):
    class Meta:
        model = Foodsales
        fields = ['food', 'unit_sold']
        widgets = {
            'food': forms.Select(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500',
                'placeholder': 'Food'
            }),
            'unit_sold': forms.NumberInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500',
                'placeholder': 'Unit Sold'
            })
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['user', 'comment', 'rating']
        widgets = {
            'user': forms.TextInput(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500',
                'placeholder': 'User'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500',
                'placeholder': 'Comment'
            }),
            'rating': forms.Select(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500',
            })
        }
