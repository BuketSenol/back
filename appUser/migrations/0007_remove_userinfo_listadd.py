# Generated by Django 4.2.2 on 2023-07-26 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0006_userinfo_listadd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='listadd',
        ),
    ]
