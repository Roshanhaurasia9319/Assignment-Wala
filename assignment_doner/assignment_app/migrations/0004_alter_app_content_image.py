# Generated by Django 5.0.6 on 2024-07-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_app', '0003_app_content_alter_user_data_sheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_content',
            name='Image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
