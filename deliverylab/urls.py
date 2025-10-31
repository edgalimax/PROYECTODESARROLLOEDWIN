from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Apps.dashboard.urls')),
    path('personal/', include('Apps.personal.urls')),
    path('requisiciones/', include('Apps.requisiciones.urls')),
    path('usuarios/', include('Apps.usuarios.urls')),
    path('', RedirectView.as_view(pattern_name='dashboard:index', permanent=False)),
]
