from django.urls import path
from . import views

app_name='buyer'



urlpatterns = [
	path('home/',views.home),
	path('seller_de/<int:id>/',views.seller_de,name="seller_de"),
	path('profile1/',views.profile1),
	path('update/',views.update_pro),
	path('search/',views.search,name="search"),
	path('image/',views.image,name="image"),
	path('cart/<int:id>/',views.cart,name="cart"),
	path('cartdetails/',views.cartdetails),
	path('cartdelete/<int:id>/', views.cartdelete, name="cartdel"),
	path('checkout/', views.checkout),
	path('my_order/',views.my_order,name="my_order"),
	# path('/',views.,name=""),

	
	
	# path('profile_user/',views.profile_user),
	# path('sell_details/<int:id>/',views.sell_details,name='seller_details'),
	#<a href="{% url 'buyer:seller_de' id=i.id %}"
		
]