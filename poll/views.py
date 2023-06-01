from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from poll.models import color


x=''
rd=0
gr=0
bl=0

def test(request):

    global rd,gr,bl,val,x
    page = loader.get_template('poll.html')
    if(request.GET.get('color')=='red'):
        
        
        x = color.objects.all()[0]
        x.red = int(x.red)+1
        rd = x.red
        x.save()
    elif(request.GET.get('color')=='green'):
        
        x = color.objects.all()[0]
        x.green = int(x.green)+1
        gr = x.green
        x.save()
    elif(request.GET.get('color')=='blue'):
       
        x = color.objects.all()[0]
        x.yellow = int(x.yellow)+1
        bl = x.yellow
        x.save()

    context ={
        'rd':rd,
        'gr':gr,
        'bl':bl
    }
    print(request.GET)
    return HttpResponse(page.render(context,request))
    
# Create your views here.
