# Generated by Django 4.0.5 on 2022-08-10 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0005_remove_customer_billing_configuration'),
    ]

    operations = [
        migrations.AddField(
            model_name='plancomponent',
            name='metric_amount_per_cost',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='event',
            name='properties',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
