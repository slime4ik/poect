# Generated by Django 5.1.4 on 2025-01-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_delete_accesskey_alter_post_image_alter_postw_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
