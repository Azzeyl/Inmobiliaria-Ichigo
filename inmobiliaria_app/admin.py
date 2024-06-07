from django.contrib import admin
from inmobiliaria_app.models import Inmobiliaria,Propietario,Edificio,Casa,Finca

# Register your models here.
admin.site.register(Inmobiliaria)
admin.site.register(Propietario)
admin.site.register(Edificio)
admin.site.register(Casa)
admin.site.register(Finca)
