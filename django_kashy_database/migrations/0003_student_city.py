# Generated by Django 4.1.7 on 2023-03-01 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_kashy_database', '0002_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
