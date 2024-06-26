# Generated by Django 5.0.2 on 2024-03-19 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Administrator', '0003_tbl_facility'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_roomDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_floor', models.CharField(max_length=50)),
                ('room_count', models.CharField(max_length=50)),
                ('room_type', models.CharField(max_length=50)),
                ('room_amount', models.CharField(max_length=50)),
                ('room_occupancy', models.CharField(max_length=50)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_roomtype')),
            ],
        ),
    ]
