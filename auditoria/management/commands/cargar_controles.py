from django.core.management.base import BaseCommand
import json
import os
from django.conf import settings
from auditoria.models import Control


class Command(BaseCommand):
    help = 'Cargar controles ISO'

    def handle(self, *args, **kwargs):

        ruta = os.path.join(settings.BASE_DIR, 'auditoria', 'data', 'controles.json')

        with open(ruta, encoding='utf-8') as f:
            data = json.load(f)

            for item in data:
                Control.objects.get_or_create(
                    codigo=item['codigo'],
                    defaults={
                        'nombre': item['nombre'],
                        'descripcion': item['descripcion'],
                        'categoria': item['categoria']
                    }
                )

        self.stdout.write(self.style.SUCCESS('Controles cargados correctamente'))