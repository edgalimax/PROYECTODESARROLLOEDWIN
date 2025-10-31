from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    """
    Cierra la sesión del usuario inmediatamente usando GET o POST
    y redirige al login.
    """
    logout(request)
    return redirect('usuarios:login')
