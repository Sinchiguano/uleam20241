from django.shortcuts import render

# Create your views here.

from datetime import datetime

from django.http import HttpResponse
def home(request):
    return HttpResponse('Hello, world from myapp')

def homepage(request):
    return HttpResponse("WELCOME TO LITTLE LEMON!")

def display_date(request):
    dateContainer=datetime.today().year
    return HttpResponse(dateContainer)

def index(request):
    return render(request,'myapp/index.html')

def product(request):
    return render(request,'myapp/products.html')

def cart(request):
    return render(request,'myapp/cart.html')

def checkout(request):
    return render(request,'myapp/checkout.html')

def showform(request):
    return render (request,'myapp/form.html')

def getform(request):
    if request.method=="POST":
        id=request.POST['id']
        name=request.POST['name']
    return HttpResponse(f"Name: {id} User ID:{name}")
    # pass

def menuitems(request,dish):
    items={'pasta':'pasta is a type of noodle.',
           'cheesecake':'it is a type of dessert.'}       
    description=items[dish]     
    return HttpResponse(f"<h2> { dish} </h2> <h1>{description}</h1>")



# def getform(request): 
#     if request.method == "POST": 
#         id=request.POST['id'] 
#         name=request.POST['name'] 
#     return HttpResponse("Name:{} UserID:{}".format(name, id)) 


# from django.shortcuts import render
# def myview(request):
#     if request.method=='GET':
#         #PERFORM READ OR DELETE OPERATION ON THE MODEL
#     if request.method=='POST':
#         #PERFORM INSERT OR UPDATE OPERATION ON THE MODELS
#         context={}
#     return render(request, 'mytemplate.html',context)
#     pass


# from django.views import View
# class MyView(View):
#     def get(self, request):
#         return HttpResponse('response to GET request')
#     def post(self,request):
#         return HttpResponse('response to POST request')
        



# def myview(request):
#     if request.method=='GET':
#         val=request.GET['key']
#         #PERFORM READ OR DELETE OPERATION ON THE MODEL
#     if request.method=='POST':
#         #PERFORM INSERT OR UPDATE OPERATION ON THE MODELS
#         val=request.POST['key']
#     pass