# Generated by Django 4.1.7 on 2023-03-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoProject4', '0005_remove_student_country_student_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(blank=True, max_length=50)),
                ('productprice', models.CharField(blank=True, max_length=50)),
                ('productdescription', models.CharField(blank=True, max_length=50)),
                ('productquantity', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
