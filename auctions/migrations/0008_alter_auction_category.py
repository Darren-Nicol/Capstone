# Generated by Django 4.0.2 on 2022-02-13 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20220104_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.CharField(choices=[('Genesis', 'Genesis'), ('Ghetto Kings', 'Ghetto Kings'), ('Township Princess', 'Township Princess')], default='Genesis', max_length=30),
        ),
    ]
