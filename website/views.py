from django.shortcuts import render
from ferias.forms import MarketplaceForm
from marketplaces.models import Marketplace
from django.db.models import Q
from django.contrib.gis.db.models.functions import Distance
#from geopy.geocoders import Nominatim
import requests

# Create your views here.


def index(request):

    r = requests.get('https://get.geojs.io/')
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    ipAdd = ip_request.json()['ip']
    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
    geo_request = requests.get(url)
    geo_data = geo_request.json()

    if request.method == "POST":
        # Search by location
        location = request.POST.get("location")
        print(location)
        print(geo_data['latitude'])
        print(geo_data['longitude'])
        print(geo_data['city'])
        print(geo_data['country'])

        '''
        if location != "any_location":
            marketplaces = Marketplace.objects.all().order_by("name")
        else:
            if location == "my_location":
                coordinates = (geo_data['latitude'], geo_data['longitude'])
            elif location == "some_location":
                # TODO: Get location from input with Nominatim
                #location = Nominatim(user_agent="GetLoc")
                #getLocation = location.geocode("Input usuario")
                #coordinates = (getLocation.latitude, getLocation.longitude)
                coordinates = (9.933364850202214, -84.07706364618377)        
            marketplaces = (
                Marketplace.objects.annotate(distance=Distance("location", coordinates)).order_by("distance")[0:3]
            )
        '''
        if location != "any_location":
            marketplaces = Marketplace.objects.all().order_by("name")
        elif location == "my_location":
            coordinates = (geo_data['latitude'], geo_data['longitude'])
            marketplaces = (
                Marketplace.objects.annotate(distance=Distance("location", coordinates)).order_by("distance")[0:3]
            )
        elif location == "some_location":
            #TODO: Get location from input with Nominatim
            #location = Nominatim(user_agent="GetLoc")
            #getLocation = location.geocode("Input usuario")
            #coordinates = (getLocation.latitude, getLocation.longitude)
            coordinates = (9.933364850202214, -84.07706364618377)        
            marketplaces = (
                Marketplace.objects.annotate(distance=Distance("location", coordinates)).order_by("distance")[0:3]
            )
        else:
            print("No hay ferias disponibles")
        # Search by schedule
        day = request.POST.get("day")
        print(day)
        marketplaces = marketplaces.filter(opening_hours__contains=day)
        # Search by amenities
        query = Q()
        fairground = request.POST.get("fairground")
        if fairground is not None:
            query &= Q(fairground=fairground)
        indoor = request.POST.get("indoor")
        if indoor is not None:
            query &= Q(indoor=indoor)
        marketplaces = marketplaces.filter(query)
        context = {
            "marketplaces": marketplaces,
        }
        return render(request, "index.html", context)
    else:
        return render(request, "index.html")


def acerca(request):
    return render(request, "acerca.html")


def contacto(request):
    return render(request, "contacto.html")
