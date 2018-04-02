from django.shortcuts import render

from django.http import HttpResponse
#from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from . import models
from . import serializers

class Birim(generics.ListCreateAPIView):
    queryset = models.Birim.objects.all()
    #permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.BirimSerializer

class Personel(generics.ListCreateAPIView):
    queryset = models.Personel.objects.all()
    #permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.PersonelSerializer