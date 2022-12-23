from django.shortcuts import render,HttpResponse
from app.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone= request.POST.get('phone')
        contact= Contact(name=name,phone= phone)
        contact.save()


    return render(request,'contact.html')
def profile(request):
    return render(request,'profile.html')