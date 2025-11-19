from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Empleado, Servicio, ContratoServicio, Material

# --- VISTAS GENERALES ---
def inicio_jardineria(request):
    return render(request, 'inicio.html')

# --- VISTAS CRUD CLIENTE ---
def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        email = request.POST['email']
        direccion = request.POST['direccion']
        ciudad = request.POST['ciudad']
        codigo_postal = request.POST['codigo_postal']
        
        Cliente.objects.create(
            nombre=nombre, apellido=apellido, telefono=telefono,
            email=email, direccion=direccion, ciudad=ciudad,
            codigo_postal=codigo_postal
        )
        return redirect('ver_clientes')
    return render(request, 'cliente/agregar_cliente.html')

def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    contratos_cliente = ContratoServicio.objects.filter(cliente=cliente)
    return render(request, 'cliente/detalle_cliente.html', {'cliente': cliente, 'contratos_cliente': contratos_cliente})

def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.telefono = request.POST['telefono']
        cliente.email = request.POST['email']
        cliente.direccion = request.POST['direccion']
        cliente.ciudad = request.POST['ciudad']
        cliente.codigo_postal = request.POST['codigo_postal']
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})


# --- VISTAS CRUD EMPLEADO ---
def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        puesto = request.POST['puesto']
        telefono = request.POST['telefono']
        email = request.POST['email']
        fecha_contratacion = request.POST['fecha_contratacion']
        salario = request.POST['salario']
        
        Empleado.objects.create(
            nombre=nombre, apellido=apellido, puesto=puesto,
            telefono=telefono, email=email, fecha_contratacion=fecha_contratacion,
            salario=salario
        )
        return redirect('ver_empleados')
    return render(request, 'empleado/agregar_empleado.html')

def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleados.html', {'empleados': empleados})

def detalle_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    servicios_asignados = empleado.servicios_asignados.all()
    return render(request, 'empleado/detalle_empleado.html', {'empleado': empleado, 'servicios_asignados': servicios_asignados})

def actualizar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.puesto = request.POST['puesto']
        empleado.telefono = request.POST['telefono']
        empleado.email = request.POST['email']
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        empleado.salario = request.POST['salario']
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})

def borrar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})


# --- VISTAS CRUD SERVICIO ---
def agregar_servicio(request):
    if request.method == 'POST':
        nombre_servicio = request.POST['nombre_servicio']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        duracion_estimada_horas = request.POST['duracion_estimada_horas']
        activo = True if 'activo' in request.POST else False
        tipo_servicio = request.POST['tipo_servicio']
        
        Servicio.objects.create(
            nombre_servicio=nombre_servicio, descripcion=descripcion, precio=precio,
            duracion_estimada_horas=duracion_estimada_horas, activo=activo,
            tipo_servicio=tipo_servicio
        )
        return redirect('ver_servicios')
    return render(request, 'servicio/agregar_servicio.html')

def ver_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicio/ver_servicios.html', {'servicios': servicios})

def detalle_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    contratos_servicio = ContratoServicio.objects.filter(servicio=servicio)
    return render(request, 'servicio/detalle_servicio.html', {'servicio': servicio, 'contratos_servicio': contratos_servicio})

def actualizar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    if request.method == 'POST':
        servicio.nombre_servicio = request.POST['nombre_servicio']
        servicio.descripcion = request.POST['descripcion']
        servicio.precio = request.POST['precio']
        servicio.duracion_estimada_horas = request.POST['duracion_estimada_horas']
        servicio.activo = True if 'activo' in request.POST else False
        servicio.tipo_servicio = request.POST['tipo_servicio']
        servicio.save()
        return redirect('ver_servicios')
    return render(request, 'servicio/actualizar_servicio.html', {'servicio': servicio})

def borrar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    if request.method == 'POST':
        servicio.delete()
        return redirect('ver_servicios')
    return render(request, 'servicio/borrar_servicio.html', {'servicio': servicio})


# --- VISTAS CRUD CONTRATO ---
def ver_contratos(request):
    contratos = ContratoServicio.objects.all().order_by('-fecha_contrato')
    return render(request, 'contrato/ver_contratos.html', {'contratos': contratos})

def agregar_contrato(request):
    clientes = Cliente.objects.all()
    servicios = Servicio.objects.all()
    empleados = Empleado.objects.all()
    
    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        servicio_id = request.POST['servicio']
        empleados_ids = request.POST.getlist('empleados')
        fecha_programada = request.POST['fecha_programada']
        estado = request.POST['estado']
        observaciones = request.POST.get('observaciones', '')
        costo_total = request.POST.get('costo_total')

        cliente = get_object_or_404(Cliente, pk=cliente_id)
        servicio = get_object_or_404(Servicio, pk=servicio_id)

        contrato = ContratoServicio.objects.create(
            cliente=cliente,
            servicio=servicio,
            fecha_programada=fecha_programada,
            estado=estado,
            observaciones=observaciones,
            costo_total=costo_total if costo_total else None
        )
        contrato.empleados.set(empleados_ids)

        return redirect('ver_contratos')

    return render(request, 'contrato/agregar_contrato.html', {
        'clientes': clientes,
        'servicios': servicios,
        'empleados': empleados,
    })

def actualizar_contrato(request, contrato_id):
    contrato = get_object_or_404(ContratoServicio, pk=contrato_id)
    clientes = Cliente.objects.all()
    servicios = Servicio.objects.all()
    empleados = Empleado.objects.all()

    if request.method == 'POST':
        contrato.cliente = get_object_or_404(Cliente, pk=request.POST['cliente'])
        contrato.servicio = get_object_or_404(Servicio, pk=request.POST['servicio'])
        contrato.fecha_programada = request.POST['fecha_programada']
        contrato.estado = request.POST['estado']
        contrato.observaciones = request.POST.get('observaciones', '')
        costo_total = request.POST.get('costo_total')
        contrato.costo_total = costo_total if costo_total else None
        contrato.save()
        
        empleados_ids = request.POST.getlist('empleados')
        contrato.empleados.set(empleados_ids)

        return redirect('ver_contratos')
    
    empleados_seleccionados_ids = contrato.empleados.values_list('id', flat=True)

    return render(request, 'contrato/actualizar_contrato.html', {
        'contrato': contrato,
        'clientes': clientes,
        'servicios': servicios,
        'empleados': empleados,
        'empleados_seleccionados_ids': list(empleados_seleccionados_ids),
    })

def borrar_contrato(request, contrato_id):
    contrato = get_object_or_404(ContratoServicio, pk=contrato_id)
    if request.method == 'POST':
        contrato.delete()
        return redirect('ver_contratos')
    return render(request, 'contrato/borrar_contrato.html', {'contrato': contrato})


# --- VISTAS CRUD MATERIAL (NUEVO) ---
def agregar_material(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        tipo = request.POST['tipo']
        cantidad = request.POST['cantidad']
        precio = request.POST['precio']
        proveedor = request.POST['proveedor']
        
        Material.objects.create(
            nombre=nombre, tipo=tipo, cantidad=cantidad,
            precio=precio, proveedor=proveedor
        )
        return redirect('ver_materiales')
    return render(request, 'material/agregar_material.html')

def ver_materiales(request):
    materiales = Material.objects.all()
    return render(request, 'material/ver_materiales.html', {'materiales': materiales})

def actualizar_material(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    if request.method == 'POST':
        material.nombre = request.POST['nombre']
        material.tipo = request.POST['tipo']
        material.cantidad = request.POST['cantidad']
        material.precio = request.POST['precio']
        material.proveedor = request.POST['proveedor']
        material.save()
        return redirect('ver_materiales')
    return render(request, 'material/actualizar_material.html', {'material': material})

def borrar_material(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    if request.method == 'POST':
        material.delete()
        return redirect('ver_materiales')
    return render(request, 'material/borrar_material.html', {'material': material})