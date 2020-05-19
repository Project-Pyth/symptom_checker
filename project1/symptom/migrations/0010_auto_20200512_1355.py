# Generated by Django 3.0.4 on 2020-05-12 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symptom', '0009_auto_20200512_1227'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bodyloc',
            new_name='body_data',
        ),
        migrations.RenameModel(
            old_name='subbody',
            new_name='body_loc',
        ),
        migrations.RenameModel(
            old_name='bodydata',
            new_name='sub_body',
        ),
        migrations.RenameField(
            model_name='body_data',
            old_name='med_bodyloc',
            new_name='med_bodydata',
        ),
        migrations.RenameField(
            model_name='body_loc',
            old_name='med_subbody',
            new_name='med_bodyloc',
        ),
        migrations.RenameField(
            model_name='sub_body',
            old_name='med_bodydata',
            new_name='med_subbody',
        ),
    ]