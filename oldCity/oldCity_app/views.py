
# Create your views here.
def addReview(request):
	name = request.POST['fullName']
	review = request.POST['review']
	
    return HttpResponseRedirect()
    
def addShop(request, addShop):
    Shop(name=addShop[0], location=addShop[1], description=addShop[2]).save()


	
def review(request):
	return render
