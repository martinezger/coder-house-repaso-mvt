# Generated by Django 4.0.4 on 2022-05-19 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='email',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
