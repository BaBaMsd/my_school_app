# Generated by Django 4.1.4 on 2023-01-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0016_depence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_abs', models.DateField()),
                ('ann_sco', models.CharField(max_length=25)),
                ('justification', models.CharField(max_length=30)),
                ('etu_id', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Metier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matier_nom', models.CharField(max_length=25)),
            ],
        ),
    ]