# Generated by Django 4.2 on 2023-10-19 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_orderhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configurations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(blank=True, help_text='Site name', max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, help_text='Displayed on contact page', max_length=15, null=True)),
                ('email', models.EmailField(blank=True, help_text='Displayed on contact page', max_length=254, null=True)),
                ('address', models.TextField(blank=True, help_text='Where customers will pick up their orders', null=True)),
                ('facebook_url', models.URLField(blank=True, help_text='Displayed on about page', null=True)),
                ('instagram_url', models.URLField(blank=True, help_text='Displayed on about page', null=True)),
            ],
            options={
                'verbose_name': 'Configuration',
                'verbose_name_plural': 'Configurations',
            },
        ),
    ]
