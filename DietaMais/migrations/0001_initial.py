# Generated by Django 5.1.3 on 2024-12-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('proteina', models.FloatField()),
                ('caloria', models.FloatField()),
                ('carboidrato', models.FloatField()),
                ('gordura', models.FloatField()),
                ('sodio', models.FloatField()),
                ('vitaminaC', models.FloatField()),
                ('ferro', models.FloatField()),
                ('magnesio', models.FloatField()),
                ('calcio', models.FloatField()),
                ('preco', models.FloatField()),
            ],
        ),
    ]
