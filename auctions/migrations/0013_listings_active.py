# Generated by Django 4.2.5 on 2023-09-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0012_bid_listing"),
    ]

    operations = [
        migrations.AddField(
            model_name="listings",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
