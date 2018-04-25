# Generated by Django 2.0.4 on 2018-04-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albo', '0017_auto_20180424_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchroster',
            name='matchday',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bonus',
            name='value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='performance',
            name='fantavote',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='performance',
            name='vote',
            field=models.FloatField(null=True),
        ),
    ]
