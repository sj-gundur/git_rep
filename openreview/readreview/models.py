from django.db import models

# Create your models here.
class movie(models.Model):
	title = models.CharField(max_length = 100)
	genre = models.CharField(max_length = 30)
	director = models.CharField(max_length = 30)
	rating = models.IntegerField()
	plot = models.TextField()
	reviewedOn = models.DateTimeField()
	
	def __unicode__(self):
		return self.title

class restaurant(models.Model):
	name = models.CharField(max_length = 30)
	location = models.CharField(max_length = 100)
	speciality = models.CharField(max_length = 50)
	rating = models.IntegerField()
	reviewedOn = models.DateTimeField()
	
	def __unicode__(self):
		rerutn ''.join([self.name,self.location])

#user comments model
class comments(models.Model):
	name = models.CharField(max_length=30)
	comments = models.CharField(max_length=100)
