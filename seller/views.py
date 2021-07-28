from django.shortcuts import render,redirect
from propertybuy.models import UserProile
from .models import PropertyDetails,addmorePro
from django.contrib.auth.models import User
from .models import chat
# Create your views here.

def home(request):
	uObj = UserProile.objects.get(user__username=request.user)
	ubj = User.objects.get(username=request.user)
	pro1 = PropertyDetails.objects.all()
	
	return render(request,"welseller.html",{'data':uObj,'pro1':pro1,'ubj':ubj})

	

def add_property(request):
	if request.method == "POST":
		name = request.POST['name']
		
		pImage= request.FILES['pImage']
		pImage2=request.FILES['pImage2']
		pImage3=request.FILES['pImage3']
		pImage4=request.FILES['pImage4']
		pImage5=request.FILES['pImage5']
		state = request.POST['state']
		city = request.POST['city']
		

		full_address = request.POST['full_address']
		pincode = request.POST['pincode']
		bhk = request.POST['bhk']
		price=request.POST['price']
		pro_type = request.POST['role'] 
		mobile= request.POST['mobile']

		uObj = UserProile.objects.get(user__username=request.user)
		ar=PropertyDetails(name=name,pro_img=pImage,state=state,full_address=full_address,pincode=pincode,
			bhk=bhk,price=price,mobile=mobile,city=city,pro_type=pro_type,added_by=uObj,pro_img2=pImage2,pro_img3=pImage3,pro_img4=pImage4,pro_img5= pImage5   )
		ar.save()
		# try:
		# 	myFile = request.FILES['pImage']
		# except MultiValueDictKeyError:
		# 	print("Error")
		# 	myFile="none"

		return redirect('/seller/add_property/')

	return render(request,"addproperty.html",)

# def addmore22(request):
# 	pid = request.POST.getlist('pid')
# 	# pro_more = addmorepro(pid)

# 	return render(request,"order_placed.html",)


# def addmorepro(request):
# 	if request.method == "POST":
# 		f1=request.FILES['img1']
# 		f2=request.FILES['img2']
# 		f3=request.FILES['img3']
# 		f4=request.FILES['img4']
		
# 		print(f5)	
# 		# uObj=add_property.objects.get(user__userid=request.user) 
# 		# uObj = UserProile.objects.get(user__username=request.user)
# 		# obj=PropertyDetails.objects.filter(added_by_id=request.user)
# 		# pObj=PropertyDetails.objects.filter(id=pid)

		

# 		pObj=addmorePro(pro_img2=f1,pro_img3=f2,pro_img4=f3,pro_img5=f4,propertyimage=pObj)
# 		pObj.save()
# 		return redirect("/seller/home/")
# 	return render(request,"welseller.html")


 	

def sellerde(request):
	pid = request.POST.getlist('pid')
	upObj = UserProile.objects.filter(user__username=request.user)	
	# user1 = User.objects.filter(user__id=request.id)
	uObj = UserProile.objects.get(user__username=request.user)
	pObj=PropertyDetails.objects.filter(user__username=request.user)
	# return render(request,"seller_detailes.html",{'pObj':pObj})

	return render(request,"welseller.html",{'pObj':pObj})



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

	return render(request,"seller_detailes.html",{'pObj':pObj})

def chat_user(request,id):
	pobj=PropertyDetails.objects.get(id=id)
	upObj = UserProile.objects.get(user__username=request.user)	
	if request.method == 'POST':
		msg=request.POST['message']
		print(msg)
	
		ch=chat(Message=msg,user=upObj,Seller=pobj)
		

		ch.save()

		return redirect('/chat_user/')











