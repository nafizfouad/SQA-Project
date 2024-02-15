# Generated by Django 4.1.1 on 2024-02-15 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0002_alter_staff_hall'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitorId', models.IntegerField(blank=True, default=0, null=True)),
                ('day', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('visit', models.CharField(blank=True, max_length=100, null=True)),
                ('arrival', models.DateTimeField(blank=True, null=True)),
                ('departure', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
