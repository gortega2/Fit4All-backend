from rest_framework import serializers
from .models import *



class ExerciseBlockSerializer(serializers.Serializer):
    exercise = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all())
    duration = serializers.IntegerField()
    reps = serializers.IntegerField()
    weight = serializers.IntegerField()


class RoutineSerialzier(serializers.Serializer):
    routine = serializers.ListField(child=ExerciseBlockSerializer(), allow_empty=False)


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'