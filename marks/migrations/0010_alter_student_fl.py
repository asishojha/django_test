# Generated by Django 3.2.4 on 2021-06-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0009_alter_student_fl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fl',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]