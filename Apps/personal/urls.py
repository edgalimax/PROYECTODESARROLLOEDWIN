from django.urls import path
from . import views
app_name = 'personal'
urlpatterns = [
    path('', views.personal_list, name='list'),
    path('nuevo/', views.personal_create, name='create'),
    path('<int:pk>/', views.personal_detail, name='detail'),
    path('<int:pk>/editar/', views.personal_update, name='update'),
    path('<int:pk>/eliminar/', views.personal_delete, name='delete'),
    path('exportar/', views.exportar_csv, name='export'),
]
