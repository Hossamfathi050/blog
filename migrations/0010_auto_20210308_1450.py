# Generated by Django 3.1.5 on 2021-03-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_arrang_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='arrang_post',
            field=models.IntegerField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
