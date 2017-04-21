from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Program

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


#########################3


class SnippetSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):

        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class ProgramSerializer(serializers.Serializer):
    diploma_turuSecenekleri = (
    ('L', u'Lisans'),
    ('O', u'Önlisans')
    )

    ogratim_duzeyiSecenekleri = (
    ('O', u'Ortak'),
    ('1', u'1. Öğretim'),
    ('2', u'2. Öğretim'),
    ('U', u'Uzaktan Eğitim')
    )


    diploma_turuSecenekleri = (
        ('L', u'Lisans'),
        ('O', u'Onlisans')

    )

    id = serializers.IntegerField(read_only=True)
    fakulte=serializers.CharField(max_length=200)
    bolum=serializers.CharField(max_length=200)
    adi = serializers.CharField(max_length=200)
    ing_adi = serializers.CharField(max_length=200)

    diploma_turu = serializers.ChoiceField(choices=diploma_turuSecenekleri)
    ogratim_duzeyi = serializers.ChoiceField(choices=ogratim_duzeyiSecenekleri)

    yaratilma_tarihi = serializers.DateTimeField()
    yayinlanma_tarihi = serializers.DateTimeField()

    def create(self, validated_data):

        return Program.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
