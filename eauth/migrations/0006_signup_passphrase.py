# Generated by Django 4.0.5 on 2022-07-26 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eauth', '0005_alter_signup_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='passphrase',
            field=models.CharField(default='', max_length=500),
        ),
    ]
