
from django.db import models

class usuario(models.Model):
		nombre = models.CharField(max_length=20)
		descripcion = models.CharField(max_length=30)
		direccion = models.CharField(max_length=30)
		fecha = models.DateTimeField()

		#def__unicode__(self):
			#return self.nombre
		
