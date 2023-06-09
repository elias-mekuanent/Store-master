# Generated by Django 4.1.3 on 2023-01-02 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0059_rename_action_employe_request_form1_dept_head_action_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employe_request_form1',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='employe_request_form1',
            name='Remark',
        ),
        migrations.RemoveField(
            model_name='employe_request_form1',
            name='req_qty',
        ),
        migrations.RemoveField(
            model_name='employe_request_form1',
            name='unit',
        ),
        migrations.CreateModel(
            name='employe_request_form2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('unit', models.CharField(blank=True, max_length=100, null=True)),
                ('req_qty', models.CharField(blank=True, max_length=100, null=True)),
                ('Remark', models.CharField(blank=True, max_length=100, null=True)),
                ('employe_request_form1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Store_manager.employe_request_form1')),
            ],
        ),
    ]
