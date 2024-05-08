# Generated by Django 5.0.4 on 2024-05-07 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('address', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('draft', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('phone_number', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date', models.DateField()),
                ('color', models.CharField(choices=[('white', 'White'), ('black', 'Black'), ('red', 'Red'), ('grey', 'Grey'), ('blue', 'Blue')], max_length=30)),
                ('additional_name', models.ManyToManyField(blank=True, related_name='additional', to='polls.manufacture')),
                ('manufacture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.manufacture')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
                'ordering': ['-name'],
            },
        ),
    ]