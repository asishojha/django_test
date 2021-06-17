# Generated by Django 3.2.4 on 2021-06-07 02:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctg', models.CharField(max_length=2)),
                ('rollno', models.CharField(max_length=11)),
                ('regno', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=40)),
                ('fname', models.CharField(max_length=40)),
                ('dob', models.CharField(max_length=6)),
                ('sub1', models.CharField(max_length=2)),
                ('sub2', models.CharField(max_length=2)),
                ('sub3', models.CharField(max_length=2)),
                ('fl', models.CharField(max_length=2)),
                ('sl', models.CharField(max_length=2)),
                ('math', models.CharField(max_length=2)),
                ('psc', models.CharField(max_length=2)),
                ('lsc', models.CharField(max_length=2)),
                ('hist', models.CharField(max_length=2)),
                ('geog', models.CharField(max_length=2)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
