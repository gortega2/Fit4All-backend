from rest_framework import serializers, fields
from .models import *

class ExerciseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    muscle_group = fields.MultipleChoiceField(choices=MUSCLE_GROUPS, required=False)

    class Meta:
        model = Exercise
        fields = ('id', 'name', 'instructions', 'muscle_group', 'equipment', 'video_link')


class ExerciseBlockSerializer(serializers.Serializer):
    exercise = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all())
    duration = serializers.IntegerField(min_value=0, required=False)
    reps = serializers.IntegerField(min_value=0, required=False)
    weight = serializers.DecimalField(max_digits=3, decimal_places=1, required=False)

#This is redundant
class RoutineSerializer(serializers.Serializer):
    routine = serializers.ListField(child=ExerciseBlockSerializer(), allow_empty=False)




class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'label')


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('label', )

class GuideSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Guide
        fields = ('id','author', 'title', 'description', 'guide_tag', 'created_at', 'updated_at', 'routine')