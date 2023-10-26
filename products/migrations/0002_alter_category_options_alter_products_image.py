# Generated by Django 4.2.3 on 2023-08-10 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='products',
            name='Image',
            field=models.ImageField(upload_to='products/%Y/%M/%D/'),
        ),
    ]
