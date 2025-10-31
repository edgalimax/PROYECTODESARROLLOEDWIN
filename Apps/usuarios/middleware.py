from django.shortcuts import redirect
from django.urls import resolve
from django.conf import settings
EXEMPT_URLS = {'usuarios:login','usuarios:logout','admin:index','admin:login'}
class LoginRequiredMiddleware:
    def __init__(self, get_response): self.get_response = get_response
    def __call__(self, request):
        match = resolve(request.path_info)
        if (not request.user.is_authenticated
            and match and match.view_name not in EXEMPT_URLS
            and not request.path.startswith('/static/')):
            return redirect(settings.LOGIN_URL)
        return self.get_response(request)
