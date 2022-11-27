from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import moviesinfo,Contact
from django.contrib import messages
from .serializers import movieapi
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import requires_csrf_token


#_____________________________________________________________#
@api_view(['GET'])                                            #                                                            
def apiread(request):                                         #
    info=moviesinfo.objects.all()                             #                
    serialize=movieapi(info,many=True)                        #                    
    return Response(serialize.data)                           #                
@api_view(['GET'])                                            #
def apireadone(request,id=0):                                 #    
    rec=moviesinfo.objects.filter(id=id)                      #                                
    serialize=movieapi(rec,many=True)                         #                    
    return Response(serialize.data)                           #                
@api_view(['GET'])                                            #
def readsearch(request,name=''):                              #        
    info=moviesinfo.objects.filter(name__icontains=name)      #                                    
    serialize=movieapi(info,many=True)                        #                    
    return Response(serialize.data)                           #                
@api_view(['GET'])                                            #
def searchyear(request,y=''):                                 #
    info=moviesinfo.objects.filter(release_year__icontains=y) #                                    
    serialize=movieapi(info,many=True)                        #                    
    return Response(serialize.data)                           #                
@api_view(['GET'])                                            #
def searchgerne(request,gerne=''):                            #
    info=moviesinfo.objects.filter(gerne__icontains=gerne)    #                                    
    serialize=movieapi(info,many=True)                        #                    
    return Response(serialize.data)                           #                
#_____________________________________________________________#



def home(request):
    info=moviesinfo.objects.all()
    context={
        'info':info
    }
    return render(request,'home.html',context)


def download(request,id=0):
    print(id)
    rec=moviesinfo.objects.filter(id=id).first()
    mrec={'rec':rec}
    return render(request,'download.html',mrec)

def search(request):
    if request.method == "POST":
        name=request.POST.get('name')
    print(name)
    info=moviesinfo.objects.filter(name__icontains=name)
    context={
        'info':info
    }
    return render(request,'home.html',context)


def gerne(request,gerne=''):
    info=moviesinfo.objects.filter(gerne__icontains=gerne)
    context={
        'info':info
    }
    return render(request,'home.html',context)


def release_year(request,y=''):
    info=moviesinfo.objects.filter(release_year__icontains=y)  
    context={
        'info':info
    }
    return render(request,'home.html',context)


@requires_csrf_token
def form(request,id=0):
    # print(id)
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        # print(name,'\n',email,'\n',desc)
        Contact(name=name, email=email, decs=desc).save()
        messages.success(request, 'Your message has been sent!')
    return redirect(download,id=id)