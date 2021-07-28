from django.shortcuts import render, redirect
from .models import UserProile
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib import messages
from .models import contact_us
import requests
from seller.models import PropertyDetails



import json



def indian_property(request):
	pro1 = PropertyDetails.objects.all()
	return render(request,"indian_property.html",{'pro1':pro1,})


def admin_1(request):
	return render (request,"admin_1.html")


def admin_customer(request):
	uObj = User.objects.all()
	Uobj = UserProile.objects.all()



	return render(request,"Admin_Customer.html",{'data':uObj,'data_mob':Uobj})

def del_user(request,id):
	aObj = User.objects.get(id=id)
	Uobj = UserProile.objects.all()

	

	aObj.delete()
	return redirect('/admin_customer/')	


def contact_user(request):
	p1 = contact_us.objects.all()
	return render(request,"admin_1contactview.html",{'p1':p1})

def del_contact1(request,id):
	p1 = contact_us.objects.get(sno=id)
	p1.delete()
	return redirect('/contact1/')









def signup_user(request):

	if request.method == "POST":
		un = request.POST['uname']
		email = request.POST['email']
		mob = request.POST['mob']
		role = request.POST['role']
		pwd = request.POST['pwd']
		firstname= request.POST['firstname']
		lastname= request.POST['lastname']

		u = User(username=un, password=make_password(pwd), email=email,first_name=firstname,last_name=lastname)
		u.save()
		up = UserProile(user=u, mobile=mob, role=role)
		up.save()
		return redirect('/signup_user/')
	return render(request, "signup.html")


def login_user(request):
	if request.method == "POST":
		un = request.POST['uname']
		pwd = request.POST['pwd']
		user = authenticate(username=un, password=pwd)
		clientkey = request.POST['g-recaptcha-response']
		secretkey = "6LftjIgaAAAAADp0AeCKhecRLPyrNr-lzTuHF0tZ"


		capthchdata = {

			'secret':secretkey,
			'response':clientkey
		}
		r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=capthchdata)
		response=json.loads(r.text)
		verify = response['success']
		print('your success is:',verify)

		# if verify:
		# 	return HttpResponse('<script>alert("success")</script>')
		# else:
		# 	return HttpResponse('<script>alert("Wroong Again")</script>') 
			



		print(user)
		if user:


			login(request, user)
			if user.is_superuser:
				return redirect('/admin_1/')
			uObj = UserProile.objects.get(user__username=request.user)
			# uObj=User.objects.get(user__username=request.user)
			if uObj.role == "seller":

				return redirect('/seller/home/')
			elif uObj.role == "buyer":

				return redirect('/buyer/home/')
			# elif user.is_superuser:
			# 	return redirect('/admin_1/')
				
			return render(request,'index.html')
		else:
				# return HttpResponse("<h1>Invalid Username or Password</h1>")
				messages.error(request,"Invalid Username or Password")
				return render(request,"login.html")


	return render(request,"login.html",)

def logout_user(request):
	logout(request)	
	return redirect('/login_user/')





# def profile(request):
# 	return render(request,"profile.html")


def update(request):
	

	return render(request,"update_profile.html")



def contact(request):

	if request.method=='POST':
		#name=request.POST.get('nameuser',False)
		name=request.POST['nameuser']
		email=request.POST['email']
		phone=request.POST['phone']
		msg=request.POST['msg']
		print(name,email,phone,msg)
		pq=contact_us(name_user=name,phone=phone,email=email,contact=msg)
		pq.save()

		uObj = UserProile.objects.get(user__username=request.user)
		if uObj.role == "seller":
			return redirect ('/seller/home/')
		elif uObj.role == "buyer":

			return redirect('/buyer/home/')		


		
	#return render(request,"welseller.html")
