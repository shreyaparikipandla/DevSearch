# Generated by Django 4.2.1 on 2023-06-06 18:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_profile_location_skill"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="social_twitter",
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("email", models.EmailField(blank=True, max_length=200, null=True)),
                ("subject", models.CharField(blank=True, max_length=200, null=True)),
                ("body", models.TextField()),
                ("is_read", models.BooleanField(default=False, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="messages",
                        to="users.profile",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="users.profile",
                    ),
                ),
            ],
            options={
                "ordering": ["is_read", "-created"],
            },
        ),
    ]
