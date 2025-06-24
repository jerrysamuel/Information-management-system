from django.test import TestCase
from django.contrib.auth import get_user_model
from users.models import Profile
from .forms import *

User = get_user_model()

class AccountModelTestCase(TestCase):
    def test_create_user(self):
        # Test creating a new user
        user = User.objects.create_user(email='test@example.com', username='testuser', password='testpass')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'testuser')
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)

    def test_create_superuser(self):
        # Test creating a new superuser
        admin_user = User.objects.create_superuser(email='admin@example.com', username='adminuser', password='adminpass')
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertEqual(admin_user.username, 'adminuser')
        self.assertTrue(admin_user.is_admin)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class ProfileModelTestCase(TestCase):
    def test_create_profile(self):
        # Test creating a new profile
        user = User.objects.create_user(email='profile@example.com', username='profileuser', password='profilepass')
        profile = Profile.objects.create(
            user=user,
            full_name='John Doe',
            country='USA',
            city='New York',
            zip_code='10001',
            address='123 Main St',
            phone='123-456-7890'
        )
        self.assertEqual(profile.user.username, 'profileuser')
        self.assertEqual(profile.full_name, 'John Doe')
        self.assertEqual(profile.country, 'USA')
        self.assertEqual(profile.city, 'New York')
        self.assertEqual(profile.zip_code, '10001')
        self.assertEqual(profile.address, '123 Main St')
        self.assertEqual(profile.phone, '123-456-7890')

# class FormsTestCase(TestCase):
#     # create dummy user for testing
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')

#     def test_signin_form(self):
#         # Test data (empty data)
#         form_data = {}
#         # Instantiate the form with test data
#         form = SigninForm(data=form_data)
#         # Assert that the form is not valid (as expected)
#         self.assertFalse(form.is_valid())

#     def test_signup_form(self):
#         # Test data (empty data)
#         form_data = {}
#         # Instantiate the form with test data
#         form = SignupForm(data=form_data)
#         # Assert that the form is not valid (as expected)
#         self.assertFalse(form.is_valid())

#     def test_user_password_reset_form(self):
#         # Test valid form data
#         form_data = {'email': 'test@example.com'}
#         form = UserPasswordResetForm(data=form_data)
#         self.assertTrue(form.is_valid())

#         # Test invalid form data
#         form_data = {'email': ''}
#         form = UserPasswordResetForm(data=form_data)
#         self.assertFalse(form.is_valid())

#     def test_user_set_password_form(self):
#         form_data = {
#             'new_password1': 'newpassword',
#             'new_password2': 'newpassword',
#         }
#         form = UserSetPasswordForm(user=self.user, data=form_data)
#         self.assertTrue(form.is_valid())

#     def test_user_password_change_form(self):
#         form_data = {
#             'old_password': 'password',
#             'new_password1': 'newpassword',
#             'new_password2': 'newpassword',
#         }
#         form = UserPasswordChangeForm(user=self.user, data=form_data)
#         self.assertTrue(form.is_valid())
#     def test_profile_form(self):
#         # Test data (empty data)
#         form_data = {}
#         # Instantiate the form with test data
#         form = ProfileForm(data=form_data)
#         # Assert that the form is not valid (as expected)
#         self.assertFalse(form.is_valid())
class SigninFormTestCase(TestCase):
    def test_valid_signin_form(self):
        # Create a user for testing
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

        # Prepare form data
        form_data = {
            'username': 'test@example.com',
            'password': 'password123'
        }

        # Instantiate the form with form data
        form = SigninForm(data=form_data)

        # Verify that the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_signin_form(self):
        # Prepare form data with invalid password
        invalid_password_data = {
            'username': 'test@example.com',
            'password': 'invalidpassword'
        }

        # Instantiate the form with form data containing an invalid password
        form = SigninForm(data=invalid_password_data)

        # Verify that the form is invalid
        self.assertFalse(form.is_valid())

        # Prepare form data with invalid username
        invalid_username_data = {
            'username': 'invalid@example.com',
            'password': 'password123'
        }

        # Instantiate the form with form data containing an invalid username
        form = SigninForm(data=invalid_username_data)

        # Verify that the form is invalid
        self.assertFalse(form.is_valid())

class SignupFormTestCase(TestCase):
    def test_valid_signup_form(self):
        # Prepare valid form data, make sure the password is a strong password else you get an error
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'password345',
            'password2': 'password345',
            'role': 'customer'
        }

        # Instantiate the form with form data
        form = SignupForm(data=form_data)

        # Verify that the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_signup_form(self):
        # Prepare form data with mismatched passwords
        mismatched_passwords_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'password123',
            'password2': 'differentpassword',
            'role': 'customer'
        }

        # Instantiate the form with form data containing mismatched passwords
        form = SignupForm(data=mismatched_passwords_data)

        # Verify that the form is invalid
        self.assertFalse(form.is_valid())

        # Prepare form data with missing required field (email)
        missing_email_data = {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123',
            'role': 'customer'
        }

        # Instantiate the form with form data containing missing email
        form = SignupForm(data=missing_email_data)

        # Verify that the form is invalid
        self.assertFalse(form.is_valid())