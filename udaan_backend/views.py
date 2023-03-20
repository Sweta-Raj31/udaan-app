from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from .models import *
from rest_framework.response import Response
from .serializer import *



class ReactView(APIView):
    serializer_class = CreateMessageSerializer
    
            
    def post(self,request):
        serializer = CreateMessageSerializer(data=request.data)
        # add emailvalidator
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
class ContentView(APIView):
    serializer_class = CreateContentSerializer
    
            
    def post(self,request):
        serializer = CreateContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# Create your views here.
