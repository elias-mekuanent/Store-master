# Generated by Django 4.1.3 on 2023-01-25 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0076_itemhistory_gift_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemhistory',
            name='Other_Reseaon',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
