# Generated by Django 5.0.2 on 2024-03-23 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0016_tbl_newhotel'),
        ('Hotel', '0010_tbl_tourpackages'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_pickanddrophead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickanddrophead_name', models.CharField(max_length=50)),
                ('pickanddrophead_amount', models.CharField(max_length=50)),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_newhotel')),
            ],
        ),
    ]
