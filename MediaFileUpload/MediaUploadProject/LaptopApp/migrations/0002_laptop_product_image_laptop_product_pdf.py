# Generated by Django 4.0 on 2022-01-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LaptopApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='product_image',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='laptop',
            name='product_pdf',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
