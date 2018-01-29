# -*- coding: utf-8 -*-

"""
Generar geometrias 'config.py'
Almacena informacion como rutas, variables que pueden
ser modificadas en el tiempo, con el fin de no afectar
la logica de programacion
"""

import os
import cx_Oracle as oracle

BASE_DIR = os.path.normpath(os.path.join(__file__, '../../..'))
MODULES_NEEDS = ["cx-Oracle==6.1", "pyshp==1.2.12"]

# Conexion de geodatabase mediante el RDBMS Oracle
class ConnOracle:
    def __init__(self):
        user = '******'
        password = '******'
        self.namedb = '******/******'
        self.conn = oracle.connect(user, password, self.namedb)

    def __str__(self):
        return self.namedb


# Conexion a geodatabase mediante a arcgis
class ConnArcgis:
    def __init__(self):
        self.conn = os.path.join(BASE_DIR, 'static\\test.gdb')

    def __str__(self):
        return os.path.basename(self.conn)


# Administrador de conexiones
class ManageConnect:
    def __init__(self, manage):
        if manage == 'oracle':
            self.conn = ConnOracle().conn
        elif manage == 'arcgis':
            self.conn = ConnArcgis().conn

# Archivos estaticos reutilizados
class Statics:
    def __init__(self):
        self.stat = os.path.join(BASE_DIR, 'static')
        self.prj = os.path.join(self.stat, 'prj')
        self.out = r'*:\\******\\Temporal'

    def __str__(self):
        return self.stat

# Sistemas de referencia
class Sreference:
    def __init__(self):
        self.wgs = [32717, 32718, 32719]
        self.psad = [24877, 24878, 24879]
        self.gcs = [4326]
