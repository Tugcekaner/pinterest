# Generated by Django 4.2.1 on 2023-08-07 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
