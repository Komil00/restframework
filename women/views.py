from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Women
from .serializers import WomenSerializers

# Create your views here.
class WomenAPIView(APIView):
    def get(self, request):
        return Response({'title': 'Angeline Jelie'})


# class WomenAPIView(generics.ListAPIView):
# 	queryset = Women.objects.all()
# 	serializer_class = WomenSerializers


		