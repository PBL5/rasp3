#  from django.shortcuts import render
from django.http.response import FileResponse
from rest_framework import generics
from rest_framework.response import Response
import cv2
import os

# Create your views here.
class PictureAPIView(generics.GenericAPIView):
    def get(self, request):
        current_path = str(os.path.abspath(os.getcwd()))
        img = open('blackpink.jpg', 'rb')
        return FileResponse(img)
