# Generated by Django 3.0.8 on 2020-07-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0004_done_requests_reviews_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='done_requests',
            name='reviews_added',
            field=models.TextField(null=True),
        ),
    ]