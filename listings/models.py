import uuid
from django.db import models
from realtors.models import realtor
from datetime import datetime

# Create your models here.
class listing(models.Model):
	Realtor_Name= models.ForeignKey(realtor,on_delete=models.CASCADE)
	State = models.CharField(max_length=30)
	Pincoad =models.CharField(max_length=100)
	Price = models.FloatField(max_length=50)
	Published_Date = models.DateTimeField(default=datetime.now)
	Is_published = models.BooleanField(default=False)
	Plot_size = models.IntegerField()
	Cities = models.CharField(max_length=10, blank=True)
	Address = models.CharField(max_length=100)
	Bedrooms = models.IntegerField()
	bathrooms = models.IntegerField()
	parking = models.IntegerField()
	Enterance = models.IntegerField()
	Aditional_Details = models.TextField()
	Name_of_owener = models.CharField(max_length=30)
	#id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	Main_image = models.ImageField(upload_to='image')
	Optional_image1 = models.ImageField(upload_to='image',blank=True)
	Optional_image2 = models.ImageField(upload_to='image',blank=True)
	Optional_image3 = models.ImageField(upload_to='image',blank=True)
	Optional_image4 = models.ImageField(upload_to='image',blank=True)
	Optional_image5 = models.ImageField(upload_to='image',blank=True)

	#def __str__(self):
		#return self.



