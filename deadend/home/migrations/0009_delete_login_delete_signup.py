# Generated by Django 4.2.7 on 2023-12-19 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_login_signup_confirm_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login',
        ),
        migrations.DeleteModel(
            name='signup',
        ),
    ]
