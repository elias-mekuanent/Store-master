# Generated by Django 4.1.3 on 2022-11-30 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0009_form1permanent_form2permanent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form2permanent',
            name='Status',
        ),
        migrations.AlterField(
            model_name='form2permanent',
            name='form1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Store_manager.form1permanent'),
        ),
    ]
