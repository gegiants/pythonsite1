from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^hair_extentions', views.hair_extentions, name='hair_extentions'),
	url(r'^make_up', views.make_up, name='make_up'),
	url(r'^lashes_brows', views.lashes_brows, name='lashes_brows'),
	url(r'^nails', views.nails, name='nails'),
	url(r'^hairdressing', views.hairdressing, name='hairdressing'),
	url(r'^price_list', views.price_list, name='price_list'),
	url(r'^contact', views.contact, name='contact'),
	url(r'^paypal/', include('paypal.standard.ipn.urls')),
]

'''
pages
'''