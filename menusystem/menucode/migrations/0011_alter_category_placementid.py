# Generated by Django 4.0.4 on 2022-06-24 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menucode', '0010_alter_category_placementid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='placementId',
            field=models.IntegerField(unique=True),
        ),
    ]
