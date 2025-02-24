import json
from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
import random
# Create your models here.
lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut lacinia vestibulum tellus sed maximus. Vestibulum felis diam, auctor nec congue ut, vehicula vel turpis. Integer convallis porttitor ante. Etiam dignissim, dui in pharetra interdum, magna leo sagittis felis, eu imperdiet metus neque nec sem. Donec nec leo quis turpis rutrum maximus. Quisque at neque est. Ut ultricies gravida diam non tincidunt. Proin tempus dolor urna, ac fringilla enim vehicula eget. Donec imperdiet, odio sit amet porttitor tempor, nibh est rutrum dui, ac cursus purus augue a enim. Quisque mattis erat sed ultricies tempus. '
MUSCLE_GROUPS = {
    'ABDR': 'Abductors',
    "ADDR": 'Adductors',
    "ABS": "Abs",
    "BACK": "Back",
    "BCPS": "Biceps",
    'CLVS': 'Calves',
    "CHST": 'Chest',
    'FARM': 'Forearms',
    "GLTS": 'Glutes',
        "HMSTR": 'Hamstrings',
    'LBACK': 'Lower Back',
    'NCK': 'Neck',
    "QDCPS": 'Quadriceps',
    "SHDR": 'Shoulders',
    'TRPS': 'Trapezius',
    "TRCPS": 'Triceps',
}


class Equipment(models.Model):
    #TODO: Add equipment picture
    label = models.CharField(max_length=55)


class Exercise(models.Model):

    name = models.CharField(max_length=255, )
    instructions = models.TextField(default=lorem)
    muscle_group = MultiSelectField(choices=MUSCLE_GROUPS, null=True, blank=True)
    equipment = models.ManyToManyField(Equipment, null=True, blank=True)
    video_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.CharField(default='http://127.0.0.1:8000/static/images/exercises/default.jpg', blank=True, null=True, max_length=255)




class Tags(models.Model):
    label = models.CharField(max_length=100, unique=True, primary_key=True)

class Guide(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(default=lorem)
    routine = models.JSONField()
    guide_tag = models.ManyToManyField(Tags, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=random.randint(0,5))

class Comments(models.Model):
    name = models.CharField(max_length=50)
    commented_guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)





    
