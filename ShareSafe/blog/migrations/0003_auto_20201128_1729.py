# Generated by Django 3.1.3 on 2020-11-28 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201126_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='createdby_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.user'),
        ),
    ]