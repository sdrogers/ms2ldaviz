from django.db import models

# Create your models here.
from basicviz.models import Feature,Experiment,Document,Mass2Motif

# Object to package up one decomposition event
class Decomposition(models.Model):
	name = models.CharField(max_length=128,unique=True)
	experiment = models.ForeignKey(Experiment)
	def __unicode__(self):
		return self.name + ' (' + self.experiment.name + ')'

# Package for a bunch of global features
class FeatureSet(models.Model):
	name = models.CharField(max_length=128,null = False,unique=True)
	description = models.CharField(max_length=1024,null = True)
	def __unicode__(self):
		return self.name

# A decomposition feature. These are shared across decompositions.
class GlobalFeature(models.Model):
	name = models.CharField(max_length=128,null=False)
	min_mz = models.FloatField(null = False)
	max_mz = models.FloatField(null = False)
	featureset = models.ForeignKey(FeatureSet)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name

# Stores the link between features here and those in basicviz
class FeatureMap(models.Model):
	globalfeature = models.ForeignKey(GlobalFeature,null = False)
	localfeature = models.ForeignKey(Feature,null = False)

# An instance of a feature in a document
class DecompositionFeatureInstance(models.Model):
	document = models.ForeignKey(Document,null = False)
	feature = models.ForeignKey(GlobalFeature,null = False)
	intensity = models.FloatField(null = False)

# A motif object here. Links to the original basicviz motif
class GlobalMotif(models.Model):
	originalmotif = models.ForeignKey(Mass2Motif,null = False)
	def get_name(self):
		return self.originalmotif.name
	def get_annotation(self):
		return self.originalmotif.annotation

	name = property(get_name) 
	annotation = property(get_annotation)


# Document <-> feature link here
class DocumentGlobalFeature(models.Model):
	document = models.ForeignKey(Document, null = False)
	feature = models.ForeignKey(GlobalFeature, null = False)
	intensity = models.FloatField(null = True)

class Beta(models.Model):
	experiment = models.ForeignKey(Experiment,unique=True)
	beta = models.TextField(null = True)
	motif_id_list = models.TextField(null = True)
	feature_id_list = models.TextField(null = True)
	alpha_list = models.TextField(null = True)

class DocumentGlobalMass2Motif(models.Model):
	document = models.ForeignKey(Document)
	mass2motif = models.ForeignKey(GlobalMotif)
	probability = models.FloatField(null = True)
	overlap_score = models.FloatField(null = True)

class DocumentFeatureMass2Motif(models.Model):
	docm2m = models.ForeignKey(DocumentGlobalMass2Motif)
	feature = models.ForeignKey(GlobalFeature)
	probability = models.FloatField(null = True)
	def get_original_mass2motif(self):
		return self.docm2m.mass2motif.originalmotif

	mass2motif = property(get_original_mass2motif)
