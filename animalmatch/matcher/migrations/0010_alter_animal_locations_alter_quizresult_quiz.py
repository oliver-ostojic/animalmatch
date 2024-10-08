# Generated by Django 5.0.7 on 2024-08-26 22:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0009_alter_animal_locations_alter_quizresult_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='locations',
            field=models.JSONField(default=None),
        ),
        migrations.AlterField(
            model_name='quizresult',
            name='quiz',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='results', to='matcher.quiz'),
        ),
    ]
