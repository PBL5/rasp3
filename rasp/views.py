#  from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.
class PictureAPIView(generics.GenericAPIView):
    def get(self, request):
        return Response()
