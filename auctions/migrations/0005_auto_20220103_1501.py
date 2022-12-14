# Generated by Django 3.1 on 2022-01-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20211231_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.CharField(choices=[('ART', 'Collectibles & Art'), ('FOT', 'Footprint'), ('PAT', 'Partners'), ('GNS', 'Genesis'), ('GTO', 'Ghetto Kings'), ('TWP', 'Township Princess')], default='GNS', max_length=8),
        ),
    ]
