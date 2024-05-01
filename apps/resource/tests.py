from django.test import TestCase
from .models import *

class ResourceModelTestCase(TestCase):
    def setUp(self):
        self.category = Resourcecategory.objects.create(name='Test Category')
        self.resource = Resource.objects.create(category=self.category, name='Test Resource', quantity=10, description='Test description', weight=5.0, worth=100.0, price_per_unit=10.0)

    def test_resource_creation(self):
        self.assertEqual(self.resource.name, 'Test Resource')
        self.assertEqual(self.resource.category.name, 'Test Category')


class AccountdetailModelTestCase(TestCase):
    def setUp(self):
        self.resource = Humanresource.objects.create(name='Test Human Resource', age=30, salary=50000.0)
        self.account_detail = Accountdetail.objects.create(name=self.resource, accountnum=123456789, bank_name='Test Bank')

    def test_account_detail_creation(self):
        self.assertEqual(self.account_detail.name.name, 'Test Human Resource')
        self.assertEqual(self.account_detail.accountnum, 123456789)
        self.assertEqual(self.account_detail.bank_name, 'Test Bank')

class MenuitemModelTestCase(TestCase):
    def setUp(self):
        self.category = Menucategory.objects.create(name='Test Category')
        self.menu_item = Menuitem.objects.create(category=self.category, name='Test Menu Item', description='Test description', price=50.0)

    def test_menu_item_creation(self):
        self.assertEqual(self.menu_item.name, 'Test Menu Item')
        self.assertEqual(self.menu_item.category.name, 'Test Category')

class FeedbackModelTestCase(TestCase):
    def setUp(self):
        self.category = Menucategory.objects.create(name='Test Category')
        self.menu_item = Menuitem.objects.create(category=self.category, name='Test Menu Item', description='Test description', price=50.0)
        self.feedback = Feedback.objects.create(user='Test User', item=self.menu_item, comment='Test comment', rating='5')

    def test_feedback_creation(self):
        self.assertEqual(self.feedback.user, 'Test User')
        self.assertEqual(self.feedback.item.name, 'Test Menu Item')
        self.assertEqual(self.feedback.comment, 'Test comment')
        self.assertEqual(self.feedback.rating, '5')
