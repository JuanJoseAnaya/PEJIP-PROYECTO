# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Antojos(models.Model):
    idantojos = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'antojos'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Calendario(models.Model):
    idcalendario = models.AutoField(primary_key=True)
    peso = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    estatura = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    ultimamenstruacion = models.DateField(blank=True, null=True)
    etapavida_idetapavida = models.ForeignKey('Etapavida', models.DO_NOTHING, db_column='etapavida_idetapavida')
    calendariop_idcalendariop = models.ForeignKey('Calendariop', models.DO_NOTHING, db_column='calendariop_idcalendariop')
    tiposangre_idtiposangre = models.ForeignKey('Tiposangre', models.DO_NOTHING, db_column='tiposangre_idtiposangre')
    calendariom_idcalendariom = models.ForeignKey('Calendariom', models.DO_NOTHING, db_column='calendariom_idcalendariom')

    class Meta:
        managed = False
        db_table = 'calendario'


class Calendariom(models.Model):
    idcalendariom = models.AutoField(primary_key=True)
    diainicio = models.DateField(blank=True, null=True)
    duracion = models.CharField(max_length=45, blank=True, null=True)
    antojos_idantojos = models.ForeignKey(Antojos, models.DO_NOTHING, db_column='antojos_idantojos')
    tipoperiodo_idtipoperiodo = models.ForeignKey('Tipoperiodo', models.DO_NOTHING, db_column='tipoperiodo_idtipoperiodo')
    metodoanticonceptivo_idmetodoanticonceptivo = models.ForeignKey('Metodoanticonceptivo', models.DO_NOTHING, db_column='metodoanticonceptivo_idmetodoanticonceptivo')
    sintomas_idsintomas = models.ForeignKey('Sintomas', models.DO_NOTHING, db_column='sintomas_idsintomas')

    class Meta:
        managed = False
        db_table = 'calendariom'


class Calendariop(models.Model):
    idcalendariop = models.AutoField(primary_key=True)
    medicamentos_idmedicamentos = models.ForeignKey('Medicamentos', models.DO_NOTHING, db_column='medicamentos_idmedicamentos')
    examen_idexamen = models.ForeignKey('Examen', models.DO_NOTHING, db_column='examen_idexamen')
    sintomas_idsintomas = models.ForeignKey('Sintomas', models.DO_NOTHING, db_column='sintomas_idsintomas')
    antojos_idantojos = models.ForeignKey(Antojos, models.DO_NOTHING, db_column='antojos_idantojos')

    class Meta:
        managed = False
        db_table = 'calendariop'


class Departamento(models.Model):
    iddepartamento = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    idempresa = models.AutoField(primary_key=True)
    fax = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class Etapavida(models.Model):
    idetapavida = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)
    etapavidacol = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etapavida'


class Eventos(models.Model):
    ideventos = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    lugar = models.CharField(max_length=45, blank=True, null=True)
    informacionevento = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventos'


class Examen(models.Model):
    idexamen = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'examen'


class Genero(models.Model):
    idgenero = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genero'


class Ips(models.Model):
    idips = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)
    empresa_idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='empresa_idempresa')
    eventos_ideventos = models.ForeignKey(Eventos, models.DO_NOTHING, db_column='eventos_ideventos')
    tiposervicio_idtiposervicio = models.ForeignKey('Tiposervicio', models.DO_NOTHING, db_column='tiposervicio_idtiposervicio')

    class Meta:
        managed = False
        db_table = 'ips'


class Lugarnacimiento(models.Model):
    idlugarnacimiento = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lugarnacimiento'


class Medicamentos(models.Model):
    idmedicamentos = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicamentos'


class Metodoanticonceptivo(models.Model):
    idmetodoanticonceptivo = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metodoanticonceptivo'


class Municipio(models.Model):
    idmunicipio = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipio'


class Personacontacto(models.Model):
    idpersonacontacto = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personacontacto'


class Personas(models.Model):
    idpersonas = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    numerodocumento = models.IntegerField(blank=True, null=True)
    fechaexpedicion = models.DateField(blank=True, null=True)
    correoelectronico = models.CharField(max_length=45, blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    celularcontacto = models.IntegerField(blank=True, null=True)
    lugarnacimiento_idlugarnacimiento = models.ForeignKey(Lugarnacimiento, models.DO_NOTHING, db_column='lugarnacimiento_idlugarnacimiento')
    tipodocumento_idtipodocumento = models.ForeignKey('Tipodocumento', models.DO_NOTHING, db_column='tipodocumento_idtipodocumento')
    genero_idgenero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='genero_idgenero')
    municipio_idmunicipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='municipio_idmunicipio')
    personacontacto_idpersonacontacto = models.ForeignKey(Personacontacto, models.DO_NOTHING, db_column='personacontacto_idpersonacontacto')
    departamento_iddepartamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_iddepartamento')
    calendario_idcalendario = models.ForeignKey(Calendario, models.DO_NOTHING, db_column='calendario_idcalendario')
    tipopersona_idtipopersona = models.ForeignKey('Tipopersona', models.DO_NOTHING, db_column='tipopersona_idtipopersona')
    empresa_idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='empresa_idempresa')

    class Meta:
        managed = False
        db_table = 'personas'


class Sintomas(models.Model):
    idsintomas = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sintomas'


class Tipodocumento(models.Model):
    idtipodocumento = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipodocumento'


class Tipoperiodo(models.Model):
    idtipoperiodo = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoperiodo'


class Tipopersona(models.Model):
    idtipopersona = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipopersona'


class Tiposangre(models.Model):
    idtiposangre = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiposangre'


class Tiposervicio(models.Model):
    idtiposervicio = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiposervicio'
