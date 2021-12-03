# Generated by Django 3.2.7 on 2021-10-18 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('description', models.CharField(max_length=100000)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='simulator.stocks')),
            ],
        ),
    ]
