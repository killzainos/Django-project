# Generated by Django 4.2.7 on 2025-01-16 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeAreDeconsultOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='عنوان')),
                ('text', models.TextField(max_length=150, verbose_name='متن توضیحات')),
            ],
        ),
        migrations.CreateModel(
            name='WeAreDeconsult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=150, verbose_name='متن توضیحات')),
                ('options', models.ManyToManyField(to='home_module.wearedeconsultoptions', verbose_name='گزینه ها')),
            ],
        ),
    ]