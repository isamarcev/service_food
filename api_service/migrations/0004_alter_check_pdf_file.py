# Generated by Django 4.1.2 on 2022-10-18 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_service', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='pdf_file',
            field=models.FileField(null=True, upload_to='./media/pdf/'),
        ),
    ]
