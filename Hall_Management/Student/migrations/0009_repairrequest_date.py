# Generated by Django 4.1.1 on 2024-02-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0008_remove_repairrequest_schdeule'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairrequest',
            name='date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]