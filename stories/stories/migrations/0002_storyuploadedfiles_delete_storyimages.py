# Generated by Django 4.2.6 on 2023-11-23 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryUploadedFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(upload_to='')),
                ('image_2', models.ImageField(upload_to='')),
                ('image_3', models.ImageField(upload_to='')),
                ('image_4', models.ImageField(upload_to='')),
                ('image_5', models.ImageField(upload_to='')),
                ('image_6', models.ImageField(upload_to='')),
                ('image_7', models.ImageField(upload_to='')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.story')),
            ],
            options={
                'verbose_name': 'story image',
                'verbose_name_plural': 'story image',
                'ordering': ('-id',),
            },
        ),
        migrations.DeleteModel(
            name='StoryImages',
        ),
    ]