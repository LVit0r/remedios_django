from django.contrib import admin

from .models import Remedio
from .models import Paciente

class RemediosExibidosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'mg', 'turno')

admin.site.register(Remedio, RemediosExibidosAdmin)


class RemediosPacientes(admin.ModelAdmin):
    list_display = ['nome', 'remedios']

    def display_remedios(self, obj):
        return ', '.join([remedio.nome for remedio in obj.remedios.all()])

admin.site.register(Paciente, RemediosPacientes)
