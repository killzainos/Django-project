# Generated by Django 4.2.7 on 2025-01-16 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0004_sentences_remove_ourservice_sentences_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ourservice',
            old_name='logo',
            new_name='icon',
        ),
    ]