# Generated by Django 3.0.6 on 2020-05-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_monitoring', '0010_auto_20200427_1151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ['-rtir']},
        ),
        migrations.AddField(
            model_name='site',
            name='mail_A_record_ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]