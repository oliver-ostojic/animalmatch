# Generated by Django 5.0.7 on 2024-08-26 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0010_alter_animal_locations_alter_quizresult_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
    ]