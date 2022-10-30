from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import moviesinfo
from django.contrib import messages
from .serializers import movieapi
from rest_framework.decorators import api_view
from rest_framework.response import Response



#_____________________________________________________________#
@api_view(['GET'])                                            #                                                            
def read(request):                                            #
    info=moviesinfo.objects.all()                             #                
    serialize=movieapi(info,many=True)                        #                    
    return Response(serialize.data)                           #                
@api_view(['GET'])                                            #
def readone(request):                                         #    
    rec=moviesinfo.objects.filter(id=id).first()              #                                
    serialize=movieapi(rec,many=True)                         #                    
    return Response(serialize.data)                           #                
@api_view(['GET'])                                            #
def readsearch(request,name=''):                              #        
    info=moviesinfo.objects.filter(name__icontains=name)      #                                    
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