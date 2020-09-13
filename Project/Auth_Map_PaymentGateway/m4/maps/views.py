from django.shortcuts import render

# Create your views here.

def gmap_map(request):
    #mapbox_access_Token = 'pk.eyJ1Ijoic2hpdmppbmRhbDc4IiwiYSI6ImNrZHBkajNhNTBoMXgycW8yYnJ6emsxMjYifQ.ebwYa-XBAX5HqTfmMOilVg'

    return render(request, "gmap.html", {})
#'mapbox_access_token' : mapbox_access_token