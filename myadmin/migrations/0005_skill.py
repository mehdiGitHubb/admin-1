# Generated by Django 5.1.1 on 2024-09-30 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0004_aboutme_about_me_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('percentage', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
