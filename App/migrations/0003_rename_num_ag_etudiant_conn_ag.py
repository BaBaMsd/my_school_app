# Generated by Django 4.1.4 on 2022-12-20 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_remove_etudiant_nom_ag_alter_etudiant_num_ag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='etudiant',
            old_name='num_ag',
            new_name='conn_ag',
        ),
    ]
