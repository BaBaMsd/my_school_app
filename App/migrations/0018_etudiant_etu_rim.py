# Generated by Django 4.1.4 on 2023-01-18 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_absence_metier'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='etu_rim',
            field=models.CharField(default=0, max_length=25),
        ),
    ]
