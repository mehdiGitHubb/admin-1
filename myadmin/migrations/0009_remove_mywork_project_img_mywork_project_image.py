# Generated by Django 5.1.1 on 2024-09-30 13:25

import myadmin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0008_mywork'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mywork',
            name='project_img',
        ),
        migrations.AddField(
            model_name='mywork',
            name='project_image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/', validators=[myadmin.models.validate_image_or_svg]),
        ),
    ]
