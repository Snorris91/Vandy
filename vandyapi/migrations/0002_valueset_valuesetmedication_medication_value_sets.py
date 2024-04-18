# Generated by Django 4.2.11 on 2024-04-18 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vandyapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValueSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_id', models.CharField(max_length=100, unique=True)),
                ('value_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ValueSetMedication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vandyapi.medication')),
                ('value_set', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vandyapi.valueset')),
            ],
        ),
        migrations.AddField(
            model_name='medication',
            name='value_sets',
            field=models.ManyToManyField(related_name='value_medications', through='vandyapi.ValueSetMedication', to='vandyapi.valueset'),
        ),
    ]
