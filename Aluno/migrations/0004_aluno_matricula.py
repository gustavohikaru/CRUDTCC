# Generated by Django 4.1.1 on 2023-03-06 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aluno', '0003_remove_aluno_idade'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
