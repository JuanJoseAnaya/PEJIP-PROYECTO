# Generated by Django 4.0.4 on 2022-05-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antojos',
            fields=[
                ('idantojos', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'antojos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('idcalendario', models.AutoField(primary_key=True, serialize=False)),
                ('peso', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('estatura', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('ultimamenstruacion', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'calendario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Calendariom',
            fields=[
                ('idcalendariom', models.AutoField(primary_key=True, serialize=False)),
                ('diainicio', models.DateField(blank=True, null=True)),
                ('duracion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'calendariom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Calendariop',
            fields=[
                ('idcalendariop', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'calendariop',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('iddepartamento', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('idempresa', models.AutoField(primary_key=True, serialize=False)),
                ('fax', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'empresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Etapavida',
            fields=[
                ('idetapavida', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
                ('etapavidacol', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'etapavida',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('ideventos', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('hora', models.TimeField(blank=True, null=True)),
                ('lugar', models.CharField(blank=True, max_length=45, null=True)),
                ('informacionevento', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'eventos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('idexamen', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'examen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idgenero', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'genero',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ips',
            fields=[
                ('idips', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'ips',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lugarnacimiento',
            fields=[
                ('idlugarnacimiento', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'lugarnacimiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medicamentos',
            fields=[
                ('idmedicamentos', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'medicamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Metodoanticonceptivo',
            fields=[
                ('idmetodoanticonceptivo', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'metodoanticonceptivo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('idmunicipio', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Personacontacto',
            fields=[
                ('idpersonacontacto', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'personacontacto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('idpersonas', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('apellido', models.CharField(blank=True, max_length=45, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('fechanacimiento', models.DateField(blank=True, null=True)),
                ('numerodocumento', models.IntegerField(blank=True, null=True)),
                ('fechaexpedicion', models.DateField(blank=True, null=True)),
                ('correoelectronico', models.CharField(blank=True, max_length=45, null=True)),
                ('celular', models.IntegerField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=45, null=True)),
                ('celularcontacto', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'personas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sintomas',
            fields=[
                ('idsintomas', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'sintomas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipodocumento',
            fields=[
                ('idtipodocumento', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tipodocumento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipoperiodo',
            fields=[
                ('idtipoperiodo', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tipoperiodo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipopersona',
            fields=[
                ('idtipopersona', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tipopersona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tiposangre',
            fields=[
                ('idtiposangre', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tiposangre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tiposervicio',
            fields=[
                ('idtiposervicio', models.AutoField(primary_key=True, serialize=False)),
                ('denominacion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tiposervicio',
                'managed': False,
            },
        ),
    ]
