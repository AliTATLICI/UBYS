# -*- coding: utf-8 -*-
#from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pbs.models import Birim, Bolum, Personel


class Program(models.Model):
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

    fakulte=models.ForeignKey(Birim, on_delete=models.PROTECT)
    bolum=models.ForeignKey(Bolum, on_delete=models.PROTECT)
    adi=models.CharField(max_length=100)
    ing_adi=models.CharField(max_length=100)
    diploma_turu = models.CharField(max_length=1, choices=diploma_turuSecenekleri, verbose_name='Diploma Türü')
    ogratim_duzeyi = models.CharField(max_length=1, choices=ogratim_duzeyiSecenekleri, verbose_name='Öğretim Düzeyi')
    #dersler = JSONField(null=True,blank=True)
    yaratilma_tarihi = models.DateTimeField(default=timezone.now)
    yayinlanma_tarihi = models.DateTimeField(blank=True, null=True)

    def yayinla(self):
        self.yayinlanma_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.adi


class Ogrenci(models.Model):

    '''
    sinifSecenekleri = (
        ('H', 'Hazırlık'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('İ', 'İntibak'),
        ('İH', 'İntibak Hazırlık'),
        ('BH', 'Bilimsel Hazırlık'),
        ('TH', 'Türkçe Hazırlık'),
        ('AH', 'Arapça Hazırlık'),
        ('GH', 'Almanca Hazırlık'),
    )

    subeSecenekleri = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F')
    )

    kayit_yiliSecenekleri = (
        ('17', '2017'),
        ('16', '2016'),
        ('15', '2015'),
        ('14', '2014'),
        ('13', '2013'),
        ('12', '2012'),
        ('11', '2011'),
        ('10', '2010'),
    )

    yonetmelikSecenekleri = (
        ('-', 'Yok'),
        ('E', 'E 50'),
        ('Y', 'Y 60'),
        ('B', 'B'),
        ('M', 'M 60')
    )

    egitim_yiliSecenekleri = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('A', '10'),
        ('B', '11'),
        ('C', '12'),
        ('D', '13'),
        ('E', '14'),
    )

    kayit_sekliSecenekleri = (
        ('48', 'DGS İle Gelen'),
        ('56', 'ÖSS Kazanan'),
        ('105', 'Yatay Geçiş(ÖSYS Merkezi Puanla) Üniversite Dışı')
    )

    not_sistemiSecenekleri = (
        ('N', 'Nümerik'),
        ('H', 'Harf'),
        ('Y', 'Yok')
    )

    hazirlik_sinifiSecenekleri = (
        ('Y', 'Yok'),
        ('M', 'Muaf'),
        ('1', '1 Yıl'),
        ('2', '2 Yıl')
    )
    '''

    ogrenci_no=models.CharField(max_length=10)
    tc_no=models.CharField(max_length=11)
    adi=models.CharField(max_length=50)
    soyadi=models.CharField(max_length=50)
    cep_telefonu=models.CharField(max_length=11, null=True)
    fakulte_yuksekokul=models.ForeignKey(Birim, on_delete=models.PROTECT)
    bolumu=models.ForeignKey(Bolum, on_delete=models.PROTECT)
    program=models.ForeignKey(Program, on_delete=models.PROTECT)
    def __str__(self):
        return ('{} {}'.format(self.adi, self.soyadi))

'''sinif=models.CharField(max_length=2, choices=sinifSecenekleri, verbose_name="Sınıf")
    sube=models.CharField(max_length=2, choices=subeSecenekleri, verbose_name='Şube')
    kayit_yili=models.CharField(max_length=2, choices=kayit_yiliSecenekleri, verbose_name="Kayıt Yılı")
    kayit_tarihi=models.DateTimeField()
    e_kayit_osym=models.DateTimeField()
    yonetmelik=models.CharField(max_length=1, choices=yonetmelikSecenekleri, verbose_name='Yönetmelik')
    egitim_yili=models.CharField(max_length=2, choices=egitim_yiliSecenekleri, verbose_name="Eğitim Yılı")
    kayit_sekli=models.CharField(max_length=3, choices=kayit_sekliSecenekleri, verbose_name='Kayıt Şekli')
    not_sistemi=models.CharField(max_length=1, choices=not_sistemiSecenekleri, verbose_name='Not Sistemi')
    mezuniyet_ayrilis_tarihi=models.DateField()
    diploma_no=models.CharField(max_length=8, verbose_name='Diploma No')
    gecici_mezuniyet_verildiMi=models.BooleanField()
    #danismani=models.ForeignKey(Personel, on_delete=models.PROTECT)
    hazirlik_sinifi=models.CharField(max_length=1, choices=hazirlik_sinifiSecenekleri, verbose_name='Hazırlık Sınıfı')
    staj_gunu=models.SmallIntegerField()
    ogrencilik_hakki=models.BooleanField()
    ek_sinav=models.BooleanField()
'''


class Ders(models.Model):

    '''
    konduguYilSecenekleri = (
        ('17', '2017-2018'),
        ('16', '2016-2017'),
        ('15', '2015-2016'),
        ('14', '2014-2015'),
        ('13', '2013-2014'),
        ('12', '2012-2013'),
        ('11', '2011-2012'),
        ('10', '2010-2011'),

    )

    kaldirildigiYilSecenekleri = (
        ('17', '2017-2018'),
        ('16', '2016-2017'),
        ('15', '2015-2016'),
        ('14', '2014-2015'),
        ('13', '2013-2014'),
        ('12', '2012-2013'),
        ('11', '2011-2012'),
        ('10', '2010-2011'),

    )

    sinifSecenekleri = (
        ('H', 'Hazırlık'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('I', 'İntibak'),
        ('K', 'İntibak Hazırlık'),
        ('B', 'Bilimsel Hazırlık'),
        ('T', 'Türkçe Hazırlık'),
        ('A', 'Arapça Hazırlık'),
        ('G', 'Almanca Hazırlık'),
    )

    donemSecenekleri = (
        ('G', 'Güz'),
        ('B', 'Bahar'),
        ('Y', 'Yaz'),
        ('L', 'Yıllık')
    )

    dersSuresiSecenekleri = (
        ('D', 'Dönemlik'),
        ('Y', 'Yıllık')
    )

    dersTuruSecenekleri = (
        ('Z', 'Zorunlu'),
        ('S', 'Seçmeli'),
        ('1', 'Seçimlik 1'),
        ('2', 'Seçimlik 2'),
        ('U', 'Üniversite Ortak Zorunlu')
    )

    dersIcerigiSecenekleri = (
        ('T', 'Teorik Ders'),
        ('U', 'Uygulamalı Ders'),
        ('S', 'Staj'),
        ('Y', 'YOK'),
        ('M', 'Mezuniyet Tezi'),
        ('B', 'Beden-Eğitim Seçmeli'),
        ('G', 'Uygulamalı Teorik Ders'),
        ('L', 'Laboratuvar'),
        ('K', 'Klinik Uygulama'),
        ('P', 'Pratik Ders'),
        ('E', 'Seminer'),
        ('O', 'Bitirme Ödevi'),
        ('L', 'Kurul'),
        ('J', 'AKTS Dahil Olmayan Staj')
    )

    dersDiliSecenekleri = (
        ('T', 'Türkçe'),
        ('I', 'İngilizce'),
        ('A', 'Arapça'),
        ('G', 'Almanca'),
        ('F', 'Fransızca'),
        ('M', 'Mesleki İngilizce')
    )

    sinavGirisSekliSecenekleri = (
        ('A', 'Vize-Final Ayrı'),
        ('B', 'Vize-Final Birlikte')
    )

    krediSecenekleri = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9')
    )

    '''

    programi = models.ForeignKey(Program, default=1, verbose_name='Programı', on_delete=models.PROTECT)
    adi = models.CharField(max_length=200)
    ing_adi = models.CharField(max_length=200)
    ders_kodu = models.CharField(max_length=7)
    ders_kodu2 = models.CharField(max_length=10)
    '''genel_bilgi = models.TextField()
    konduguYil = models.CharField(max_length=2, choices=konduguYilSecenekleri, verbose_name='Konduğu Yıl')
    kaldirildigiYil = models.CharField(max_length=2, choices=kaldirildigiYilSecenekleri, verbose_name='Kaldırıldığı Yıl')
    sinif = models.CharField(max_length=1, choices=sinifSecenekleri, verbose_name='Sınıf')
    donem = models.CharField(max_length=1, choices=donemSecenekleri, verbose_name='Dönem')
    dersSuresi = models.CharField(max_length=1, choices=dersSuresiSecenekleri, verbose_name='Ders Süresi')
    dersTuru = models.CharField(max_length=1, choices=dersTuruSecenekleri, verbose_name='Ders Türü')
    dersIcerigi = models.CharField(max_length=1, choices=dersIcerigiSecenekleri, verbose_name='Ders İçeriği')
    dersKaldirilmisMi = models.BooleanField()
    transkriptteCikmasinMi = models.BooleanField()
    dersDili = models.CharField(max_length=1, choices=dersDiliSecenekleri, verbose_name='Ders Dili')
    ortalamayaKatilmasinMi = models.BooleanField()
    sinavGirisSekli = models.CharField(max_length=1, choices=sinavGirisSekliSecenekleri, verbose_name='Sınav Giriş Şekli')
    krediTeorik = models.CharField(max_length=1, choices=krediSecenekleri, verbose_name='Teorik Kredi')
    krediPratik = models.CharField(max_length=1, choices=krediSecenekleri, verbose_name='Pratik Kredi')
    krediLab = models.CharField(max_length=1, choices=krediSecenekleri, verbose_name='Laboratuvar Kredi')
    krediToplam = models.CharField(max_length=1, verbose_name='Toplam Kredi')
    '''






    def __str__(self):
        return self.adi


##### Kod görünüm ayarları #######

# Kodlar yan yana mı - alt alta mı
LEXERS = [item for item in get_all_lexers() if item[1]]
# Diller
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# Style - görünüm tipi
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


##### Kod görünüm ayarları #######


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    def __str__(self):
        return ('{}'.format(self.title))

    class Meta:
        ordering = ('created',)
