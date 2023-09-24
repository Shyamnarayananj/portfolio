from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    #return HttpResponse("this is my homepage(/)")
    context={"name":"shyam", "course": "django"}
    return render(request, "home.html", context)
def about(request):
    #return HttpResponse("this is my aboutpage(about/)")
    return render(request, "about.html")
def projects(request):
    #return HttpResponse("this is my projectspage(projects/)")
    return render(request, "projects.html")
def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
       # print(name,email,phone,desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("The data has been written to the DB")
    #return HttpResponse("this is my contactpage(conatact/)")
    return render(request, "contact.html")