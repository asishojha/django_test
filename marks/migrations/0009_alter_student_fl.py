# Generated by Django 3.2.4 on 2021-06-08 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0008_auto_20210608_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fl',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
