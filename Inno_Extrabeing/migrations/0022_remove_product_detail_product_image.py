# Generated by Django 2.0 on 2022-05-20 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inno_Extrabeing', '0021_auto_20220520_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_detail',
            name='Product_Image',
        ),
    ]
