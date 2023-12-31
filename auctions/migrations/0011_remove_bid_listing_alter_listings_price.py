# Generated by Django 4.2.5 on 2023-09-18 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0010_alter_bid_bid_alter_listings_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bid",
            name="listing",
        ),
        migrations.AlterField(
            model_name="listings",
            name="price",
            field=models.ForeignKey(
                blank=True,
                default=40.0,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="auctions.bid",
            ),
        ),
    ]
