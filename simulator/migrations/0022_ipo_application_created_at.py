# Generated by Django 3.2.7 on 2022-04-16 15:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0021_auto_20220416_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipo_application',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
