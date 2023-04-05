# Generated by Django 4.1.7 on 2023-04-05 17:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Psicologa', '0003_remove_psicologa_id_alter_psicologa_suap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psicologa',
            name='SUAP',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999)]),
        ),
    ]