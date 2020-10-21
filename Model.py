
from django.db import models


class EcoFlush_Model(models.Model):
	b8100 = models.CharField(max_length=6)
	b8104 = models.CharField(max_length=6)
	b8106 = models.CharField(max_length=6)
	b8106s = models.CharField(max_length=6)
	def __str__(self):
	    return self.b8100

class Issue(models.Model):
	no_flush = models.CharField(max_length=100)
	def __str__(self):
	    return self.no_flush

class Troubleshoot(models.Model):
	manuel_flush = models.ForeignKey(Issue, on_delete=models.CASCADE)
	issue_type = models.CharField(max_length=200)
	def __str__(self):
	    return self.issue_type
      
 class Part(models.Model):
  
	
# Create your models here.




-----------------------------------


from django.db import models


class EcoFlush_Model(models.Model):
	b8100 = models.CharField(max_length=6)
	b8104 = models.CharField(max_length=6)
	b8106 = models.CharField(max_length=6)
	b8106s = models.CharField(max_length=6)
	def __str__(self):
	    return self.b8100

class Issue(models.Model):
	no_flush = models.CharField(max_length=100)
	def __str__(self):
	    return self.no_flush

class Troubleshoot(models.Model):
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
	issue_type = models.CharField(max_length=200)
	def __str__(self):
	    return self.issue_type
	
# Create your models here.
