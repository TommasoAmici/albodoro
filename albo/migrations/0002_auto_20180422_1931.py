# Generated by Django 2.0.4 on 2018-04-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='history',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='roster',
            field=models.TextField(blank=True),
        ),
    ]
