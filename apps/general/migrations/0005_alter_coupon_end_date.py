# Generated by Django 5.0.4 on 2024-04-30 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_alter_coupon_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 10, 14, 9, 43, 382782, tzinfo=datetime.timezone.utc)),
        ),
    ]
