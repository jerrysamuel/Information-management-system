from functools import wraps
from django.shortcuts import redirect


def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_admin:
            return view_func(request, *args, **kwargs)
        else:
            # Redirect to a different page or raise PermissionDenied
            return redirect("index")  # You need to define this URL
    return wrapper

def customer_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.role == 'customer':
            return view_func(request, *args, **kwargs)
        else:
            # Redirect to a different page or raise PermissionDenied
            return redirect("index")  # You need to define this URL
    return wrapper

def waiter_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.role == 'waiter':
            return view_func(request, *args, **kwargs)
        else:
            # Redirect to a different page or raise PermissionDenied
            return redirect("index")  # You need to define this URL
    return wrapper