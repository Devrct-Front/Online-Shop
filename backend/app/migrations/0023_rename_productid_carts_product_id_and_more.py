# Generated by Django 4.2 on 2023-06-16 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_rename_product_carts_productid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carts',
            old_name='productId',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='carts',
            old_name='userId',
            new_name='user_id',
        ),
    ]