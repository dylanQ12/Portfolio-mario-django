# Generated by Django 5.1 on 2024-09-01 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contacts_delete_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacts',
            new_name='Contact',
        ),
    ]
