# Generated by Django 3.2 on 2022-09-08 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos_pdf', '0002_remove_contratos_nombre_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratos',
            name='contenido_del_contrato',
            field=models.TextField(),
        ),
    ]
