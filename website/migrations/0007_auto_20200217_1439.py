# Generated by Django 3.0.3 on 2020-02-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20200217_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(default=False, max_length=20),
        ),
    ]