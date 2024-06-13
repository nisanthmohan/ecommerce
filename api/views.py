from django.shortcuts import render
from rest_framework.views import APIView
from api.serializer import signup
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from api.serializer import productserializers
from store.models import Productmod
from rest_framework import status
# Create your views here.

class signupview(APIView):
    def post(self,request,*args,**kwargs):
        serializer=signup(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class taskviewset(ViewSet):
    def list(self,request,*args,**kwargs):
        data=Productmod.objects.all()
        serializers=productserializers(data,many=True)
        return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
    
    def create(self,request,*args,**kwargs):
        serializers=productserializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_404_NOT_FOUND)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Productmod.objects.get(id=id)
        serializers=productserializers(qs)
        return Response(data=serializers.data,status=status.HTTP_202_ACCEPTED)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Productmod.objects.get(id=id)
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Productmod.objects.get(id=id)
        serializers=productserializers(data=request.data,instance=qs)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data,status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(data=serializers.errors,status=status.HTTP_404_NOT_FOUND)
        