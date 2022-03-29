from datetime import datetime
from django.shortcuts import render
from app1.models import Contact

# Create your views here.
def index(request):
   #return HttpResponse("This is Home page")
   return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
   #return HttpResponse("This is About page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
        name=request.post.get('name')
        email=request.post.get('email')
        phone=request.post.get('phone')
        desc=request.post.get('desc')
        
        contact = Contact(name=name, email=email ,phone=phone ,desc=desc ,date=datetime.today())
        contact.save()
        
    return render(request, 'contact.html')
    