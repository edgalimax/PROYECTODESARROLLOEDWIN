from django.apps import AppConfig
class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Apps.usuarios'
    def ready(self):
        # Auto-create a superuser if database is ready
        from django.contrib.auth import get_user_model
        from django.db.utils import OperationalError, ProgrammingError
        try:
            User = get_user_model()
            if not User.objects.filter(is_superuser=True).exists():
                User.objects.create_superuser(username='admin', email='', password='admin123')
        except (OperationalError, ProgrammingError):
            pass
