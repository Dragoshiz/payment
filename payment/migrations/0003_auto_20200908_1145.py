# Generated by Django 3.1.1 on 2020-09-08 11:45

from django.db import migrations, models
import jobtest.utils


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20200908_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailcard',
            name='expiration_date',
            field=models.DateField(validators=[jobtest.utils.present_or_future_date], verbose_name='expiration date'),
        ),
    ]
