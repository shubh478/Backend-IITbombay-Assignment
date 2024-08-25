# Generated by Django 5.1 on 2024-08-24 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='course',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='course',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='course',
            name='course_code',
            field=models.CharField(default='DEFAULT_CODE', max_length=10, unique=True),
        ),
        migrations.CreateModel(
            name='CourseInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField(choices=[(1, 'Spring'), (2, 'Fall')])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='courses.course')),
            ],
        ),
        migrations.DeleteModel(
            name='Instance',
        ),
    ]
