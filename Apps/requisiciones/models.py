from django.db import models
class Requisicion(models.Model):
    PROYECTOS = [('ON_DEMAND','On Demand'),('POLLO_BRUJO','Pollo Brujo'),('FIJOS','Proyectos Fijos')]
    ESTADOS = [('PENDIENTE','Pendiente'),('APROBADA','Aprobada'),('RECHAZADA','Rechazada')]
    proyecto = models.CharField(max_length=20, choices=PROYECTOS)
    cantidad = models.PositiveIntegerField()
    justificacion = models.TextField()
    fecha_solicitud = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='PENDIENTE')
    def __str__(self): return f"{self.get_proyecto_display()} - {self.cantidad} ({self.estado})"
