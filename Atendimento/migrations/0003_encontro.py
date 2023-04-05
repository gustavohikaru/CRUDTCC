# Generated by Django 4.1.7 on 2023-04-05 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0002_remove_atendimento_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='encontro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desenvolvimento', models.CharField(max_length=60, null=True)),
                ('observacoes', models.CharField(max_length=300)),
                ('diadoatendimento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Atendimento.atendimento')),
            ],
        ),
    ]
