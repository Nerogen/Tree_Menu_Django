# Generated by Django 5.0.4 on 2024-04-06 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tree_menu_app", "0003_remove_menuitem_link_remove_menuitem_title_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="name",
            field=models.CharField(default="home", max_length=100),
        ),
        migrations.AlterField(
            model_name="menuitem",
            name="named_url",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
