# Generated by Django 3.2.4 on 2021-09-05 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zfitcoy', '0012_auto_20210905_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCQQUCTIONS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=200)),
                ('ans', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
