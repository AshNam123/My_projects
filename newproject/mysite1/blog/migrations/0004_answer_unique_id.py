# Generated by Django 3.1.7 on 2021-03-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210324_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='unique_id',
            field=models.IntegerField(null=True),
        ),
    ]
