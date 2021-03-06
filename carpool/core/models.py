from django.conf import settings
from django.db import models
from django.utils import timezone


class Pool(models.Model):
    TIPO_POOL = (
        ('regular', 'Regular'),
        ('irregular', 'Irregular'),
    )

    creador = models.ForeignKey(settings.AUTH_USER_MODEL)
    origen = models.ForeignKey('localidad.Colonia', related_name='origen')
    destino = models.ForeignKey('localidad.Colonia', related_name='destino')
    tipo = models.CharField(max_length=10, choices=TIPO_POOL)
    dias = models.ManyToManyField('Dia', blank=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.CharField(max_length=10, blank=True, null=True)
    contacto_email = models.CharField(max_length=255, blank=True, null=True)
    contacto_telefono = models.CharField(max_length=15, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True, default=timezone.now)

    def __unicode__(self):
        return self.creador.email


class Dia(models.Model):
    dia = models.CharField(max_length=10)

    def __unicode__(self):
        return self.dia

    class Meta:
        verbose_name_plural = "Dias"
