from django.conf.urls import patterns, include, url
from oldCity_app import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^review$',views.addReview, name='addReview'),
    url(r'^shops/shop$',views.addShop, name='addShop'),
    url(r'^displayReview$',views.displayReviewForm),
    url(r'^displayShops$',views.displayShops),
    url(r'^shop$',views.addShop),
    url(r'^review$',views.addReview),
    url(r'^tourists$',views.goToTourists),
    url(r'^oldCity$',views.goToOldCity),
    # Examples:
    # url(r'^$', 'oldCity.views.home', name='home'),
    # url(r'^oldCity/', include('oldCity.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
