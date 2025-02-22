# Generated by Django 4.0.4 on 2022-08-10 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0008_alter_reciept_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reciept',
            old_name='address',
            new_name='destination',
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/profile_images'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='reciept',
            name='Total',
            field=models.FloatField(null=True),
        ),
    ]
