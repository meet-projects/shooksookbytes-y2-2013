# Create your views here.
def addReview(request,addReview):
    Review(name=addReview[0], review=addReview[1], shop=addReview[2]).save()
def addShop(request, addShop):
    Shop(name=addShop[0], location=addShop[1], description=addShop[2]).save()
