# Generated by Django 4.2.1 on 2023-05-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemsImages', '0005_remove_items_analogue_palette_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='items',
            name='color',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]