# Generated by Django 2.2.6 on 2019-12-13 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laporan', '0012_auto_20191213_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='laporan',
            name='daerah',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
