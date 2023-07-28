# Generated by Django 4.2.2 on 2023-07-26 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appMy', '0009_remove_moviecard_category_remove_moviecard_movietype_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catetitle', models.CharField(max_length=50, verbose_name='Kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Tür')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Film/dizi')),
                ('image', models.ImageField(max_length=200, upload_to='image', verbose_name='Resim')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.category', verbose_name='Kategori')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.type', verbose_name='Tür')),
            ],
        ),
    ]
