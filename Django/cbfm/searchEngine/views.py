from django.shortcuts import render
from urlparse import urlparse, parse_qs

import scripts

# Create your views here.
from django.http import HttpResponse

def results(request):

    #Find Query string

    quantity = request.GET['quantity']
    units = request.GET['units']
    keywords = request.GET['keywords']
    region = request.GET['region']
    usertype = request.GET['usertype']

    quantity = str(quantity).lower()
    units = str(units).lower()
    keywords = str(keywords).lower()
    region = str(region).lower()
    usertype = str(usertype).lower()
    
    return HttpResponse(scripts.search(quantity, units, keywords, region, usertype))

