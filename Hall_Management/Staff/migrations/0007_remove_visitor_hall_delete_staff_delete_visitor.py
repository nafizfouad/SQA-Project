# Generated by Django 4.1.1 on 2024-02-16 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0006_visitor_hall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='hall',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.DeleteModel(
            name='Visitor',
        ),
    ]
