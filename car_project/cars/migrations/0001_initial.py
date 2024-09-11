# Generated by Django 5.1.1 on 2024-09-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('title', models.TextField()),
                ('time', models.TextField()),
                ('year', models.TextField()),
                ('mileage', models.TextField()),
                ('location', models.TextField()),
                ('description', models.TextField()),
                ('image', models.TextField()),
                ('modified_date', models.TextField()),
                ('price', models.TextField()),
            ],
        ),
    ]
