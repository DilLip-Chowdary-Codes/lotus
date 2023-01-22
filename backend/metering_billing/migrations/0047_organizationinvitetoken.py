# Generated by Django 4.0.5 on 2022-10-16 04:01

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import metering_billing.models


class Migration(migrations.Migration):
    dependencies = [
        (
            "metering_billing",
            "0046_rename_old_plan_backtestsubstitution_original_plan_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="OrganizationInviteToken",
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
                ("token", models.CharField(default=uuid.uuid4, max_length=250)),
                (
                    "expire_at",
                    models.DateTimeField(default=metering_billing.models.now_plus_day),
                ),
                ("is_valid", models.BooleanField(default=True)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="org_invite_token",
                        to="metering_billing.organization",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_invite_token",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
