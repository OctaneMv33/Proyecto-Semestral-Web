# Generated by Django 4.2.1 on 2023-05-31 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrincipal', '0002_categoriatrabajo_contacto_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriatrabajo',
            name='nombre_categtrabajo',
            field=models.CharField(db_column='nombre_categtrabajo', max_length=80),
        ),
    ]
