# Generated by Django 2.0.4 on 2018-04-24 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albo', '0009_remove_competition_formato'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='bench',
            field=models.IntegerField(null=True),
        ),
    ]
