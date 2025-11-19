from django.urls import path
from . import views

urlpatterns = [
    # ... (Tus URLs existentes de Cliente, Empleado, Servicio, Contrato van aquí) ...
    path('', views.inicio_jardineria, name='inicio_jardineria'),
    
    # (Pega aquí todas tus rutas anteriores de Clientes, Empleados, Servicios y Contratos)
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('clientes/actualizar/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/<int:cliente_id>/', views.borrar_cliente, name='borrar_cliente'),
    
    # ... (URLs de Empleados, Servicios y Contratos igual que antes) ...
    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/<int:empleado_id>/', views.detalle_empleado, name='detalle_empleado'),
    path('empleados/actualizar/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/borrar/<int:empleado_id>/', views.borrar_empleado, name='borrar_empleado'),

    path('servicios/', views.ver_servicios, name='ver_servicios'),
    path('servicios/agregar/', views.agregar_servicio, name='agregar_servicio'),
    path('servicios/<int:servicio_id>/', views.detalle_servicio, name='detalle_servicio'),
    path('servicios/actualizar/<int:servicio_id>/', views.actualizar_servicio, name='actualizar_servicio'),
    path('servicios/borrar/<int:servicio_id>/', views.borrar_servicio, name='borrar_servicio'),

    path('contratos/', views.ver_contratos, name='ver_contratos'),
    path('contratos/agregar/', views.agregar_contrato, name='agregar_contrato'),
    path('contratos/actualizar/<int:contrato_id>/', views.actualizar_contrato, name='actualizar_contrato'),
    path('contratos/borrar/<int:contrato_id>/', views.borrar_contrato, name='borrar_contrato'),

    # --- URLs MATERIAL (NUEVAS) ---
    path('materiales/', views.ver_materiales, name='ver_materiales'),
    path('materiales/agregar/', views.agregar_material, name='agregar_material'),
    path('materiales/actualizar/<int:material_id>/', views.actualizar_material, name='actualizar_material'),
    path('materiales/borrar/<int:material_id>/', views.borrar_material, name='borrar_material'),
]