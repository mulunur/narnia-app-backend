# Generated by Django 4.2.1 on 2023-05-13 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itemsImages', '0004_alter_items_analogue_palette_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='analogue_palette_id',
        ),
        migrations.RemoveField(
            model_name='items',
            name='contrast_palette_id',
        ),
    ]
