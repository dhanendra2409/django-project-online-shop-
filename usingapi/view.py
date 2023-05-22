from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from .models import Product_View
from .serializer import ProductSerializer



# Create your views here.
@api_view(['GET'])
def getproduct(request):
    product=Product_View.objects.all()
    serializer=ProductSerializer(product,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postproduct(request):
    serializer=ProductSerializer(data=request.data) 
    if serializer.is_valid():
         serializer.save()
    return Response(serializer.data)    


      