# Generated by Django 4.1.3 on 2022-12-19 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0039_remove_employ_departments_employ_indepartment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student',
        ),
        migrations.AddField(
            model_name='employ',
            name='accessStore',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Store_manager.allstore'),
        ),
    ]
