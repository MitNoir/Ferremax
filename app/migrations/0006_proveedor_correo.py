# Generated by Django 5.0.6 on 2024-06-28 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='correo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
