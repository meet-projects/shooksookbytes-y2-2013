from django.db import models



# Create your models here.
class Shop(models.Model):
	name = models.CharField(max_length=20)
	location = models.CharField(max_length=40)
	description = models.CharField(max_length=1000)

class Reviews(models.Model):
	review = models.CharField(max_length=1000)
	name = models.CharField(max_length=20)
	shop = models.ForeignKey('Shop')
	def __unicode__(self):
		return self.name
	
class Forum(models.Model): 
	question = models.CharField(max_length=1000)
	name = 	models.CharField(max_length=20)
	qid = models.AutoField(primary_key=True)

class Comment(models.Model):
	question = models.ForeignKey('Forum')
	name = models.CharField(max_length=20)
	comment = models.CharField(max_length=1000)
	
	
