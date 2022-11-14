# Generated by Django 4.1.2 on 2022-11-13 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santechnic', '0002_alter_category_options_alter_category_category_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default='', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]