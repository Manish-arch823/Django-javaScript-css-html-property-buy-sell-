from django.db import models
from propertybuy.models import UserProile
from django.contrib.auth.models import User


# Create your models here.
class PropertyDetails(models.Model):
	name = models.CharField(max_length=40)
	about = models.CharField(max_length=250)
	pro_img = models.ImageField(upload_to="propertyimage",blank=True,)
	pro_img2=models.ImageField(upload_to="propertyimage",blank=True,default="0" )
	pro_img3=models.ImageField(upload_to="propertyimage",blank=True,default="0" )
	pro_img4=models.ImageField(upload_to="propertyimage",blank=True,default="0" )
	pro_img5=models.ImageField(upload_to="propertyimage",blank=True,default="0" )
	state = models.CharField(max_length=100)
	city = models.CharField(max_length=50,blank=True)
	added_by=models.ForeignKey(UserProile,on_delete=models.CASCADE)
	full_address = models.CharField(max_length=200)
	pincode=models.IntegerField()
	bhk=models.CharField(max_length=40)
	price=models.CharField(max_length=40) 
	date = models.DateTimeField(auto_now=True)
	pro_type = models.CharField(max_length=20)
	mobile = models.CharField(max_length=20) 
	bookPrice=models.CharField(max_length=20,default="2000.00" )


class addmorePro(models.Model):
	propertyimage = models.ForeignKey(PropertyDetails, on_delete=models.CASCADE)
	pro_img2=models.ImageField(upload_to="propertyimage",blank=True)
	pro_img3=models.ImageField(upload_to="propertyimage",blank=True)
	pro_img4=models.ImageField(upload_to="propertyimage",blank=True)
	pro_img5=models.ImageField(upload_to="propertyimage",blank=True)
	






class chat(models.Model):
	Message=models.TextField()
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	Seller=models.ForeignKey(PropertyDetails,on_delete=models.CASCADE)






