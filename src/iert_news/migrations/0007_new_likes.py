# Generated by Django 2.1.5 on 2019-02-25 08:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("iert_news", "0006_auto_20190211_2245"),
    ]

    operations = [
        migrations.AddField(
            model_name="new",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="new_likes", to=settings.AUTH_USER_MODEL
            ),
        )
    ]
