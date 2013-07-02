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

def displayShops(request,shop):
	review_list = Reviews.objects.filter(shop=shop)
	context = {'reviews':review_list}
	return render(request , 'oldCity_app/Shops.html',context)

def displayShopsMain(request):
	context = {'reviews':'noReview'}
	return render(request , 'oldCity_app/Shops.html',context)
	
def review(request):
	#return render
	pass

def changeShop(request):
	shop = request.POST['shop']
	return displayShops(request,shop)
	
def addShop(request):
	name = request.POST['name']
	location = request.POST['location']
	description = request.POST['description']
	Shop(name=name,location=location,description=description).save()
	return displayShops(request,Shop.objects.filter(name=name))

def goToTourists(request):
	return render(request,'oldCity_app/Tourists.html')

def goToOldCity(request):
	return render(request,'oldCity_app/old_city.html')

def goTocustomers(request):
	return render(request,'oldCity_app/customers.html')

def goToabout(request):
	return render(request,'oldCity_app/about.html')

def goToshopkeepers(request):
	return render(request,'oldCity_app/Shopkeepers.html')

def goToHotels(request):
	return render(request,'oldCity_app/Hotels.html')
	
def goToArche_Sites(request):
	return render(request,'oldCity_app/Arche.Sites.html')
	
def goToResturants(request):
	return render(request,'oldCity_app/Resturants.html')
	
def goToShops(request):
	return render(request,'oldCity_app/Shops.html')
