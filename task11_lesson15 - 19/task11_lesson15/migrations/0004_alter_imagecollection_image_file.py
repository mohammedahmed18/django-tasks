# Generated by Django 3.2.7 on 2022-06-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task11_lesson15', '0003_imagecollection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecollection',
            name='image_file',
            field=models.ImageField(upload_to='static/uploads'),
        ),
    ]
