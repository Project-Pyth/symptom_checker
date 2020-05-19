# Generated by Django 3.0.4 on 2020-04-22 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptom', '0004_profilee'),
    ]

    operations = [
        migrations.CreateModel(
            name='diagnose1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnose_age', models.IntegerField()),
                ('diagnose_gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10)),
                ('diagnose_symptom', models.CharField(max_length=225)),
            ],
        ),
        migrations.DeleteModel(
            name='diagnose',
        ),
        migrations.DeleteModel(
            name='Profilee',
        ),
    ]
