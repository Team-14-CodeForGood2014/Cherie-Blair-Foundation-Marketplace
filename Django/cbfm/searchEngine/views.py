from django.shortcuts import render
from urlparse import urlparse, parse_qs

import scripts

# Create your views here.
from django.http import HttpResponse

def results(request):

    #Find Query string

#    requestParse = urlparse.parse_qs(request)
    quantity = request.GET['quantity']
    units = request.GET['units']
    keywords = request.GET['keywords']
    region = request.GET['region']
    
    return HttpResponse(scripts.main(quantity,units,keywords,region)))
