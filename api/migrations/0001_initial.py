# Generated by Django 5.1.6 on 2025-02-17 01:39

import django.db.models.deletion
import multiselectfield.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('instructions', models.TextField()),
                ('muscle_group', multiselectfield.db.fields.MultiSelectField(choices=[('ABDR', 'Abductors'), ('ADDR', 'Adductors'), ('ABS', 'Abs'), ('BACK', 'Back'), ('BCPS', 'Biceps'), ('CLVS', 'Calves'), ('CHST', 'Chest'), ('FARM', 'Forearms'), ('GLTS', 'Glutes'), ('HMSTR', 'Hamstrings'), ('LBACK', 'Lower Back'), ('NCK', 'Neck'), ('QDCPS', 'Quadriceps'), ('SHDR', 'Shoulders'), ('TRPS', 'Trapezius'), ('TRCPS', 'Triceps')], max_length=81, null=True)),
                ('equipment', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('video_link', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('label', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('routine', models.JSONField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('guide_tag', models.ManyToManyField(blank=True, to='api.tags')),
            ],
        ),
    ]
