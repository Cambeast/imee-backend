# Generated by Django 4.0.4 on 2022-05-15 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipoIdent', models.CharField(choices=[('TD', 'Tarjeta de identidad')], max_length=50)),
                ('identificacion', models.BigIntegerField()),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('barrio', models.TextField()),
                ('localidad', models.TextField()),
                ('telefono', models.BigIntegerField(null=True)),
                ('nivelSisben', models.PositiveSmallIntegerField()),
                ('puntajeSisben', models.FloatField()),
                ('eps', models.CharField(max_length=30)),
                ('tipoSanguinio', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('O', 'O'), ('AB', 'AB')], max_length=50)),
                ('rh', models.CharField(choices=[('+', 'Positivo'), ('-', 'Negativo')], max_length=50)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('Sin definir', 'Sin definir')], max_length=50)),
            ],
        ),
    ]
