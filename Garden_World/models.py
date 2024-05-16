from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices

# Create your models here.
class Crop(models.Model):
    #Crop's information
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    
    WHEATER = Choices(
        ('anyone', _('Cualquiera')),
        ('tropical', _('Tropical')),
        ('dry', _('Seco')),
        ('mild', _('Templado')),
        ('continental', _('Continental')),
        ('cool', _('Frios')),
    )
    weather = models.CharField(
        max_length=15,
        choices=WHEATER,
        default=WHEATER.anyone,
    )
    
    image = models.ImageField(upload_to='images', null=True)

    quantity = models.IntegerField(default=0)

    DIFICULTY = Choices(
        ('begginer', _('Principiante')),
        ('medium', _('Medio')),
        ('hard', _('Dificil'))
    )
    dificulty = models.CharField(
        max_length=10,
        choices=DIFICULTY,
        default=DIFICULTY.begginer,
    )

    SEASON = Choices(
        ('anyone', _('Cualquiera')),
        ('spring', _('Primavera')),
        ('summer', _('Verano')),
        ('autumn', _('otoño')),
        ('winter', _('Invierno')),
    )
    season = models.CharField(
        max_length=10,
        choices=SEASON,
        default=SEASON.anyone,
    )

    ILLUMINATION = Choices(
        ('sun', _('Sol')),
        ('half_shadow', _('Media sombra')),
        ('shadow', _('Sombra')),
    )
    illumination = models.CharField(
        max_length=12,
        choices=ILLUMINATION,
        default=ILLUMINATION.sun,
    )

    TYPE = Choices(
        ('vegetables', _('Hortalizas')),
        ('flowers', _('Flores')),
        ('aromatics', _('Aromaticas')),
    )
    type = models.CharField(
        max_length=10,
        choices=TYPE,
        default=TYPE.vegetables,
    )


    class Meta:
        verbose_name = 'crop'
        verbose_name_plural = 'crops'

    def __str__(self):
        return f"Nombre: {self.title}, {self.image}"
