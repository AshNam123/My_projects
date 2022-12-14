# Generated by Django 3.1.7 on 2021-03-23 02:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=150)),
                ('service_provider', models.TextField()),
                ('service_contact', models.CharField(max_length=20)),
                ('service_cost', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_id_ser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
