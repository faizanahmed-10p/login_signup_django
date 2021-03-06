# Generated by Django 2.1.2 on 2018-10-31 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0006_auto_20181031_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateprofileinfo',
            name='independent_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='candidateprofileinfo',
            name='id',
            field=models.CharField(max_length=128, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='candidateprofileinfo',
            name='party',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
