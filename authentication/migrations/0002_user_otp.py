# Generated by Django 4.0.4 on 2022-04-19 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
