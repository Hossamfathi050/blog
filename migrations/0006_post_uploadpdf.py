# Generated by Django 3.1.5 on 2021-01-30 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uploadpdf',
            field=models.FileField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
