# Generated by Django 5.1.1 on 2024-09-30 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_alter_hero_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me_para1', models.TextField()),
                ('about_me_para2', models.TextField()),
                ('years_of_experience', models.PositiveIntegerField()),
                ('projects', models.PositiveIntegerField()),
                ('happy_clients', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
