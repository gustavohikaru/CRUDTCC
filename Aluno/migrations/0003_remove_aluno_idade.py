# Generated by Django 4.1.1 on 2023-01-12 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aluno', '0002_alter_aluno_idade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='idade',
        ),
    ]