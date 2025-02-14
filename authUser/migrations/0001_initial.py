# Generated by Django 5.0.6 on 2024-07-27 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('birth_date', models.DateField(max_length='100')),
                ('gender', models.CharField(max_length=6)),
                ('condition', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
    ]
