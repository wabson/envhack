from django.db import models

# Create your models here

class HistoricIncident(models.Model):
	not_id = models.CharField(max_length=30)
	not_date = models.CharField(max_length=20)
	region_wm  = models.CharField(max_length=20)
	area_wm = models.CharField(max_length=30)
	region_pf = models.CharField(max_length=20)
	area_pf = models.CharField(max_length=50)
	county = models.CharField(max_length=50) 
	unitary = models.CharField(max_length=200)
	district = models.CharField(max_length=50) 
	ngr_conf = models.CharField(max_length=50)
	x_conf = models.CharField(max_length=30)
	y_conf = models.CharField(max_length=30)
	ep_inc = models.CharField(max_length=30)
	eil_air = models.CharField(max_length=60)
	eil_land = models.CharField(max_length=60)
	eil_water = models.CharField(max_length=60)

class HistoricPollutant(models.Model):
	not_id = models.IntegerField()
	poll_type = models.CharField(max_length=50)
	pollutant = models.CharField(max_length=50)
