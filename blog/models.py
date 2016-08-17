from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title		
		
# Hair Extentions/Prices.
			
class Weave(models.Model):
	type = models.CharField(max_length=200,primary_key=True)
	description = models.TextField()
	
	def __str__(self):
		return self.type
		
class Weave_Price(models.Model):
	disc = models.CharField(max_length=200)
	weave = models.ForeignKey(Weave, on_delete=models.CASCADE)	
	price = models.IntegerField()
	
	def __str__(self):
		return "%s - %s" % (self.weave, self.disc)
		
class KeratinBond(models.Model):
	type = models.CharField(max_length=200,primary_key=True)
	description = models.TextField()
	
	def __str__(self):
		return self.type

class KeratinBond_Price(models.Model):
	disc = models.CharField(max_length=200)
	weave = models.ForeignKey(Weave, on_delete=models.CASCADE)	
	price = models.IntegerField()
	
	def __str__(self):
		return "%s - %s" % (self.weave, self.disc)		
				
class MicroRing(models.Model):
	type = models.CharField(max_length=200,primary_key=True)
	description = models.TextField()
	
	def __str__(self):
		return self.type

class MicroRing_Price(models.Model):
	disc = models.CharField(max_length=200)
	microRing = models.ForeignKey(MicroRing, on_delete=models.CASCADE)	
	price = models.IntegerField()

	def __str__(self):
		return "%s - %s" % (self.microRing, self.disc)
		
class TapedHairExtention(models.Model):
	type = models.CharField(max_length=200,primary_key=True)
	description = models.TextField()
	
	def __str__(self):
		return self.type
		
class TapedHairExtention_Price(models.Model):
	disc = models.CharField(max_length=200)
	weave = models.ForeignKey(Weave, on_delete=models.CASCADE)	
	price = models.IntegerField()
	
	def __str__(self):
		return "%s - %s" % (self.weave, self.disc)
		
class MakeUp(models.Model):
	type = models.CharField(max_length=200,primary_key=True)
	description = models.TextField()
	
	def __str__(self):
		return self.type	
		
class Lash_Brow(models.Model):
	type = models.CharField(max_length=200,primary_key=True)
	description = models.TextField()
	
	def __str__(self):
		return self.type		

class Nail(models.Model):
	type = models.CharField(max_length=200,primary_key=True)
	description = models.TextField()
	
	def __str__(self):
		return self.type	

class Hairdressing(models.Model):
	type = models.CharField(max_length=200,primary_key=True)
	description = models.TextField()
	
	def __str__(self):
		return self.type		
		
class Pricee(models.Model):
	type = models.CharField(max_length=200)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	price = models.IntegerField()
	
	def __str__(self):
		return self.type		


		
		
# Create your models here.
