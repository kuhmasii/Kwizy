# Generated by Django 4.0.1 on 2022-06-04 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmentDetails', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='level',
            old_name='date_created',
            new_name='created',
        ),
        migrations.AlterField(
            model_name='level',
            name='name',
            field=models.CharField(choices=[('FIRST_YEAR', '100'), ('SECOND_YEAR', '200'), ('THIRD_YEAR', '300'), ('FOURTH_YEAR', '400')], max_length=20),
        ),
    ]