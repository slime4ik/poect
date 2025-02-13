# Generated by Django 5.1.4 on 2025-01-11 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_rename_posts_postw'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesskey',
            name='assigned_name',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='accesskey',
            name='used',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='accesskey',
            name='key',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
