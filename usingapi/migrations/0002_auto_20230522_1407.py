# Generated by Django 3.0.5 on 2023-05-22 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usingapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_view',
            old_name='Total_buyers',
            new_name='total_buyers',
        ),
    ]
