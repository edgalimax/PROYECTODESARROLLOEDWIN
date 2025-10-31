from django.contrib import admin
from .models import Personal
@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','dpi','proyecto','estado','fecha_ingreso')
    search_fields = ('nombre','dpi')
    list_filter = ('proyecto','estado')
