# Generated by Django 5.1.4 on 2024-12-30 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('proc', models.CharField(max_length=100)),
                ('memory', models.CharField(max_length=100)),
                ('nvme', models.CharField(max_length=100)),
                ('internet', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
