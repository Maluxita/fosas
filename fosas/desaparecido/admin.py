from django.contrib import admin
from .models import Desaparecido 
# Register your models here.

class DesaparecidoAdmin(admin.ModelAdmin):
    model = Desaparecido

admin.site.register(Desaparecido, DesaparecidoAdmin)