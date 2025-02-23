# Generated by Django 5.1.6 on 2025-02-23 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_exercise_muscle_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=255)),
                ('commented_guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.guide')),
            ],
        ),
    ]
