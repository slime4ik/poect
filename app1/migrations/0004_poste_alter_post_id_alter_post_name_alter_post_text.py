# Generated by Django 5.1.4 on 2025-01-11 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_accesskey_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
    ]
