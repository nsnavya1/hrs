# Generated by Django 5.0.2 on 2024-04-06 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0018_alter_tbl_newhotel_hotel_floor'),
        ('User', '0016_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_title', models.CharField(max_length=50)),
                ('complaint_description', models.CharField(max_length=200)),
                ('complaint_reply', models.CharField(max_length=200)),
                ('complaint_status', models.IntegerField(default='0')),
                ('complaint_date', models.DateField(auto_now_add=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_newhotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
