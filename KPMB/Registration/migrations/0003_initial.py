# Generated by Django 4.0.5 on 2024-04-19 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Registration', '0002_delete_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('nama', models.TextField()),
            ],
        ),
    ]
