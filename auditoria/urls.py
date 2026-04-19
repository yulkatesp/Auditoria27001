from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('menu/', views.menu, name='menu'),
    path('logout/', views.logout_view, name='logout'),

    path('empresa/nueva/', views.crear_empresa, name='crear_empresa'),
    path('empresas/', views.lista_empresas, name='lista_empresas'),

    path('rol/<int:empresa_id>/', views.seleccionar_rol, name='seleccionar_rol'),
    path('controles/<int:empresa_id>/', views.evaluacion, name='evaluacion'),

    path('reporte/excel/<int:empresa_id>/', views.reporte_excel, name='reporte_excel'),
    path('reporte/pdf/<int:empresa_id>/', views.reporte_pdf, name='reporte_pdf'),
    path('dashboard/<int:empresa_id>/', views.dashboard, name='dashboard'),
    path('registro/', views.registro_view, name='registro'),
    path('lista-maestra/', views.lista_maestra, name='lista_maestra'),
    path('lista-maestra/actualizar/<int:doc_id>/', views.actualizar_documento, name='actualizar_documento'),
]
