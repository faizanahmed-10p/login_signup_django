# Generated by Django 2.1.2 on 2018-10-31 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0005_auto_20181031_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voterprofileinfo',
            name='id',
            field=models.CharField(max_length=128, primary_key=True, serialize=False),
        ),
    ]
