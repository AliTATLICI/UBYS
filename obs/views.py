# -*- coding: utf-8 -*-
from django.http import *
from django.shortcuts import render
from obs.models import *

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from obs.serializers import UserSerializer, GroupSerializer, SnippetSerializer, ProgramSerializer


from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



# Api_views decaretörü, GET-POST vb. istekleri kontrol eder.
from rest_framework.decorators import api_view
# Response : İstekleri istemciye geri gönderir.
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer



def merhaba_dunya(request):
    return HttpResponse(u'Merhaba Dunya')

def post_list(request):
    return render(request, 'index.html', {})

def icerilen_sayfa(request):
    return render(request, 'dahil.html', {})

def get_deneme(request):
    if request.method=="GET":
        adi=request.GET['adi']
        soyadi=request.GET['soyadi']
        return HttpResponse(u'<b>Adı:</b> %s <br><b>Soyadı:</b> %s' %(adi, soyadi))


# Create your views here...

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    style = {'base_template': 'rest_test.html'}
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



####################


# GET ve POST istekleri dışında istek gelmeyecek. Gelsede dövecek :)
@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    Snippetleri listeler(GET) - Snippetleri kayıt eder(POST)
    """
    # GET isteği gelirse
    if request.method == 'GET':
        # Modeldeki verileri al
        snippets = Snippet.objects.all()
        # Serializer tarafından tarat
        serializer = SnippetSerializer(snippets, many=True)
        # Json olarak dönder.
        return Response(serializer.data)
    # Post isteği gelirse
    elif request.method == 'POST':
        # Gelen request.data'ı Serializer gönder, tarasın
        serializer = SnippetSerializer(data=request.data)
        # Eğer doğru data gelmişse
        if serializer.is_valid():
            # Snippet kaydet
            serializer.save()
            # Doğru data gelmediyse, snippeti kaydetme 201 http kodunu yansıt
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET - PUT - DELETE İsteklerini alacak.
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Güncelleme - silme ve görüntüleme işlemi yapar.
    """
    try:
        # Eğer gelen id veri tabanında var ise, değişkene depola
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        # Bu ide sahip veri yok ise 404 http kodunu göster
        return Response(status=status.HTTP_404_NOT_FOUND)
    # Get isteği gelirse
    if request.method == 'GET':
        # Aranan id'deki veriyi depola
        serializer = SnippetSerializer(snippet)
        # json olarak yolla
        return Response(serializer.data)
    #PUT İsteği gelirse
    elif request.method == 'PUT':
        # Gelen detayı serializer tarafından tarattır
        serializer = SnippetSerializer(snippet, data=request.data)
        # Gelen data doğru ise
        if serializer.is_valid():
            # Snippet'i kaydet
            serializer.save()
            # Oluşan çıktıyı geri dönder
            return Response(serializer.data)
        # Eğer gelen data doğru değilde, 400 http kodunu yansıt
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Eğer Delete isteği gelirse
    elif request.method == 'DELETE':
        # İstekte bulunan id sahip veriyi sil.
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


####SINIF TABANLI GÖRÜNÜM###

class SnippetList(APIView):

    """
    Snippet modelini listeleyip, post metodu ile veri eklemeye yarar.
    """

    # Get metodu kontrol ediliyor.
    def get(self, request, format=None):
        # Model deki veriler, listeye aktarılıyor.
        snippets = Snippet.objects.all()
        # Serizalizer tarafından, kontrol ediliyor.
        serializer = SnippetSerializer(snippets, many=True)
        # Sonuç yollanıyor.
        return Response(serializer.data)

    # Post metodu kontrol ediliyor.
    def post(self, request, format=None):
        # Serializer tarafından, gelen data kontrol ediliyor.
        serializer = SnippetSerializer(data=request.data)
        # data uygun ise
        if serializer.is_valid():
            # ftfyıt ediyor.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    SnippetDetail fonksiyonu ile ;
    id göre listeleme, put metodu ile kaydetme , delete metodu ile silme işlemi yapılmaktadır.
    """

    # pk : gelen id isteği
    def get_object(self, pk):
        try:
            # gelen id, modelde aranıyor.
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            # eğer yoksa ise, 404
            raise Http404

    # get isteği gelirse, id' göre veriler listelenir.
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    # put metodu gelirse, data uygunsa kayıt edilir.
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete metodu ile, istekte bulunan id silinir.
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



######
class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'rest_test.html'

    def get(self, request):
        queryset = Snippet.objects.all()
        return Response({'profiles': queryset})


#####
class Fakulte_MYOList(APIView):

    """
    Snippet modelini listeleyip, post metodu ile veri eklemeye yarar.
    """

    # Get metodu kontrol ediliyor.
    def get(self, request, format=None):
        # Model deki veriler, listeye aktarılıyor.
        snippets = Program.objects.all()
        # Serizalizer tarafından, kontrol ediliyor.
        serializer = ProgramSerializer(snippets, many=True)
        # Sonuç yollanıyor.
        return Response(serializer.data)

    # Post metodu kontrol ediliyor.
    def post(self, request, format=None):
        # Serializer tarafından, gelen data kontrol ediliyor.
        serializer = Fakulte_MYOSerializer(data=request.data)
        # data uygun ise
        if serializer.is_valid():
            # ftfyıt ediyor.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
