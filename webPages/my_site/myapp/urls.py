from django.urls import path 
from . import views
#from myapp import views
from myapp import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('homepage/',views.homepage,name='homepage'),
    path('display_date/',views.display_date,name='display_date'),
    path('',views.index,name='index'),
    path('cart/',views.cart,name='cart'),
    path('product/',views.product,name='products'),
    path('checkout/',views.checkout,name='checkout'),
    path('showform/',views.showform, name='showform'),
    path('getform/',views.getform,name='getform'),
    path('menuitems/<str:dish>',views.menuitems, name='menuitems')

]