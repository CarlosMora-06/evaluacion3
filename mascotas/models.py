from django.db import models

# Create your models here.

class Responsable(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    correo = models.EmailField(unique=True,null=False)
    rut =models.CharField(max_length=12,null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Responsables"
        ordering = ["nombre"]

class Mascota(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    anio_nacimiento = models.PositiveIntegerField(null=False)
    especie = models.CharField(max_length=100,null=False)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Mascotas"
        ordering = ["nombre"]