# -*- coding: utf-8 -*-


from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0006_populate_uuid_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
