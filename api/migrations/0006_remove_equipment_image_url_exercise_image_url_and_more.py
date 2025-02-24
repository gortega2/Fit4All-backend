# Generated by Django 5.1.6 on 2025-02-24 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_equipment_image_url_alter_guide_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='image_url',
        ),
        migrations.AddField(
            model_name='exercise',
            name='image_url',
            field=models.CharField(blank=True, default='http://127.0.0.1:8000/static/images/exercises/default.jpg', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='guide',
            name='rating',
            field=models.IntegerField(default=4),
        ),
    ]
