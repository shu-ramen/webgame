# Generated by Django 2.1.7 on 2019-05-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('othello', '0003_auto_20190513_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]