from django.conf.urls import patterns, include, url
from oldCity_app import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^review$',views.addReview, name='addReview'),
    url(r'^shops/shop$',views.addShop, name='addShop'),
    url(r'^displayReview$',views.displayReviewForm),
    url(r'^displayShops$',views.displayShopsMain),
    url(r'^shop$',views.addShop),
    url(r'^review$',views.addReview),
    url(r'^Tourists$',views.goToTourists),
    url(r'^$',views.goToOldCity),
    url(r'^customers$',views.goTocustomers),
    url(r'^About$',views.goToabout),
    url(r'^changeShop',views.changeShop),
    url(r'^Hotels$',views.goToHotels),
    url(r'^Arche_Sites$',views.goToArche_Sites),
    url(r'^Resturants$',views.goToResturants),
    url(r'^Shops$',views.displayShopsMain),
    url(r'^displayForum',views.goToForum),
    url(r'^addQuestion',views.addQuestion),
    url(r'^addComment',views.addComment),
    url(r'^removeReview',views.removeReview),
    url(r'^ads',views.ads),
	url(r'^map',views.goToMap),

    # Examples:
    # url(r'^$', 'oldCity.views.home', name='home'),
    # url(r'^oldCity/', include('oldCity.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
