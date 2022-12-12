from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import AccessMixin


class StaffRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and staff."""

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_authenticated and request.user.is_staff):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


def staff_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None
):
    """
    Decorator for views that checks that the user is logged in and staff, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
