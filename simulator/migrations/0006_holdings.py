# Generated by Django 3.2.7 on 2021-10-18 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simulator', '0005_lauth'),
    ]

    operations = [
        migrations.CreateModel(
            name='holdings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('buy_price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holdings', to='simulator.league')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holdings', to='simulator.stocks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holdings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
