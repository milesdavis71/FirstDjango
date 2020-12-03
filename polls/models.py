from django.db import models


# Modellek.
class Kerdes(models.Model):
    kerdes_text = models.CharField(max_length=200)
    kihelyezes_ideje = models.DateField('date published')


class Valasztas(models.Model):
    kerdes = models.ForeignKey(Kerdes, on_delete=models.CASCADE)
    valasztas_text = models.CharField(max_length=200)
    szavazas = models.IntegerField(default=0)