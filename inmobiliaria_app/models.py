from django.db import models

# Create your models here.

class Inmobiliaria(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre


class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    inmobiliaria = models.ForeignKey(Inmobiliaria, on_delete=models.CASCADE, related_name='propietarios')

    def __str__(self):
        return self.nombre

class Edificio(models.Model):
    inmobiliaria = models.ForeignKey(Inmobiliaria, on_delete=models.CASCADE, related_name='edificios')
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    numero_pisos = models.IntegerField()
    numero_apartamentos = models.IntegerField()
    numero_habitaciones = models.IntegerField()
    propietarios = models.ManyToManyField(Propietario, related_name='edificios_propiedad')

    def __str__(self):
        return self.nombre
    

class Casa(models.Model):
    inmobiliaria = models.ForeignKey(Inmobiliaria, on_delete=models.CASCADE, related_name='casas')
    localidad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    numero_habitaciones = models.IntegerField()
    area_terreno = models.DecimalField(max_digits=10, decimal_places=2)
    propietarios = models.ManyToManyField(Propietario, related_name='casas_propiedad')

    def __str__(self):
        return self.localidad

class Finca(models.Model):
    inmobiliaria = models.ForeignKey(Inmobiliaria, on_delete=models.CASCADE, related_name='fincas')
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    area_total = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_terreno = models.CharField(max_length=100)
    propietarios = models.ManyToManyField(Propietario, related_name='fincas_propiedad')

    def __str__(self):
        return self.nombre







