from rest_framework import serializers, fields
from .models import *
from django.contrib.auth.models import User

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ExerciseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    muscle_group = fields.MultipleChoiceField(choices=MUSCLE_GROUPS, required=False)

    class Meta:
        model = Exercise
        fields = ('id', 'name', 'instructions', 'muscle_group', 'equipment', 'video_link', 'image_url')


class ExerciseBlockSerializer(serializers.Serializer):
    exercise = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all())
    duration = serializers.IntegerField(min_value=0, required=False)
    reps = serializers.IntegerField(min_value=0, required=False)
    sets = serializers.IntegerField(min_value=0, required=False)
    weight = serializers.DecimalField(max_digits=3, decimal_places=1, required=False)


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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('')

class GuideSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Guide
        fields = '__all__'