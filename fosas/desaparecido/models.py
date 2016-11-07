# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Desaparecido(models.Model):
    quien_registra = models.ForeignKey(User)
    FECHA_ALTA = models.DateTimeField(auto_now_add=True)
    FECHA_ACTUALIZACION = models.DateTimeField(auto_now=True)
    fecha_desaparicion= models.DateTimeField()

    nombre = models.CharField(max_length=50, blank=True)    
    primer_apellido = models.CharField(max_length=50, blank=True)
    segundo_apellido = models.CharField(max_length=50, blank=True)
    punto_desaparecido = models.PointField(default='POINT(0 0)', srid=4326)
    @property
    def longitude(self):
        return self.punto_desaparecido[0]
    @property
    def latitude(self):
        return self.punto_desaparecido[1]


    num_de_identificacion= models.CharField(max_length=50, blank=True)
    TIPO_DE_IDENTIFICACION_OPT= (
        ('I', 'IFE'),
        ('P', 'PASAPORTE'),
        ('L', 'LICENCIA DE MANEJO'), 
        ('O', 'OTRO') 
    )
    TIPO_DE_IDENTIFICACION=models.CharField(max_length=2, choices= TIPO_DE_IDENTIFICACION_OPT,
                                            blank=True)
    
    SEXO_OPT= (
        ('M', 'Masculino'),
        ('F', 'Femenino'), 
    )
    sexo = models.CharField(max_length=2, choices= SEXO_OPT,blank=True)

    orientacion_sexual = models.CharField(max_length=50, blank=True)
    intervencion_quirurgica_modificar_sexo = models.CharField(max_length=50, blank=True)
    fecha_nacimiento=models.DateTimeField()
    edad_aproximada=models.IntegerField()
    nacionalidad=models.CharField(max_length=50, blank=True,default="Mexicano(a)")
    pais_origen=models.CharField(max_length=50, blank=True, default="México")
    #ESTADO_PROCEDENCIA=
    #MUNICIPIO_PROCEDENCIA=
    #LOCALIDAD_PROCEDENCIA
    descripcion_fisica_desaparecido=models.CharField(max_length=300, blank=True)
    estatura=models.IntegerField()
    complexion= models.CharField(max_length=50, blank=True)
    tez=models.CharField(max_length=50, blank=True)
    tipo_de_cabello= models.CharField(max_length=50, blank=True)
    color_cabello= models.CharField(max_length=50, blank=True)
    color_de_ojos= models.CharField(max_length=50, blank=True)
    tiene_muestras_geneticas = models.CharField(max_length=2, blank=True)
    numero_referencia_de_muestra = models.CharField(max_length=50, blank=True)
    institucon_que_la_tomo = models.CharField(max_length=50, blank=True)
    senias_particulares = models.CharField(max_length=300, blank=True)
    grupo_etnico = models.CharField(max_length=50, blank=True)
    migrante = models.CharField(max_length=50, blank=True)
    pais_origen = models.CharField(max_length=50, blank=True)
    fue_encontrado = models.CharField(max_length=50, blank=True)
    fecha_encontrado = models.CharField(max_length=50, blank=True)
    estatus_encontrado = models.CharField(max_length=50, blank=True)
    SOLO_OPT= (
        ('0', 'Sólo'),
        ('1', 'Acompañado'), 
    )
    desaparicion_en_grupo = models.CharField(max_length=2,blank=True, 
                            verbose_name='Estaba sólo o acompañado', choices = SOLO_OPT)
    AVERIGUACION_OPT= (
        ('0', 'Sí'),
        ('1', 'No'), 
    )
    tiene_averiguacion_previa = models.CharField(max_length=2,blank=True, 
                                                choices=AVERIGUACION_OPT,
                                                help_text="Tiene averiguacion?")
    NUM_AVERIGUACION = models.CharField(max_length=100, blank=True)


    tipo_lugar_ultimavez_visto=models.CharField(max_length=100, blank=True)

    #ESTADO=
    #MUNICIPIO=
    #LOCALIDAD=
    colonia_barrio_ejido_desaparicion=models.CharField(max_length=100, blank=True) #dsp es desaparicion
    calle_desaparicion=models.CharField(max_length=100, blank=True)
    numero_desaparicion=models.CharField(max_length=100, blank=True)
    def __str__(self):
        return "%s" % (self.nombre, ' ',self.primer_apellido, ' ', self.segundo_apellido)
"""
---ID_DESAPARECIDO
---USUARIO

DATOS_GENERALES_DESAPARICION

TIPO_LUGARULTIMAVEZVISTO
FECHA_DESAPARICION
NUM_REPORTE_DESAPARICION
ESTADO
MUNICIPIO
LOCALIDAD
COLONIA_BARRIO_EJIDO
CALLE
NUMERO

DATOS_GENERALES_DESAPARECIDO

NÚMERO DE IDENTIFICACIÓN
TIPO DE IDENTIFICACIÓN
SEXO
ORIENTACIÓN SEXUAL
ALGUNA INTERVENCIÓN QUIRURGICA PARA MODIFICAR SU SEXO
FECHANACIMIENTO
EDADAPROXIMADA
NACIONALIDAD
PAIS_ORIGEN
ESTADO_PROCEDENCIA
MUNICIPIO_PROCEDENCIA
LOCALIDAD_PROCEDENCIA
DESCRIPCION_FISICA_DESAPARECIDO
ESTATURA
COMPLEXION
TEZ
TIPODECABELLO
COLOR CABELLO
COLOR DE OJOS
MUESTRAS_GENETICAS
NUMERO_REFERENCIA_DE_MUESTRA
INSTITUCON_QUE_LA_TOMO
SEÑAS_PARTICULARES
DATOS_ADICIONALES
GRUPO_ETNICO
MIGRANTE
PAIS_ORIGEN*
DATOS_ENCONTRADO
ENCONTRADO
FECHA_ENCONTRADO
"""

