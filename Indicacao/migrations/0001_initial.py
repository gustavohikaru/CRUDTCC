# Generated by Django 4.1.7 on 2023-04-05 18:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indicacao',
            fields=[
                ('Indicacao', models.AutoField(primary_key=True, serialize=False)),
                ('SUAPServidor', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999999)])),
            ],
        ),
        migrations.CreateModel(
            name='responsavel',
            fields=[
                ('id_resp', models.AutoField(primary_key=True, serialize=False)),
                ('nomeresponsavel', models.CharField(max_length=20, null=True)),
                ('endereco', models.CharField(max_length=30)),
                ('email_responsavel', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
