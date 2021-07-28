from django.db import models 
from django.contrib.auth.models import User


class UserProile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role =models.CharField(max_length=20)
	mobile = models.CharField(max_length=20)
	Con_password = models.CharField(max_length=50)
	


class contact_us(models.Model):
	sno = models.AutoField(primary_key=True)
	name_user=models.CharField(max_length=255)
	phone=models.CharField(max_length=13)
	email=models.CharField(max_length=100)
	contact=models.TextField()
	time=models.DateTimeField(auto_now_add=True,blank=True)



	def __str__(self):
		return '  Message  From_____ ' + self.name_user  +'____Email-id____  '+    self.email



# class cheat(models.Model):
# 	Message=models.TextField()
# 	user=models.ForeignKey(User, on_delete=models.CASCADE)
# 	Seller=models.ForeignKey(PropertyDetails,on_delete=models.CASCADE)
