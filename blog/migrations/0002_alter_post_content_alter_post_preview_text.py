# Generated by Django 4.2 on 2023-09-18 08:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='preview_text',
            field=models.TextField(default='', max_length=200),
        ),
    ]