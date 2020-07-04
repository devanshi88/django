from django.db import models

# Create your models here.
class realtor(models.Model):
	Name = models.CharField(max_length=30)
	E_mail = models.EmailField(max_length=100)
	Contect = models.CharField(max_length=20)
	Image = models.ImageField(upload_to='Image')

	def __str__(self):
		return self.Name
