# Generated by Django 2.1 on 2018-09-01 07:38

import aristotle.models
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
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('violation', models.CharField(choices=[(aristotle.models.ViolationCategory('Red line parking'), 'Red line parking')], max_length=10)),
                ('plate_number', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=256)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]