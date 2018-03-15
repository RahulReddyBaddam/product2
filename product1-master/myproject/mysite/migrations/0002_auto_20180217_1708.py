# Generated by Django 2.0.2 on 2018-02-17 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='descrip',
            field=models.TextField(default='', max_length=300),
            preserve_default=False,
        ),
    ]