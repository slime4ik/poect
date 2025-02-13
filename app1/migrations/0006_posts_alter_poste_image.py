# Generated by Django 5.1.4 on 2025-01-11 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_post_options_alter_poste_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='imagess')),
            ],
            options={
                'verbose_name': 'Темы',
                'verbose_name_plural': 'СЭВС',
            },
        ),
        migrations.AlterField(
            model_name='poste',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imagese'),
        ),
    ]
