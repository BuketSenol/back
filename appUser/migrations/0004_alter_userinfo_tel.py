# Generated by Django 4.2.2 on 2023-07-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0003_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='tel',
            field=models.CharField(default='-', max_length=50, verbose_name='Telefon'),
        ),
    ]
