# Generated by Django 3.2.7 on 2022-05-15 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0002_alter_estudiante_genero_alter_estudiante_rh'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acudiente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('NomAcu', models.CharField(max_length=50)),
                ('ideAcu', models.BigIntegerField()),
                ('direccionAcu', models.TextField()),
                ('fechaNacAcu', models.DateField()),
                ('telAcu', models.BigIntegerField(null=True)),
                ('nomPadre', models.CharField(max_length=50, null=True)),
                ('idePadre', models.BigIntegerField(null=True)),
                ('correoPadre', models.EmailField(max_length=254, null=True)),
                ('telPadre', models.BigIntegerField(null=True)),
                ('nomMadre', models.CharField(max_length=50, null=True)),
                ('ideMadre', models.BigIntegerField(null=True)),
                ('correoMadre', models.EmailField(max_length=254, null=True)),
                ('telMadre', models.BigIntegerField(null=True)),
                ('estudiante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Acudiente', to='authApp.estudiante')),
            ],
        ),
    ]