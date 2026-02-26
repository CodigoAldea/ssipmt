from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("Hello, world! This is the home page of the appdev application.")
    
    return render(request, 'home.html') 