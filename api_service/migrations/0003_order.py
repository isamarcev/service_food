# Generated by Django 4.1.2 on 2022-10-17 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_service', '0002_alter_check_pdf_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_id', models.IntegerField()),
                ('order', models.JSONField()),
            ],
        ),
    ]
