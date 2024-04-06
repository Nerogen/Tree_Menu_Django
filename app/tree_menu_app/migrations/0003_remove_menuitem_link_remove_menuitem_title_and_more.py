# Generated by Django 5.0.4 on 2024-04-06 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "tree_menu_app",
            "0002_remove_menuitem_menu_remove_menuitem_named_url_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menuitem",
            name="link",
        ),
        migrations.RemoveField(
            model_name="menuitem",
            name="title",
        ),
        migrations.AddField(
            model_name="menuitem",
            name="name",
            field=models.CharField(default="home", max_length=255),
        ),
        migrations.AddField(
            model_name="menuitem",
            name="named_url",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="menuitem",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="tree_menu_app.menuitem",
            ),
        ),
        migrations.AddField(
            model_name="menuitem",
            name="url",
            field=models.CharField(default="/", max_length=255),
        ),
    ]