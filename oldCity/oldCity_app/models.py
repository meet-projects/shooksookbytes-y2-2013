from django.db import models

# Create your models here.
class Shop(models.Model):
	name = models.CharField(max_length=20)
	location = models.CharField(max_length=40)
	description = models.CharField(max_length=1000)

class Reviews(models.Model):
	review = models.CharField(max_length=1000)
	name = models.CharField(max_length=20)
	shop = models.ForiegnKey(Shop)
	
