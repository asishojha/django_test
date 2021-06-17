# Generated by Django 3.2.4 on 2021-06-12 09:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import marks.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marks', '0011_auto_20210608_2028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'permissions': [('can_update', 'Can update the data of students'), ('can_change_password', 'Can change the password of school user')]},
        ),
        migrations.AlterField(
            model_name='student',
            name='fl',
            field=models.CharField(blank=True, max_length=2, null=True, validators=[marks.validators.validate_marks]),
        ),
        migrations.AlterField(
            model_name='student',
            name='geog',
            field=models.CharField(blank=True, max_length=2, null=True, validators=[marks.validators.validate_marks]),
        ),
        migrations.AlterField(
            model_name='student',
            name='hist',
            field=models.CharField(blank=True, max_length=2, null=True, validators=[marks.validators.validate_marks]),
        ),
        migrations.AlterField(
            model_name='student',
            name='lsc',
            field=models.CharField(blank=True, max_length=2, null=True, validators=[marks.validators.validate_marks]),
        ),
        migrations.AlterField(
            model_name='student',
            name='math',
            field=models.CharField(blank=True, max_length=2, null=True, validators=[marks.validators.validate_marks]),
        ),
        migrations.AlterField(
            model_name='student',
            name='psc',
            field=models.CharField(blank=True, max_length=2, null=True, validators=[marks.validators.validate_marks]),
        ),
        migrations.AlterField(
            model_name='student',
            name='sl',
            field=models.CharField(blank=True, max_length=2, null=True, validators=[marks.validators.validate_marks]),
        ),
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70)),
                ('phone', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('school', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
