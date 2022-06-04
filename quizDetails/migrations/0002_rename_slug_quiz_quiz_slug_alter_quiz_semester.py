# Generated by Django 4.0.1 on 2022-06-04 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizDetails', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='slug',
            new_name='quiz_slug',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='semester',
            field=models.CharField(choices=[('FIRST_SEMESTER', '1ST'), ('SECOND_SEMESTER', '2ND')], default=('FIRST_SEMESTER', '1ST'), max_length=20),
        ),
    ]
