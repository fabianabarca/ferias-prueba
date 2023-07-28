from django.contrib.gis.db import models
from products.models import Product
from django.contrib.auth.models import User
from marketplaces.models import Marketplace, Payment

# Create your models here.


class MarketplaceEdit(models.Model):
    """Model definition for Marketplace (la feria)."""

    SIZE_CHOICES = [
        ("S", "Pequeña"),
        ("M", "Mediana"),
        ("L", "Grande"),
        ("XL", "Muy grande"),
    ]
    BRANCH_CHOICES = [
        ("Atlántico", "Comité Regional Atlántico"),
        ("Brunca", "Comité Regional Brunca"),
        ("Central Central", "Comité Regional Central Central"),
        ("Central Occidental Este", "Comité Regional Central Occidental Este"),
        ("Central Occidental Oeste", "Comité Regional Central Occidental Oeste"),
        ("Central Oriental", "Comité Regional Central Oriental"),
        ("Chorotega", "Comité Regional Chorotega"),
        ("Huetar Norte", "Comité Regional Huetar Norte"),
        ("Pacífico Central", "Comité Regional Pacífico Central"),
    ]
    PARKING_CHOICES = [
        ("lane", "en la calle"),
        ("street_side", "al lado de la calle en espacio dedicado"),
        ("surface", "un espacio amplio de parqueo"),
    ]

    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    # General information
    name = models.CharField(max_length=127)
    name_alternate = models.CharField(max_length=127, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    opening_hours = models.CharField(max_length=1023, blank=True, null=True)
    opening_date = models.DateField(blank=True, null=True)
    location = models.PointField(blank=True, null=True)
    area = models.PolygonField(blank=True, null=True)
    province = models.CharField(max_length=31)
    canton = models.CharField(max_length=31)
    district = models.CharField(max_length=31)
    postal_code = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    size = models.CharField(choices=SIZE_CHOICES, max_length=2, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=127, blank=True, null=True)
    website = models.URLField(max_length=127, blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(
        choices=BRANCH_CHOICES, max_length=63, blank=True, null=True
    )
    # Infrastructure
    parking = models.CharField(
        choices=PARKING_CHOICES, max_length=31, blank=True, null=True
    )
    bicycle_parking = models.BooleanField(blank=True, null=True)
    fairground = models.BooleanField(blank=True, null=True)
    indoor = models.BooleanField(blank=True, null=True)
    toilets = models.BooleanField(blank=True, null=True)
    handwashing = models.BooleanField(blank=True, null=True)
    drinking_water = models.BooleanField(blank=True, null=True)
    # Services
    food = models.BooleanField(blank=True, null=True)
    drinks = models.BooleanField(blank=True, null=True)
    handicrafts = models.BooleanField(blank=True, null=True)
    butcher = models.BooleanField(blank=True, null=True)
    dairy = models.BooleanField(blank=True, null=True)
    seafood = models.BooleanField(blank=True, null=True)
    garden_centre = models.BooleanField(blank=True, null=True)
    florist = models.BooleanField(blank=True, null=True)
    # Other
    payment = models.ManyToManyField(Payment, blank=True)
    other_services = models.TextField(blank=True, null=True)
    # Products
    products = models.ManyToManyField(Product, blank=True)
    # Crowdsourcing
    comments = models.TextField(blank=True, null=True)
    submitted_by = models.CharField(max_length=127)
    submitted_on = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.name} por {self.submitted_by} ({self.submitted_on})'


class PhotoEdit(models.Model):
    """Model definition for Photo."""

    marketplace = models.ForeignKey(MarketplaceEdit, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="crowdsourcing")
    description = models.CharField(
        max_length=255, blank=True, null=True, help_text="Descripción de la foto."
    )

    def __str__(self):
        return f'{self.url}: {self.description}'

class OpeningHoursEdit(models.Model):
    DAY_CHOICES = [
        ("Mo", "Lunes"),
        ("Tu", "Martes"),
        ("We", "Miércoles"),
        ("Th", "Jueves"),
        ("Fr", "Viernes"),
        ("Sa", "Sábado"),
        ("Su", "Domingo"),
    ]
    HOUR_CHOICES = [
        ("5:00", "5:00"),
        ("6:00", "6:00"),
        ("7:00", "7:00"),
        ("8:00", "8:00"),
        ("9:00", "9:00"),
        ("10:00", "10:00"),
        ("11:00", "11:00"),
	("12:00", "12:00"),
        ("13:00", "13:00"),
        ("14:00", "14:00"),
        ("15:00", "15:00"),
        ("16:00", "16:00"),
	("17:00", "17:00"),
    ]
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    day_opens = models.CharField(choices=DAY_CHOICES, max_length=10, blank=True, null=True)
    hour_opens = models.TimeField(choices=HOUR_CHOICES, max_length=10, blank=True, null=True)
    day_closes = models.CharField(choices=DAY_CHOICES, max_length=10, blank=True, null=True)
    hour_closes = models.TimeField(choices=HOUR_CHOICES, max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.marketplace}: {self.day_opens} {self.hour_opens} - {self.day_closes} {self.hour_closes}'
