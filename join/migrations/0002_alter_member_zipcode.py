# Generated by Django 3.2.13 on 2022-07-12 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='zipcode',
            field=models.CharField(max_length=5),
        ),
    ]
