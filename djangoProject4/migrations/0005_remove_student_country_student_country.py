# Generated by Django 4.1.7 on 2023-03-02 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoProject4', '0004_student_country_alter_student_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Country',
        ),
        migrations.AddField(
            model_name='student',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
