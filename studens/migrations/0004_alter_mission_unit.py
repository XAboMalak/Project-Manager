# Generated by Django 4.1.4 on 2022-12-28 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studens', '0003_mission_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='unit',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium')], max_length=1),
        ),
    ]