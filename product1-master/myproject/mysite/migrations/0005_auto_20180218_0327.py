# Generated by Django 2.0.2 on 2018-02-17 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20180218_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='mysite.Category'),
        ),
    ]
