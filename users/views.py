from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from django.views.generic import CreateView
from apps.common.models import Product
from users.models import Profile
from users.forms import SigninForm, SignupForm, UserPasswordChangeForm, UserSetPasswordForm, UserPasswordResetForm, ProfileForm
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from users.utils import user_filter

# Create your views here.

def index(request):
    return render(request, "dashboard/index.html", {

    })


class SignInView(LoginView):
    form_class = SigninForm
    template_name = "authentication/sign-in.html"
    
    def get_success_url(self): 
        user = self.request.user
        if user.is_authenticated:
            if getattr(user, 'is_admin', False):
                return reverse_lazy("admin_dashboard")
            role = getattr(user, 'role', None)
            if role == "customer":
                return reverse_lazy("customer_dashboard")
            elif role == "admin":
                messages.error(self.request, "Role not recognized! Please wait for admin to assign a role.")
                return reverse_lazy("wait_for_role")
        else:
            messages.error(self.request, "You must be logged in to access this page.")
            return reverse_lazy("signin")

        return reverse_lazy("dashboard")

class SignUpView(CreateView):
    form_class = SignupForm
    template_name = "authentication/sign-up.html"
    success_url = "/users/signin/"

class UserPasswordChangeView(PasswordChangeView):
    template_name = 'authentication/password-change.html'
    form_class = UserPasswordChangeForm

class UserPasswordResetView(PasswordResetView):
    template_name = 'authentication/forgot-password.html'
    form_class = UserPasswordResetForm

class UserPasswrodResetConfirmView(PasswordResetConfirmView):
    template_name = 'authentication/reset-password.html'
    form_class = UserSetPasswordForm


def signout_view(request):
    logout(request)
    return redirect(reverse('signin'))


@login_required(login_url='/users/signin/')
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    else:
        form = ProfileForm(instance=profile)
    
    context = {
        'form': form,
        'segment': 'profile',
    }
    return render(request, 'dashboard/profile.html', context)


@login_required(login_url='/users/signin/')
def wait_for_role_assignment(request):

    return render(request, "authentication/wait_for_role.html")

def upload_avatar(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        profile.avatar = request.FILES.get('avatar')
        profile.save()
        messages.success(request, 'Avatar uploaded successfully')
    return redirect(request.META.get('HTTP_REFERER'))


def change_password(request):
    user = request.user
    if request.method == 'POST':
        if check_password(request.POST.get('current_password'), user.password):
            user.set_password(request.POST.get('new_password'))
            user.save()
            messages.success(request, 'Password changed successfully')
        else:
            messages.error(request, "Password doesn't match!")
    return redirect(request.META.get('HTTP_REFERER'))



def user_list(request):
    filters = user_filter(request)
    user_list = User.objects.filter(**filters)
    form = SignupForm()

    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 5)
    users = paginator.page(page)

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            return post_request_handling(request, form)

    context = {
        'users': users,
        'form': form,
    }
    return render(request, 'apps/users.html', context)


@login_required(login_url='/users/signin/')
def post_request_handling(request, form):
    form.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/users/signin/')
def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/signin/')
def update_user(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/signin/')
def user_change_password(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.set_password(request.POST.get('password'))
        user.save()
    return redirect(request.META.get('HTTP_REFERER'))