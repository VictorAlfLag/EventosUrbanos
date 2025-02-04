# Generated by Django 5.1.4 on 2025-01-24 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arte', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('user', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
            ],
            options={
                'db_table': 'Audit',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('professional', 'Professional'), ('normal', 'Normal')], max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('initials', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('expired', 'Expired')], max_length=50)),
            ],
            options={
                'db_table': 'License',
            },
        ),
        migrations.AlterModelTable(
            name='eventpublication',
            table='ventPublication',
        ),
    ]
