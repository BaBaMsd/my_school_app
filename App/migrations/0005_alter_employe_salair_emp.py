# Generated by Django 4.1.4 on 2022-12-22 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_employe_alter_etu_classe_class_nom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='salair_emp',
            field=models.IntegerField(default=0),
        ),
    ]
