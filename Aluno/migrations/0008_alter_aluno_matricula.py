# Generated by Django 4.1.7 on 2023-04-05 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aluno', '0007_alter_aluno_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(max_length=16, primary_key=True, serialize=False),
        ),
    ]
