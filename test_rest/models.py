
from django.db import models
from django.contrib.gis.db import models 
import jsonfield
import datetime

# Create your models here.
class Geom(models.Model):
	id = models.IntegerField(primary_key = True)
	geom = jsonfield.JSONField()
	def __str__(self):
		return str(self.id)

class Geos(models.Model):
	id = models.IntegerField(primary_key = True)
	url = models.URLField(blank=True, default='DEFAULT VALUE', max_length=200)
	ID = models.CharField(max_length=10)
	name = models.CharField(max_length=200)
	m_type = models.CharField(max_length=50)
	geom = models.PolygonField(null=True, blank=True)
	created_at = models.DateTimeField(default=datetime.datetime.now)
	modified_at = models.DateTimeField(default=datetime.datetime.now)
	objects = models.GeoManager()
	def get_geom(self):
		return self.geom
	def get_url(self):
		return self.url
	def __str__(self):
		return self.name

class Geos_Multi(models.Model):
	id = models.IntegerField(primary_key = True)
	url = models.URLField(blank=True, default='DEFAULT VALUE', max_length=200)
	ID = models.CharField(max_length=10)
	name = models.CharField(max_length=200)
	m_type = models.CharField(max_length=50)
	geom = models.MultiPolygonField(srid=4326, null=True, blank=True)
	created_at = models.DateTimeField(default=datetime.datetime.now)
	modified_at = models.DateTimeField(default=datetime.datetime.now)
	objects = models.GeoManager()
	def get_geom(self):
		return self.geom
	def get_url(self):
		return self.url
	def __str__(self):
		return self.name

class User_geos(models.Model):
	id = models.IntegerField(primary_key = True)
	url = models.URLField(blank=True, default='DEFAULT VALUE', max_length=200)
	geo = models.URLField(blank=True, default='DEFAULT VALUE', max_length=200)
	user = models.IntegerField(default=0)
	user_url = models.URLField(blank=True, default='DEFAULT VALUE', max_length=200)
	created_at = models.DateTimeField(default=datetime.datetime.now)
	modified_at = models.DateTimeField(default=datetime.datetime.now)
	objects = models.GeoManager()
	def __str__(self):
		return str(self.user)

class User(models.Model):
	id = models.IntegerField(primary_key = True)
	age = models.IntegerField(null=True)
	gender = models.IntegerField()
	def __str__(self):
		return str(self.id)