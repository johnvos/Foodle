from django.shortcuts import render

# Create your views here.
def showpage(req):
    return render(req, 'places/sampleRestaurantPage.html')
