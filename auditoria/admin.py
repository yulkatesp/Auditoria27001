from django.contrib import admin
from .models import Empresa, Auditoria, Control, Evaluacion

admin.site.register(Empresa)
admin.site.register(Auditoria)
admin.site.register(Control)
admin.site.register(Evaluacion)
