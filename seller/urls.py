
from django.urls import path
from . import views

app_name ='seller'

urlpatterns = [
	path('home/',views.home),
	path('add_property/',views.add_property),
	path('sellerde/<int:id>/',views.sellerde,name="sellerde"),
	path('chat_user/<int:id>/',views.chat,name="chat_user1"),
	# path('addmore22/',views.addmore22),
	# path('addmorepro/',views.addmorepro,name="addmorepro1"),
	path('seller_de/<int:id>/',views.seller_de,name="seller_de"),

		
]



