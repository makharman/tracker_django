# Generated by Django 5.0.4 on 2024-04-17 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], null=True),
        ),
    ]
