from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
# Create your models here.


class Exercise(models.Model):

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




    name = models.CharField(max_length=255, )
    instructions = models.TextField()
    muscle_group = MultiSelectField(choices=MUSCLE_GROUPS, null=True)
    equipment = models.CharField(default=None, null=True, blank=True)
    #TODO: Add picture thumbnail to exercises
    video_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
    tags = models.ManyToManyField(Tags)
    routine = models.JSONField()
    guide_tag = models.ManyToManyField(Tags, null=True, blank=True)

#TODO: Implement Rating

#TODO: Implement Comments

    
