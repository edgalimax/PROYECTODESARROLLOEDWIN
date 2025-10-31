from django.shortcuts import render
from Apps.personal.models import Personal
from Apps.requisiciones.models import Requisicion
from django.db.models import Count

def index(request):
    total_activo = Personal.objects.filter(estado='ALTA').count()
    por_proyecto = (Personal.objects.values('proyecto').annotate(total=Count('id')).order_by('proyecto'))
    req_pendientes = Requisicion.objects.filter(estado='PENDIENTE').count()
    return render(request, 'dashboard/index.html', {
        'total_activo': total_activo, 'por_proyecto': por_proyecto, 'req_pendientes': req_pendientes
    })
