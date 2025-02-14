# Generated by Django 5.0.6 on 2024-07-27 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(blank=True, max_length=256, null=True)),
                ('menu_ingredients', models.TextField(blank=True, null=True)),
                ('menu_instructions', models.TextField(blank=True, null=True)),
                ('menu_category', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'menu',
                'managed': False,
            },
        ),
    ]
