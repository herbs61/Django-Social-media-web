# Generated by Django 4.2.2 on 2023-08-02 15:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="liked_by",
            field=models.ManyToManyField(
                blank=True, related_name="posts_liked", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
