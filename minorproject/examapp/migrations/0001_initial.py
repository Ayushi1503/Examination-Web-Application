# Generated by Django 4.0.4 on 2022-06-18 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que_no', models.IntegerField()),
                ('que', models.TextField()),
            ],
        ),
    ]