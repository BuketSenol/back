# Generated by Django 4.2.2 on 2023-07-26 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0004_rename_type_moviecard_movietype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviecard',
            old_name='movieType',
            new_name='typeTitle',
        ),
    ]
