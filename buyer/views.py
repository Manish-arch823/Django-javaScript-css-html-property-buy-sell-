from django.shortcuts import render,redirect
from seller.models import PropertyDetails
from propertybuy.models import UserProile  
from django.contrib.auth.models import User
from .models import seller_detailes,Book,BookProperty
from django.db.models import Q
import random 
import datetime 



# Create your views here.

def home(request):
	user1 = UserProile.objects.get(user__username=request.user)
	pro1 = PropertyDetails.objects.all()
	ubj = User.objects.get(username=request.user)
	return render(request,"welcomeBuyer.html",{'user1':user1,'pro1':pro1,'ubj':ubj})




def seller_de(request,id):
	# user1 = UserProile.objects.get(user__username=request.user)

	# pObj=PropertyDetails.objects.filter(added_by_id=id)
	pObj=PropertyDetails.objects.filter(id=id)
	print(pObj)
	# uObj = UserProile.objects.get(user__username=request.user)
	# proObjs=PropertyDetails.objects.filter(user_id=uObj.id)
	# items = []


	# for i in details:
	# 	items.append(PropertyDetails.objects.get(id=i.PropertyDetails_id))
	# # print(items)

	return render(request,"buyer_detailes.html",{'pObj':pObj})
	
def profile1(request):
	upObj = UserProile.objects.filter(user__username=request.user)	
	uObj = User.objects.filter(username = request.user)
	# profi=profile.objects.filter(username = request.user)
	# if request.method == "post":
	# 	pimage = request.FIlES['pImage']
	# 	ar = profile(pro_image='pimage')
	# 	ar.save()
	# 	return redirect('/buyer/profile')
	
	return render(request,"buyer_profile.html",{'upObj':upObj,'uObj1':uObj})




def image(request):
	# uObj = UserProile.objects.get(user__username=request.user)
	# uObj1 = User.objects.get(username = request.user)



	if request.method =='POST':
		# print(uObj)
		ima=request.FILES['pImage']
		
		print(ima)
		uObj = UserProile.objects.get(user__username=request.user)
		proimg=profile(pro_img=ima,user_id=uObj)
		proimg.save()
	return render(request,"profile.html")











def update_pro(request):
	upObj = UserProile.objects.filter(user__username=request.user)	
	uObj = User.objects.filter(username = request.user)
	if request.method =='POST':
		first1=request.POST['firstname']
		last1=request.POST['lastname']
		email=request.POST['email']
		phone=request.POST['phone']
		#ima=request.FILES['pImage']
		# if profile.user_id == '':

		# 	profile.user_id = uObj
		current_user = request.user
		user_id =current_user.id
		print(user_id)




		#proimg=profile(pro_img=ima)
		#proimg.save()
		
		
		uObj.update(first_name=first1,last_name=last1,email=email)
		
		upObj.update(mobile=phone)
		return redirect('/buyer/profile1/')
	return render(request,"update_profile.html",{'upObj':upObj,'uObj':uObj})







def search(request):
	query = request.GET.get('keyword')
	print(query)
	result=PropertyDetails.objects.filter (Q(bhk__contains=query) | Q(price__contains=query))
	return render(request,"search.html",{'result':result})






def cart(request,id):
	pobj = UserProile.objects.get(user__username=request.user)
	uobj = PropertyDetails.objects.get(id=id)
	# try: 
	c=seller_detailes(user=pobj,seller=uobj)
	c.save()
		# messages.success(request,"Product added successfully")
	return redirect('/buyer/home/')
	# except:
	# 	messages.error(request,"Product already available in your cart")
	# 	return redirect('/buyer/home/')


def cartdetails(request):
	uobj = UserProile.objects.get(user__username=request.user)
	count = seller_detailes.objects.filter(user__id=uobj.id).count()
	cartobjs = seller_detailes.objects.filter(user__id=uobj.id)
	items = []
	for i in cartobjs:
		items.append(PropertyDetails.objects.get(id=i.seller_id))

	# uObj = UserProfile.objects.get(user__username = request.user)
	# add=AddressDetail.objects.filter(user_id=uobj.id)

	return render(request,"favra.html",{'cnt':count,'pobjs':items})

def cartdelete(request, id):
	uobj = UserProile.objects.get(user__username=request.user)
	pobj = PropertyDetails.objects.get(id=id)

	c = seller_detailes.objects.get(user=uobj, seller=pobj)
	c.delete()
	#Task: Confirmation
	return redirect('/buyer/cartdetails/')


def checkout(request):
	
	price = request.POST.getlist('price')
	pid = request.POST.getlist('pid')
	
	
	uObj = UserProile.objects.get(user__username=request.user)

	amount = 0

	# for i in range(len(pQty)):
	# 	#Task 1: Gen. Total Amount
	# 	amount = amount + (float(price[i])*int(pQty[i]))
	# 	# amountone = amount + (int(pQty[i])*float(price[i]))
	# 	# Task 2: Update Stock
	# 	pobj = Product.objects.filter(id=pid[i]) #QuerySet(pobj)
	# 	newQty = pobj[0].qty - int(pQty[i])
	# 	pobj.update(qty=newQty)
	
	# Orders(address=)
		
	cobjs = seller_detailes.objects.filter(user_id=uObj.id)
	cobjs.delete()

	order_id =orderCreation(price,uObj,pid)
	return redirect('/buyer/my_order/')

def orderCreation(price,uObj,pid):
	d=datetime.date.today()
	d2=str(d)
	d3=d2.replace('-','-')
	order_id = d3 + str( random.randint(10000, 99999))
	p=float(2000)


	Orders = Book(order_id=order_id,order_date=d2,total_amt=2000,amt_status=0,order_status=0,placedby=uObj)
	Orders.save()
	a=pid
	# b=int(pid)
	# c=str(a)
	# c1=c.replace('[',']')
	# c2=int(c1)
	# pobj = PropertyDetails.objects.get(id=c2)
	# for i in pid:
	# 	pobj = PropertyDetails.objects.get(id=pid[i])
	# 	BookPro=BookProperty(qty=0,status=0,order=Orders,product=pobj)
	# 	BookPro.save()
	# return order_id

def my_order(request):
	# cartobjs = Cart.objects.filter(user__id=uobj.id)
	# uobj = UserProfile.objects.get(user__username=request.user)
	

	# c = Cart.objects.get(user=uobj, product=pobj)
	# orbuyer=Orders.objects.get(placedby=uobj)
	# uobj = UserProfile.objects.get(user__username=request.user)
	# pObjs=Product.objects.filter(added_by=uobj.id)
	# obj = OrderProduct.objects.filter()
	# uobj=OrderProduct.objects.all()
	uObj = UserProile.objects.get(user__username = request.user)
	obj = Book.objects.filter(placedby_id=uObj.id)
	# orpro = OrderProduct.filter(id=obj.id)
	# add=AddressDetail.objects.filter(user_id=uObj.id)


	# pObjs=Product.objects.filter(obj.id)

	return render(request, "order_placed.html",{'Objs':obj})	




