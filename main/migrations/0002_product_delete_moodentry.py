# Generated by Django 5.1.1 on 2024-09-11 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('size', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='MoodEntry',
        ),
    ]
