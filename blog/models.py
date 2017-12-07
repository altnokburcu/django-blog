from django.db import models
from django.utils import timezone


class Post(models.Model): #Modelimizi nesne turunden tanimladik
    yazar = models.ForeignKey('auth.User')
    baslik = models.CharField(max_length=200) #kısa metinleri tanımlar.
    yazi = models.TextField() #uzun metinleri tanımlar.
    #bu da gün ve saati tanımlamada kullanılır.
    yaratilma_tarihi = models.DateTimeField(
           default=timezone.now)
    yayinlanma_tarihi = models.DateTimeField(
           blank=True, null=True)

    def yayinla(self):
        self.yayinlanma_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik