from django.http import HttpResponse
from django.shortcuts import render
from models import Reviews,Shop,Forum,Comment
# Create your views here.

def addReview(request):
	name = request.POST['fullName']
	review = request.POST['review']
	print "Here is error"
	print request.POST['shop']
	s1 =  Shop.objects.filter(name = request.POST['shop'])[0]
	
	Reviews(review =review,name=name, shop=s1).save()
	return displayShops(request,s1)
    

def displayReviewForm(request):
	return render(request,'oldCity_app/review.html',{})

def displayShops(request,shop1):
	review_list = Reviews.objects.filter(shop=shop1)
	shop_list = Shop.objects.all()
	context = {'reviews':review_list, 'shops':shop_list,'pageShop':shop1}
	return render(request , 'oldCity_app/Shops.html',context)

def displayShopsMain(request):
	shop_list = Shop.objects.all()
	reviews = Reviews.objects.filter(shop = shop_list[0])
	context = {'reviews':reviews,'shops':shop_list,'pageShop':shop_list[0]}
	return render(request , 'oldCity_app/Shops.html',context)
	
def review(request):
	#return render
	pass

def removeReview(request):
	Shop.objects.filter(name=request.POST['review'])[0].delete()
	shop1 = Shop.objects.filter(name = request.POST['shop'])
	return displayShops(request,shop1)

def changeShop(request):
	shop = Shop.objects.filter(name=request.POST['shop'])[0]
	return displayShops(request,shop)
	
def addQuestion(request):
	question = request.POST['question']
	name = request.POST['fullName']
	Forum(name = name, question = question).save()
	return goToForum(request)
	
def addShop(request):
	name1 = request.POST['name']
	location = request.POST['location']
	description = request.POST['description']
	shop = Shop(name=name1,location=location,description=description)
	shop.save()
	return displayShops(request,shop)

def addComment(request):
	name = request.POST['name']
	comment = request.POST['comment']
	question = Forum.objects.filter(qid = request.POST['qid'])[0]
	Comment(name = name,comment=comment, question=question).save()
	return goToForum(request)

def ads(request):
	shops = [['Zahdeh', 'Soo2 il lahmeh','sells meat and fish'],['Abo Shukri','Pain road','Falafel and Humus Resturaunt'],['Salon Fadi Barbers Shop','Armanien quarter','Barber Shop'],['Abo ahmed','Pain road','sells fruit and vegtables']]

	for shop in shops:
		Shop(name = shop[0],location = shop[1],description = shop[2]).save()
	return HttpResponse("add those shops")

def goToForum(request):
	context = {'questions':Forum.objects.all(),'comments':Comment.objects.all()}
	return render(request,'oldCity_app/forum.html',context)

def goToTourists(request):
	return render(request,'oldCity_app/Tourists.html')

def goToOldCity(request):
	return render(request,'oldCity_app/old_city.html')

def goTocustomers(request):
	return render(request,'oldCity_app/customers.html')

def goToabout(request):
	return render(request,'oldCity_app/about.html')

def goToHotels(request):
	return render(request,'oldCity_app/Hotels.html')
	
def goToArche_Sites(request):
	return render(request,'oldCity_app/Arche.Sites.html')
	
def goToResturants(request):
	return render(request,'oldCity_app/Resturants.html')
