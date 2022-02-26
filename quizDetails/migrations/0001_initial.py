# Generated by Django 4.0.1 on 2022-02-23 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departmentDetails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_subject', models.CharField(help_text='Eg: Biology, GST, Biochemistry, Microbiology', max_length=100)),
                ('course_title', models.CharField(help_text='Eg: Immunochemistry, Feasibility studies, Microbial studies', max_length=100)),
                ('course_code', models.CharField(help_text='GST101, BCH301, MCB202, BIO102', max_length=10)),
                ('semester', models.CharField(choices=[('First', '1st'), ('Second', '2nd')], default='First', max_length=10)),
                ('section', models.CharField(blank=True, max_length=10)),
                ('slug', models.SlugField(max_length=200)),
                ('number_of_question', models.PositiveIntegerField(help_text='questions in query')),
                ('time', models.PositiveIntegerField(help_text='Duration of the quiz in minutes')),
                ('required_score_to_pass', models.PositiveIntegerField(help_text='Passed mark 80%')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_course_level', to='departmentDetails.level')),
            ],
            options={
                'verbose_name_plural': 'Quizes',
                'ordering': ('course_subject',),
            },
        ),
    ]
