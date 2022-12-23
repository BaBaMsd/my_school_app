# Generated by Django 4.1.4 on 2022-12-22 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_delete_employe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_emp', models.CharField(max_length=25)),
                ('fonc_emp', models.CharField(max_length=30)),
                ('nni_emp', models.CharField(max_length=10)),
                ('num_tel_emp', models.CharField(max_length=15)),
                ('credit_emp', models.IntegerField(default=0)),
                ('salair_emp', models.IntegerField(default=0)),
            ],
        ),
    ]