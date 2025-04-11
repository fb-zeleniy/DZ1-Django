# Generated by Django 5.2 on 2025-04-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
