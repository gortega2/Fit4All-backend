import json
from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
# Create your models here.

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
    #image = models.ImageField(blank=True, null=True)
    label = models.CharField(max_length=55)


class Exercise(models.Model):

    name = models.CharField(max_length=255, )
    instructions = models.TextField()
    muscle_group = MultiSelectField(choices=MUSCLE_GROUPS, null=True, blank=True)
    equipment = models.ManyToManyField(Equipment)
    #TODO: Add exercise picture
    #image = models.ImageField(blank=True, null=True)
    video_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return json.dumps({'id': self.id, 'name': self.name})


# class Exercise_block(models.Model):

#     exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
#     duration = models.IntegerField()
#     reps = models.IntegerField()
#     #TODO: Allow the weight to either be metric or imperial
#     #For now, setting the default system to be imperial
#     weight = models.DecimalField()

class Tags(models.Model):
    label = models.CharField(max_length=100, unique=True, primary_key=True)

class Guide(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    routine = models.JSONField()
    guide_tag = models.ManyToManyField(Tags, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    name = models.CharField(max_length=50)
    commented_guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)

#TODO: Implement Rating

#TODO: Implement Comments

    
