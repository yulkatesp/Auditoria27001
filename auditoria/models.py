from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    nit = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100, blank=True)
    representante_legal = models.CharField(max_length=200, blank=True)
    fecha_registro = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Auditoria(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    auditor = models.CharField(max_length=100)

    def __str__(self):
        return f"Auditoría {self.empresa.nombre} - {self.fecha}"


class Control(models.Model):
    codigo = models.CharField(max_length=10)  # Ej: A.5.1
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    
    categoria = models.CharField(max_length=50) 
    # Organizacional, Personas, Físicos, Tecnológicos

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Evaluacion(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    control = models.ForeignKey(Control, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)
    rol = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)


class DocumentoSGSI(models.Model):
    CATEGORIAS = [
        ('DG', 'Documentos Generales'),
        ('CD', 'Control de Documentos'),
        ('VR', 'Valoración y Plan de Tratamiento de Riesgos'),
        ('CC', 'Concientización y Comunicación'),
        ('AI', 'Auditoría Interna'),
        ('AC', 'Acciones Correctivas y de Mejora'),
        ('RD', 'Revisión por la Dirección'),
        ('PS', 'Políticas de Seguridad'),
        ('OS', 'Organización de la Seguridad de la Información'),
        ('RH', 'Seguridad de los Recursos Humanos'),
        ('GA', 'Gestión de Activos'),
        ('CA', 'Control de Acceso'),
        ('EN', 'Encriptación'),
        ('SF', 'Seguridad Física y Ambiental'),
        ('SO', 'Seguridad en la Operación'),
        ('SC', 'Seguridad en las Comunicaciones'),
        ('AD', 'Adquisición, Desarrollo y Mantenimiento de Sistemas'),
        ('RP', 'Relación con Proveedores'),
        ('GI', 'Gestión de Incidentes de Seguridad'),
        ('CN', 'Continuidad del Negocio'),
        ('CU', 'Cumplimiento'),
    ]

    codigo = models.CharField(max_length=20)
    version = models.CharField(max_length=10, default='1.0')
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=2, choices=CATEGORIAS)
    ubicacion = models.CharField(max_length=200, default='/docs/')
    ultima_revision = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    class Meta:
        ordering = ['categoria', 'codigo']


