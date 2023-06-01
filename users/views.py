from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from users.models import register


def reg(request):
    global fet
    name = request.GET.get('name')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    username = request.GET.get('username')
    password = request.GET.get('password')
    country = request.GET.get('country')
    temp = loader.get_template('reg.html')
    
    #x = register(name=name,email=email,phone=phone,username=username,password=password,country=country)
    #x.save()
    con={}
    #print(name+" "+phone+" "+password+" "+username+" "+country)
    #print(request.GET)
    return HttpResponse(temp.render(con,request))

def login(request):
    global name,email,phone,username,password,country
    temp = loader.get_template('login.html')
    con={}
    
    name = request.GET.get('name')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    username = request.GET.get('username')
    password = request.GET.get('password')
    country = request.GET.get('country')
    fet=0
    
    username = request.GET.get('username')
    password = request.GET.get('password') 
    for i in  len(register.objects.all().values()):
        if(username==register.objects.all()['username'] and password==register.objects.all()['password']):
            print("Accepted User")
        else:
            print("prevented")
            break




    return HttpResponse(temp.render(con,request))
    

# Create your views here.
