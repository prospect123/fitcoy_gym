# Generated by Django 3.2.4 on 2021-08-31 08:12

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('zfitcoy', '0007_auto_20210830_0631'),
    ]

    operations = [
        migrations.CreateModel(
            name='COMPANEY_LISENCE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont', djrichtextfield.models.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='COMPANEY_SUPPORTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont', djrichtextfield.models.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FAQs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont', djrichtextfield.models.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PRIVACY_POLICYs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont', djrichtextfield.models.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TERMS_CONDITIONSs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont', djrichtextfield.models.RichTextField(null=True)),
            ],
        ),
    ]