# Generated by Django 4.0.4 on 2022-06-24 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menucode', '0014_alter_category_options_alter_category_placementid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['placementId'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
