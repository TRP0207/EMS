from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy


def manager_required(view_func, login_url=reverse_lazy('Emp_profile:base')):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_manager,
        login_url=login_url
    )

    if view_func:
        return actual_decorator(view_func)
    return actual_decorator
