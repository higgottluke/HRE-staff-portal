# Generated by Django 2.0.7 on 2018-12-26 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20181225_2126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monitorconnection',
            options={'verbose_name': 'Monitor', 'verbose_name_plural': 'Connected Monitors'},
        ),
        migrations.AlterField(
            model_name='asset',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='audio_outputs',
            field=models.ManyToManyField(blank=True, to='inventory.AudioPortType'),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='audio_inputs',
            field=models.ManyToManyField(blank=True, to='inventory.AudioPortType'),
        ),
        migrations.AlterField(
            model_name='monitorconnection',
            name='monitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Monitor', unique=True),
        ),
    ]