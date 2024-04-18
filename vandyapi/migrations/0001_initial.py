# Generated by Django 4.2.11 on 2024-04-17 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=150)),
                ('generic_name', models.CharField(max_length=50)),
                ('route', models.CharField(max_length=50)),
                ('outpatients', models.IntegerField(blank=True, null=True)),
                ('inpatients', models.IntegerField(blank=True, null=True)),
                ('patients', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]