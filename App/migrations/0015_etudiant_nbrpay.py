# Generated by Django 4.1.4 on 2023-01-03 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_frais'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='nbrPay',
            field=models.IntegerField(default=0),
        ),
    ]
