# Generated by Django 5.0.7 on 2024-08-26 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0006_alter_animal_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='quiz',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='matcher.quiz'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='animal',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
