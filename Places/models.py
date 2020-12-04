from django.db.models import Model, CharField, TextField, IntegerField
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class CityInfo(Model):
    city_name = CharField(max_length=50)
    city_image_link = CharField(max_length=100, null=True)
    state = CharField(max_length=200, null=True, blank=True)
    country = CharField(max_length=200, null=True)
    covid_details = CharField(max_length=100, null=True, blank=True)
    para = TextField(null=True)

class PlacesToVisit(Model):
    city_name = CharField(max_length=50)
    names = ArrayField(CharField(max_length=60), null=True)
    links = ArrayField(CharField(max_length=200), null=True)
    photo_links = ArrayField(CharField(max_length=200), null=True)
    info = ArrayField(CharField(max_length=1000), null=True)
    total_places = IntegerField(null=True)

class Food(Model):
    city_name = CharField(max_length=50)
    names = ArrayField(CharField(max_length=60), null=True)
    info = ArrayField(CharField(max_length=300), null=True)
    photo_links = ArrayField(CharField(max_length=200), null=True)
    res_items = ArrayField(ArrayField(CharField(max_length=100)))
    total_restaurants = IntegerField(null=True)
