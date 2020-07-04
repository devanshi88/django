from django.urls import path
from.import views
urlpatterns = [
    path('',views.listings,name='listings'),
    path('<int:id>',views.Listing,name='listing'),
    path('search/',views.search,name='search')


]
