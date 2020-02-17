# Generated by Django 3.0.3 on 2020-02-17 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200216_2133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'student_name'},
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='student_name',
        ),
        migrations.AddField(
            model_name='student',
            name='confirm_password',
            field=models.CharField(default=False, max_length=300),
        ),
        migrations.AddField(
            model_name='student',
            name='contact',
            field=models.CharField(default=False, max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='student_email',
            field=models.EmailField(default=False, max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(default=False),
        ),
    ]