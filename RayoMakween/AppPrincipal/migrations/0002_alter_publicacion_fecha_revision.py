# Generated by Django 4.2.1 on 2023-06-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrincipal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_revision',
            field=models.DateTimeField(blank=True, db_column='fecha_revision', null=True),
        ),
    ]