# Generated by Django 2.1.5 on 2019-02-25 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("iert_news", "0010_auto_20190225_1539")]

    operations = [
        migrations.RemoveField(model_name="new", name="dislikes"),
        migrations.RemoveField(model_name="new", name="likes"),
    ]
