# Generated by Django 5.0.2 on 2024-02-25 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='remedios',
        ),
        migrations.AddField(
            model_name='paciente',
            name='remedios',
            field=models.ManyToManyField(to='cadastro.remedio'),
        ),
    ]
