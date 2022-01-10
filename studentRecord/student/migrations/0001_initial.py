# Generated by Django 3.2.7 on 2022-01-10 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('Rollno', models.IntegerField(default='', max_length=2, primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(default='', max_length=70)),
                ('Class', models.IntegerField(default='', max_length=2)),
                ('School', models.CharField(default='', max_length=200)),
                ('Mobile', models.IntegerField(default='', max_length=10)),
                ('Address', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAcademics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Math', models.IntegerField(default='', max_length=3)),
                ('Physics', models.IntegerField(default='', max_length=3)),
                ('Chemistry', models.IntegerField(default='', max_length=3)),
                ('Biology', models.IntegerField(default='', max_length=3)),
                ('English', models.IntegerField(default='', max_length=3)),
                ('Rollno', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='student.studentinfo', unique=True)),
            ],
        ),
    ]
