# Generated by Django 2.2.5 on 2019-09-22 17:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Strains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('strain_name', models.CharField(max_length=100)),
                ('strain_effect_list', models.TextField()),
                ('strain_flavor_list', models.TextField()),
                ('strain_desc', models.TextField(blank=True)),
                ('strain_effect_embed', models.TextField(blank=True)),
                ('strain_flavor_embed', models.TextField(blank=True)),
                ('strain_desc_embed', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(blank=True, default='defaultuser', max_length=100)),
                ('userclass', models.CharField(choices=[(0, 'default'), (1, 'recreational'), (2, 'medical')], default='default', max_length=100)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]