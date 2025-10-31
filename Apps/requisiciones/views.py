from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Requisicion
from .forms import RequisicionForm
from Apps.personal.models import Personal

def requisicion_list(request):
    qs = Requisicion.objects.all().order_by('-id')
    return render(request, 'requisiciones/list.html', {'requisiciones': qs})

def requisicion_create(request):
    if request.method == 'POST':
        form = RequisicionForm(request.POST)
        if form.is_valid():
            form.save(); messages.success(request, 'Requisición creada.')
            return redirect('requisiciones:list')
    else:
        form = RequisicionForm()
    return render(request, 'requisiciones/form.html', {'form': form})

def requisicion_aprobar(request, pk):
    obj = get_object_or_404(Requisicion, pk=pk)
    if obj.estado != 'APROBADA':
        for i in range(obj.cantidad):
            Personal.objects.create(
                nombre=f"Pendiente asignación {obj.id}-{i+1}",
                dpi=f"SIN-DPI-{obj.id}-{i+1}",
                telefono='', proyecto=obj.proyecto, estado='ALTA',
                observaciones=f"Creado por aprobación de requisición #{obj.id}"
            )
        obj.estado = 'APROBADA'; obj.save()
        messages.success(request, 'Requisición aprobada y personal creado.')
    return redirect('requisiciones:list')

def requisicion_rechazar(request, pk):
    obj = get_object_or_404(Requisicion, pk=pk)
    if obj.estado != 'RECHAZADA':
        obj.estado = 'RECHAZADA'; obj.save()
        messages.info(request, 'Requisición rechazada (histórico).')
    return redirect('requisiciones:list')
