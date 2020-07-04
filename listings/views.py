from django.shortcuts import render,get_object_or_404
from .models import listing
from django.core.paginator import Paginator
from listings.choices import state_choices,Prise_choices,bedroom_choices

# Create your views here.
def listings(request): 
	listings=listing.objects.all()
	paginator=Paginator(listings,3)
	page=request.GET.get('page')
	listing_per_page= paginator.get_page(page)
	context={
	'listings':listings
	}
	return render(request,'listings/listings.html',context)
	
def Listing(request,id):
	Listing=get_object_or_404(listing,pk=id)
	context={ 
	'listing':Listing
	}
	return render(request,'listings/listing.html',context)

def search(request):
	listings=listing.objects.order_by('-Published_Date')
	if 'keywords' in request.GET:
		keywords=request.GET['keywords']
		if keywords:
			listings=listings.filter(Aditional_Details__icontains=keywords)

	if 'city' in request.GET:
		city=request.GET['city']
		if city:
			listings=listings.filter(Cities__iexact=city)

	if 'state' in request.GET:
		state=request.GET['state']
		if state:
			listings=listings.filter(State__iexact=state)


	if 'badrooms' in request.GET:
		badrooms=request.GET['badrooms']
		if badrooms:
			listings=listings.filter(Bedrooms__lte=badrooms)

	if 'price' in request.GET:
		price=request.GET['price']
		if price:
			listings=listings.filter(Price__lte=price)
	context={
	'listings':listings,
	'state_choices':state_choices,
	'Prise_choices':Prise_choices,
	'bedroom_choices':bedroom_choices,
	'values':request.GET  
	}
	return render(request,'listings/search.html',context)

	
