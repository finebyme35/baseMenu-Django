# Generated by Django 4.0.4 on 2022-06-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menucode', '0008_alter_category_updatedat_alter_product_updatedat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='placementId',
            field=models.IntegerField(unique=True),
        ),
    ]
