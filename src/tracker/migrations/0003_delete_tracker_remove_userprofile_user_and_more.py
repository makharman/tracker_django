# Generated by Django 4.0 on 2024-03-23 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('tracker', '0002_accountprofile_expensecategory_incomecategory_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tracker',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='income',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.DeleteModel(
            name='AccountProfile',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]