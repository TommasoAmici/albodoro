# Generated by Django 2.0.4 on 2018-04-27 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albo', '0036_position_matchday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='draws',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='fantapunti',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='goal_against',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='goal_for',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='losses',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='played',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='points',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='wins',
            field=models.IntegerField(default=0, null=True),
        ),
    ]