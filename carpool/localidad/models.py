from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Colonia(models.Model):
    nombre = models.CharField(max_length=60)

    def __unicode__(self):
        return self.nombre
