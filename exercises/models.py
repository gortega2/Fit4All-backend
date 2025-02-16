from django.db import models
from multiselectfield import MultiSelectField

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
    muscle_group = MultiSelectField(choices=MUSCLE_GROUPS,)
    equipment = models.CharField()
    #TODO: Add picture thumbnail to exercises
    video_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)