# Generated by Django 2.0.4 on 2018-04-18 22:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('NOT DONE', 'NOT DONE'), ('DONE', 'DONE')], default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
