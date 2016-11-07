# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Desaparecido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FECHA_ALTA', models.DateTimeField(auto_now_add=True)),
                ('FECHA_ACTUALIZACION', models.DateTimeField(auto_now=True)),
                ('fecha_desaparicion', models.DateTimeField()),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('primer_apellido', models.CharField(max_length=50, blank=True)),
                ('segundo_apellido', models.CharField(max_length=50, blank=True)),
                ('punto_desaparecido', django.contrib.gis.db.models.fields.PointField(default='POINT(0 0)', srid=4326)),
                ('num_de_identificacion', models.CharField(max_length=50, blank=True)),
                ('TIPO_DE_IDENTIFICACION', models.CharField(blank=True, max_length=2, choices=[('I', 'IFE'), ('P', 'PASAPORTE'), ('L', 'LICENCIA DE MANEJO'), ('O', 'OTRO')])),
                ('sexo', models.CharField(blank=True, max_length=2, choices=[('M', 'Masculino'), ('F', 'Femenino')])),
                ('orientacion_sexual', models.CharField(max_length=50, blank=True)),
                ('intervencion_quirurgica_modificar_sexo', models.CharField(max_length=50, blank=True)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('edad_aproximada', models.IntegerField()),
                ('nacionalidad', models.CharField(default='Mexicano(a)', max_length=50, blank=True)),
                ('descripcion_fisica_desaparecido', models.CharField(max_length=300, blank=True)),
                ('estatura', models.IntegerField()),
                ('complexion', models.CharField(max_length=50, blank=True)),
                ('tez', models.CharField(max_length=50, blank=True)),
                ('tipo_de_cabello', models.CharField(max_length=50, blank=True)),
                ('color_cabello', models.CharField(max_length=50, blank=True)),
                ('color_de_ojos', models.CharField(max_length=50, blank=True)),
                ('tiene_muestras_geneticas', models.CharField(max_length=2, blank=True)),
                ('numero_referencia_de_muestra', models.CharField(max_length=50, blank=True)),
                ('institucon_que_la_tomo', models.CharField(max_length=50, blank=True)),
                ('senias_particulares', models.CharField(max_length=300, blank=True)),
                ('grupo_etnico', models.CharField(max_length=50, blank=True)),
                ('migrante', models.CharField(max_length=50, blank=True)),
                ('pais_origen', models.CharField(max_length=50, blank=True)),
                ('fue_encontrado', models.CharField(max_length=50, blank=True)),
                ('fecha_encontrado', models.CharField(max_length=50, blank=True)),
                ('estatus_encontrado', models.CharField(max_length=50, blank=True)),
                ('desaparicion_en_grupo', models.CharField(blank=True, max_length=2, verbose_name='Estaba s\xf3lo o acompa\xf1ado', choices=[('0', 'S\xf3lo'), ('1', 'Acompa\xf1ado')])),
                ('tiene_averiguacion_previa', models.CharField(blank=True, help_text='Tiene averiguacion?', max_length=2, choices=[('0', 'S\xed'), ('1', 'No')])),
                ('NUM_AVERIGUACION', models.CharField(max_length=100, blank=True)),
                ('tipo_lugar_ultimavez_visto', models.CharField(max_length=100, blank=True)),
                ('colonia_barrio_ejido_desaparicion', models.CharField(max_length=100, blank=True)),
                ('calle_desaparicion', models.CharField(max_length=100, blank=True)),
                ('numero_desaparicion', models.CharField(max_length=100, blank=True)),
                ('quien_registra', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
