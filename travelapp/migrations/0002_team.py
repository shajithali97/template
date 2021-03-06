# Generated by Django 3.2.7 on 2021-09-06 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('profile_img', models.ImageField(upload_to='profiles')),
                ('profile_desc', models.TextField()),
            ],
        ),
    ]
