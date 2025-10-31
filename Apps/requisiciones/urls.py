from django.urls import path
from . import views
app_name = 'requisiciones'
urlpatterns = [
    path('', views.requisicion_list, name='list'),
    path('nueva/', views.requisicion_create, name='create'),
    path('<int:pk>/aprobar/', views.requisicion_aprobar, name='aprobar'),
    path('<int:pk>/rechazar/', views.requisicion_rechazar, name='rechazar'),
]
