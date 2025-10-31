from django.db import models
class Personal(models.Model):
    PROYECTOS = [('ON_DEMAND','On Demand'),('POLLO_BRUJO','Pollo Brujo'),('FIJOS','Proyectos Fijos')]
    ESTADOS = [('ALTA','Alta'),('BAJA','Baja')]
    nombre = models.CharField(max_length=150)
    dpi = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=30, blank=True)
    proyecto = models.CharField(max_length=20, choices=PROYECTOS)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='ALTA')
    fecha_ingreso = models.DateField(auto_now_add=True)
    observaciones = models.TextField(blank=True)
    def __str__(self): return f"{self.nombre} - {self.get_proyecto_display()}"
