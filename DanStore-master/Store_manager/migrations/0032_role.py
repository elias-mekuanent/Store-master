# Generated by Django 4.1.3 on 2022-12-14 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0031_employ_departments'),
    ]

    operations = [
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roleName', models.CharField(max_length=100)),
                ('roleMembers', models.IntegerField(max_length=100)),
            ],
        ),
    ]
