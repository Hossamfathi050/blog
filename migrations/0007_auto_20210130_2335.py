# Generated by Django 3.1.5 on 2021-01-30 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_uploadpdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uploadpdf',
            field=models.FileField(upload_to='uploadpdf/'),
        ),
    ]