# Generated by Django 3.1.3 on 2020-11-23 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_monitoring', '0025_auto_20200910_1014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ['-rtir'], 'verbose_name': 'Website', 'verbose_name_plural': 'Suspicious Websites Monitored'},
        ),
    ]