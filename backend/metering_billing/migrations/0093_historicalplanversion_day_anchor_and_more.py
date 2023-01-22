# Generated by Django 4.0.5 on 2022-12-02 00:51

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0092_alter_invoicelineitem_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalplanversion",
            name="day_anchor",
            field=models.SmallIntegerField(
                blank=True,
                default=1,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(31),
                ],
            ),
        ),
        migrations.AddField(
            model_name="historicalplanversion",
            name="month_anchor",
            field=models.SmallIntegerField(
                blank=True,
                default=1,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(12),
                ],
            ),
        ),
        migrations.AddField(
            model_name="planversion",
            name="day_anchor",
            field=models.SmallIntegerField(
                blank=True,
                default=1,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(31),
                ],
            ),
        ),
        migrations.AddField(
            model_name="planversion",
            name="month_anchor",
            field=models.SmallIntegerField(
                blank=True,
                default=1,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(12),
                ],
            ),
        ),
        migrations.AddField(
            model_name="subscription",
            name="filters",
            field=models.ManyToManyField(
                blank=True, to="metering_billing.categoricalfilter"
            ),
        ),
        migrations.CreateModel(
            name="SubscriptionManager",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "day_anchor",
                    models.SmallIntegerField(
                        blank=True,
                        default=1,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(31),
                        ],
                    ),
                ),
                (
                    "month_anchor",
                    models.SmallIntegerField(
                        blank=True,
                        default=1,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(12),
                        ],
                    ),
                ),
                (
                    "customer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscription_manager",
                        to="metering_billing.customer",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscription_managers",
                        to="metering_billing.organization",
                    ),
                ),
            ],
        ),
    ]
