# Generated by Django 4.1.3 on 2022-11-29 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0007_itemhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='form1temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Request_by', models.CharField(blank=True, max_length=100, null=True)),
                ('Department', models.CharField(blank=True, max_length=100, null=True)),
                ('checkd_by', models.CharField(blank=True, max_length=100, null=True)),
                ('Approved_by', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='form2temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('unit', models.CharField(blank=True, max_length=100, null=True)),
                ('qty', models.CharField(blank=True, max_length=100, null=True)),
                ('Remark', models.CharField(blank=True, max_length=100, null=True)),
                ('form1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Store_manager.form1temp')),
            ],
        ),
    ]
