#  from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from PIL import Image


# Create your views here.
class PictureAPIView(generics.GenericAPIView):
    def get(self, request):
        img = Image.open('blackpink.jpg')
        print(img)
        return Response()
