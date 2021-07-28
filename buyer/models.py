from django.db import models
from propertybuy.models import UserProile
from seller.models import PropertyDetails
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class seller_detailes(models.Model):
	class Meta():
		unique_together = ('seller','user')

	seller = models.ForeignKey(PropertyDetails,on_delete=models.CASCADE)
	user = models.ForeignKey(UserProile,on_delete=models.CASCADE)
 
# class profile(models.Model):
# 	user = models.ForeignKey(UserProile, on_delete=models.CASCADE)
# 	# added_by=models.ForeignKey(UserProile,on_delete=models.CASCADE)
# 	pro_img = models.ImageField(upload_to="profileimage",null=True,default='default.svg')

	# def save( self, *args , **kwargs ):
	# 	super().save(*args,**kwargs)
	# 	img = Image.open(self.image.path)

	# 	if img.height > 300 or img.weight > 300 :
	# 		output_size =(300 ,300)
	# 		img.thumbnail(output_size)
	# 		img.save(self.image.path)

class Book(models.Model):
	order_id = models.CharField(max_length=100) #OD_16052021_RANDOMNUM
	order_date = models.DateTimeField(auto_now=True)
	total_amt = models.DecimalField(max_digits=10, decimal_places=3)
	amt_status = models.IntegerField(default=0) #0-->Unpaid
	order_status = models.IntegerField(default=0) #0-->Placed
	placedby = models.ForeignKey(UserProile, on_delete=models.CASCADE)
	# address = models.ForeignKey(AddressDetail, on_delete=models.CASCADE,blank=True)

class BookProperty(models.Model):
	order = models.ForeignKey(Book, on_delete=models.CASCADE)
	product = models.ForeignKey(PropertyDetails, on_delete=models.CASCADE)
	qty = models.IntegerField()
	status = models.IntegerField(default=0) #0->placeds

	





