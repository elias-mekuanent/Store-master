# Generated by Django 4.1.3 on 2023-01-09 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0070_employe_request_form1_permanent_recival_status_by_employer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe_request_form1_permanent',
            name='Recival_status_by_Employer',
            field=models.CharField(choices=[('Received ', 'Received'), ('Not_Received ', 'Not_Received')], max_length=200, null=True),
        ),
    ]
