# Generated by Django 3.2.16 on 2022-12-18 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seminario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
                ('inscripcion', models.CharField(max_length=50)),
                ('hora', models.TimeField(null=True)),
                ('observacion', models.CharField(max_length=50)),
                ('estado_de_seminario', models.CharField(choices=[('d', 'Disponible'), ('r', 'Reservado'), ('c', 'Completado'), ('a', 'Anulado')], default='d', max_length=2)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminario.institucion')),
            ],
        ),
    ]