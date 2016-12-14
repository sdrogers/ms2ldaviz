from django.db import models

from basicviz.models import Mass2Motif
# Create your models here.

class SubstituentTerm(models.Model):
	name = models.CharField(max_length = 128,null = False,unique = True)

	def __str__(self):
		return self.name
	def __unicode__(self):
		return self.name

class TaxaTerm(models.Model):
	name = models.CharField(max_length = 128,null = False,unique = True)

	def __str__(self):
		return self.name
	def __unicode__(self):
		return self.name



class SubstituentInstance(models.Model):
	subterm = models.ForeignKey(SubstituentTerm,null = False)
	motif = models.ForeignKey(Mass2Motif,null = False)
	probability = models.FloatField(null = False)

class TaxaInstance(models.Model):
	taxterm = models.ForeignKey(TaxaTerm,null = False)
	motif = models.ForeignKey(Mass2Motif,null = False)
	probability = models.FloatField(null = False)

