# Generated by Django 3.2.7 on 2022-06-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task11_lesson15', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=200)),
                ('image_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image_file', models.ImageField(upload_to='uploads')),
            ],
        ),
    ]