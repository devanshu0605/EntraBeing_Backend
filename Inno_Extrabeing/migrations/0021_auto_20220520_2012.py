# Generated by Django 2.0 on 2022-05-20 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inno_Extrabeing', '0020_product_detail_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_detail',
            old_name='Product_image',
            new_name='Product_Image',
        ),
    ]
