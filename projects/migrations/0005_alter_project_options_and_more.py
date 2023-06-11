# Generated by Django 4.2.1 on 2023-06-06 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_remove_profile_social_twitter_message"),
        ("projects", "0004_project_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={"ordering": ["-vote_ratio", "-vote_total", "title"]},
        ),
        migrations.RenameField(
            model_name="project",
            old_name="votes_total",
            new_name="vote_ratio",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="votes_ratio",
            new_name="vote_total",
        ),
        migrations.AddField(
            model_name="review",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.profile",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="review",
            unique_together={("owner", "project")},
        ),
    ]
