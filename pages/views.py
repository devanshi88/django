from django.shortcuts import render
from listings.models import listing
from listings.choices import state_choices,Prise_choices,bedroom_choices
# Create your views here.
def home(request):
	latest_listings=listing.objects.all()
	context={
	'latest_listings':latest_listings,
	'state_choices':state_choices,
	'Prise_choices':Prise_choices,
	'bedroom_choices':bedroom_choices,
	}
	return render(request,'pages/index.html',context)
def aboutus(request):
	return render(request,'pages/about.html')