# Generated by Django 4.1.5 on 2023-01-24 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('duration', models.CharField(max_length=30)),
                ('author_name', models.CharField(max_length=30)),
            ],
        ),
    ]
