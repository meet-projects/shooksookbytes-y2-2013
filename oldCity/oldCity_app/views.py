from django.http import HttpResponse
from django.shortcuts import render
from models import Reviews,Shop
# Create your views here.

def addReview(request):
	name = request.POST['fullName']
	review = request.POST['review']
	shop =  request.POST['shop']
	shop2 = Shop.objects.filter(name=shop)
	Reviews(review = review,name=name, shop=shop2[0]).save()
	return HttpResponse(name + review)
    

def displayReviewForm(request):
	return render(request,'oldCity_app/review.html',{})

def displayShops(request):
	review_list = Reviews.objects.all()
	context = {'reviews':review_list}
	return render(request , 'oldCity_app/Shops.html',context)
	
def review(request):
	#return render
	pass
	
def addShop(request):
	name = request.POST['name']
	location = request.POST['location']
	description = request.POST['description']
	Shop(name=name,location=location,description=description).save()
	return render(request , 'displayShops',{})
