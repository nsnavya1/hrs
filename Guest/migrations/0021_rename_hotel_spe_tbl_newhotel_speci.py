# Generated by Django 5.0.4 on 2024-04-10 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0020_tbl_newhotel_hotel_spe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_newhotel',
            old_name='hotel_spe',
            new_name='speci',
        ),
    ]